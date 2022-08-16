package com.ufcg.psoft.scrum_board.service;

import java.util.List;
import java.util.stream.Collectors;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.ufcg.psoft.scrum_board.dto.AddUserToUserStoryDTO;
import com.ufcg.psoft.scrum_board.dto.NewUserStoryDTO;
import com.ufcg.psoft.scrum_board.dto.UpdateUserStoryDTO;
import com.ufcg.psoft.scrum_board.dto.UserStoryDTO;
import com.ufcg.psoft.scrum_board.exception.InappropriateRoleException;
import com.ufcg.psoft.scrum_board.exception.ProjectNotFoundException;
import com.ufcg.psoft.scrum_board.exception.UnauthorizedAccessException;
import com.ufcg.psoft.scrum_board.exception.UserNotFoundException;
import com.ufcg.psoft.scrum_board.exception.UserStoryAlreadyExistsException;
import com.ufcg.psoft.scrum_board.exception.UserStoryNotFoundException;
import com.ufcg.psoft.scrum_board.model.Project;
import com.ufcg.psoft.scrum_board.model.User;
import com.ufcg.psoft.scrum_board.model.UserStory;
import com.ufcg.psoft.scrum_board.repository.ProjectRepository;
import com.ufcg.psoft.scrum_board.repository.UserRepository;
import com.ufcg.psoft.scrum_board.repository.UserStoryRepository;
import com.ufcg.psoft.scrum_board.utils.UserStoryMapper;

@Service
public class UserStoryService {

    @Autowired
    private UserStoryRepository userStoryRep;

    @Autowired
    private UserRepository userRep;

    @Autowired
    private ProjectRepository projectRepository;


    public UserStoryDTO addUserStory(NewUserStoryDTO newUserStoryDTO, String loggedUsername) throws UserStoryAlreadyExistsException, ProjectNotFoundException, UserNotFoundException, UnauthorizedAccessException {
        
        Project project = this.projectRepository.getProjectById(newUserStoryDTO.getProjectId());
        if (project == null) throw new ProjectNotFoundException("The project with id '" + newUserStoryDTO.getProjectId() + "' was not found!");

        verifyUserStoryAlreadyExists(newUserStoryDTO);

        User user = this.userRep.getUserByUsername(loggedUsername);
        if (user == null) throw new UserNotFoundException("The user with username '" + loggedUsername + "' was not found!");

        verifyParticipationInProject(project, user);

        UserStory userStory = new UserStory(newUserStoryDTO.getTitle(), newUserStoryDTO.getDescription(), project);

        this.userStoryRep.addUserStory(userStory);
        return UserStoryMapper.convertToUserStoryDTO(userStory);
    }


    public void verifyUserStoryAlreadyExists(NewUserStoryDTO newUserStoryDTO) throws UserStoryAlreadyExistsException {
        UserStoryDTO userStoryDTO = findUserStoryByTitle(newUserStoryDTO.getTitle());
        if (userStoryDTO != null && userStoryDTO.getProjectId().equals(newUserStoryDTO.getProjectId())) throw new UserStoryAlreadyExistsException(userStoryDTO + " already exists!");
    }
    

    private UserStory findUserStoryById(String id_UserStory) throws UserStoryNotFoundException {
        UserStory userStory = this.userStoryRep.findUserStoryById(id_UserStory);

        if (userStory == null) throw new UserStoryNotFoundException(userStory + " not found!");

        return userStory;
        
    }

    public UserStoryDTO getUserStoryById(String id_UserStory) throws UserStoryNotFoundException{
        return UserStoryMapper.convertToUserStoryDTO(this.findUserStoryById(id_UserStory));

    }


    public UserStoryDTO updateUserStory(UpdateUserStoryDTO updateUserStoryDTO, String loggedUsername) throws UserStoryNotFoundException, UnauthorizedAccessException {
        UserStory userStory = this.findUserStoryById(updateUserStoryDTO.getId());
        this.verifyAuthorization(userStory, loggedUsername);

        userStory.setTitle(updateUserStoryDTO.getTitle());
        userStory.setDescription(updateUserStoryDTO.getDescription());
        
        List<User> devs = userRep.getUsersByUsername(updateUserStoryDTO.getDevs());
        userStory.setDevs(devs);

        if(updateUserStoryDTO.isMoveToNextState()) userStory.moveToNextStage();

        userStoryRep.editUserStory(userStory);

        return UserStoryMapper.convertToUserStoryDTO(userStory);
    }

    private void verifyAuthorization(UserStory userStory, String loggedUsername) throws UnauthorizedAccessException {
        if (userStory.getDevs().stream().noneMatch(d -> d.getUsername().equals(loggedUsername))) throw new UnauthorizedAccessException("The user '" + loggedUsername + "' is not authorized to peform this operation in this User Story!");
    }

    public void deleteUserStory(String id_UserStory, String loggedUsername) throws UserStoryNotFoundException, UnauthorizedAccessException {
        UserStory userStory = this.findUserStoryById(id_UserStory);
        this.verifyAuthorization(userStory, loggedUsername);
        this.userStoryRep.delUserStory(id_UserStory);

    }

    private UserStoryDTO findUserStoryByTitle(String title) {
        UserStoryDTO userStoryFound = null;
        for (UserStoryDTO userStory : getAllUserStories()) {
            if(userStory.getTitle().equals(title)){
                userStoryFound = userStory;
            }
        }
        return userStoryFound;
    }


    public List<UserStoryDTO> getAllUserStories() {
        return this.userStoryRep.getAll().stream().map(us -> UserStoryMapper.convertToUserStoryDTO(us)).collect(Collectors.toList());
        
    }

    public UserStoryDTO joinUserStory(String loggedUsername, String userStoryId) throws UserNotFoundException, UserStoryNotFoundException, InappropriateRoleException {
        User user = this.userRep.getUserByUsername(loggedUsername);
        if (user == null) throw new UserNotFoundException("The user with username '" + loggedUsername + "' was not found!");

        UserStory userStory = this.findUserStoryById(userStoryId);

        this.verifyParticipationInDevelopmentTeam(userStory.getProject(), user);

        userStory.addDev(user);

        this.userStoryRep.editUserStory(userStory);

        return UserStoryMapper.convertToUserStoryDTO(userStory);
    }


    private void verifyParticipationInDevelopmentTeam(Project project, User user) throws InappropriateRoleException {
        if (
            project.getDevelopers().stream().noneMatch(u -> u.equals(user)) &&
            project.getResearchers().stream().noneMatch(u -> u.equals(user)) &&
            project.getTrainees().stream().noneMatch(u -> u.equals(user))
        ) throw new InappropriateRoleException("The user with username '" + user.getUsername() + "' has not the role to join this User Story!");
    }


    private void verifyParticipationInProject(Project project, User user) throws UnauthorizedAccessException {
        if (
            project.getDevelopers().stream().noneMatch(u -> u.equals(user)) &&
            project.getResearchers().stream().noneMatch(u -> u.equals(user)) &&
            project.getTrainees().stream().noneMatch(u -> u.equals(user)) &&
            !project.getScrumMaster().equals(user) &&
            !project.getProductOwner().equals(user)
        ) throw new UnauthorizedAccessException("The user with username '" + user.getUsername() + "' has not the permission to perform this action!");
    }
    
    

    
    
}

package com.ufcg.psoft.scrum_board.service;

import com.ufcg.psoft.scrum_board.dto.AddUserToProjectDTO;
import com.ufcg.psoft.scrum_board.dto.NewProjectDTO;
import com.ufcg.psoft.scrum_board.dto.ProjectDTO;
import com.ufcg.psoft.scrum_board.enums.ScrumRoleEnum;
import com.ufcg.psoft.scrum_board.exception.InappropriateRoleException;
import com.ufcg.psoft.scrum_board.exception.ProjectAlreadyExistsException;
import com.ufcg.psoft.scrum_board.exception.ProjectNotFoundException;
import com.ufcg.psoft.scrum_board.exception.UnauthorizedAccessException;
import com.ufcg.psoft.scrum_board.exception.UnavailableRoleException;
import com.ufcg.psoft.scrum_board.exception.UserNotFoundException;
import com.ufcg.psoft.scrum_board.factory.ScrumRoleFactory;
import com.ufcg.psoft.scrum_board.model.Project;
import com.ufcg.psoft.scrum_board.model.User;
import com.ufcg.psoft.scrum_board.repository.ProjectRepository;
import com.ufcg.psoft.scrum_board.repository.UserRepository;
import com.ufcg.psoft.scrum_board.utils.ProjectMapper;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class ProjectService {

    @Autowired
    private ProjectRepository projectRep;


    @Autowired
    private UserRepository userRep;


    public ProjectDTO addProject(NewProjectDTO newProjectDTO, String loggedUsername) throws UserNotFoundException {

        User scrumMaster = userRep.getUserByUsername(loggedUsername);
        if (scrumMaster == null) throw new UserNotFoundException("The user with username '" + loggedUsername + "' was not found! Project not created!");

        Project project = new Project(newProjectDTO.getName(), newProjectDTO.getDescription(), newProjectDTO.getPartnerInstitution(), scrumMaster);

        this.projectRep.addProject(project);

        return ProjectMapper.convertToProjectDTO(project);
    }


    public void verifyProjectAlreadyExists(String projectId) throws ProjectAlreadyExistsException {
        Project project = this.projectRep.getProjectById(projectId);
        if (project != null) throw new ProjectAlreadyExistsException("Project already exists!");
    }


    public ProjectDTO findProjectById(String projectId) throws ProjectNotFoundException {
        Project project = this.getProjectById(projectId);

        return ProjectMapper.convertToProjectDTO(project);
    }


    public List<ProjectDTO> findProjectsByProductOwner(String username) {
        return projectRep.getProjectsByProjectOwner(username)
                    .stream()
                    .map(p -> ProjectMapper.convertToProjectDTO(p))
                    .collect(Collectors.toList());
    }


    public List<ProjectDTO> findProjectsByScrumMaster(String username) {
        return projectRep.getProjectsByScrumMaster(username)
                    .stream()
                    .map(p -> ProjectMapper.convertToProjectDTO(p))
                    .collect(Collectors.toList());
    }


    public List<ProjectDTO> getAllProjects() {
        List<ProjectDTO> projectsFound = projectRep.getAll()
                                            .stream()
                                            .map(p -> ProjectMapper.convertToProjectDTO(p))
                                            .collect(Collectors.toList());
        
        return projectsFound;
    }


    public ProjectDTO updateProject(String loggedUsername, ProjectDTO projectDTO) throws UnauthorizedAccessException, ProjectNotFoundException {
        Project project = this.getProjectById(projectDTO.getId());

        this.verifyAuthorization(project, loggedUsername);

        project.setName(projectDTO.getName());
        project.setDescription(projectDTO.getDescription());
        project.setPartnerInstitution(projectDTO.getPartnerInstitution());
        project.setScrumMaster(project.getScrumMaster());
        project.setProductOwner(project.getProductOwner());
        project.setDevelopers(project.getDevelopers());
        project.setDevelopers(project.getResearchers());
        project.setDevelopers(project.getTrainees());

        this.projectRep.editProject(project);

        return ProjectMapper.convertToProjectDTO(project);
    }


    public void deleteProject(String projectId, String loggedUsername) throws ProjectNotFoundException, UnauthorizedAccessException {
        Project project = this.getProjectById(projectId);

        this.verifyAuthorization(project, loggedUsername);

        this.projectRep.delProject(projectId);
    }


    private void verifyAuthorization(Project project, String username) throws UnauthorizedAccessException {
        if (!project.getScrumMaster().getUsername().equals(username)) { 
            throw new UnauthorizedAccessException("The user '" + username + "' is not authorized to peform this operation in this project!");
        }
    }


    private Project getProjectById(String projectId) throws ProjectNotFoundException {
        Project project = this.projectRep.getProjectById(projectId);
        if (project == null) throw new ProjectNotFoundException("The project with id '" + projectId + "' was not found!");
        return project;
    }


    private void verifyUserRoles(User user, ScrumRoleEnum sre) throws InappropriateRoleException {
        if (!user.getRoles().stream().anyMatch(r -> r.getScrumRoleEnum().equals(sre))) {
            throw new InappropriateRoleException("The user with username '" + user.getUsername() + "' does not have the role "+ sre.name() +"!" );
        }
    }


    private User getUserByUsername(String username) throws UserNotFoundException {
        User user = this.userRep.getUserByUsername(username);
        if (user == null) {
            throw new UserNotFoundException("The user with username '" + username + "' was not found!");
        }
        return user;
    }


    public ProjectDTO addUserToProject(String loggedUsername, AddUserToProjectDTO addUserToProjectDTO) throws ProjectNotFoundException, UnauthorizedAccessException, UserNotFoundException, InappropriateRoleException, UnavailableRoleException {
        Project project = this.getProjectById(addUserToProjectDTO.getProjectId());

        verifyAuthorization(project, loggedUsername);

        User user = this.getUserByUsername(addUserToProjectDTO.getUsername());

        ScrumRoleFactory srf = new ScrumRoleFactory();
        srf.verifyRole(addUserToProjectDTO.getRole());
        ScrumRoleEnum sre = srf.getEnumByString(addUserToProjectDTO.getRole());

        verifyUserRoles(user, sre);
        
        project.addUserToProject(user, sre);
        
        this.projectRep.editProject(project);

        return ProjectMapper.convertToProjectDTO(project);
    }

}

package com.ufcg.psoft.scrum_board.service;

import java.util.List;
import java.util.stream.Collectors;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.ufcg.psoft.scrum_board.dto.NewTaskDTO;
import com.ufcg.psoft.scrum_board.dto.TaskDTO;
import com.ufcg.psoft.scrum_board.dto.UpdateTaskDTO;
import com.ufcg.psoft.scrum_board.exception.TaskAlreadyDoneException;
import com.ufcg.psoft.scrum_board.exception.TaskNotFoundException;
import com.ufcg.psoft.scrum_board.exception.UnauthorizedAccessException;
import com.ufcg.psoft.scrum_board.exception.UserNotFoundException;
import com.ufcg.psoft.scrum_board.exception.UserStoryNotFoundException;
import com.ufcg.psoft.scrum_board.exception.WrongTaskStateException;
import com.ufcg.psoft.scrum_board.model.Task;
import com.ufcg.psoft.scrum_board.model.User;
import com.ufcg.psoft.scrum_board.model.UserStory;
import com.ufcg.psoft.scrum_board.repository.TaskRepository;
import com.ufcg.psoft.scrum_board.repository.UserRepository;
import com.ufcg.psoft.scrum_board.repository.UserStoryRepository;
import com.ufcg.psoft.scrum_board.utils.TaskMapper;

@Service
public class TaskService {

    @Autowired
    private TaskRepository taskRep;

    @Autowired
    private UserStoryRepository userStoryRepository; 

    @Autowired
    private UserRepository userRepository;

   

    public TaskDTO addTask(NewTaskDTO newTaskDTO) throws UserStoryNotFoundException {
        UserStory userStory = userStoryRepository.findUserStoryById(newTaskDTO.getId_userStory());
        if (userStory == null) throw new UserStoryNotFoundException("The associated user story was not found!");
        Task task = TaskMapper.convertFromNewTaskDTO(newTaskDTO, userStory);
        this.taskRep.addTask(task);
        return TaskMapper.convertToTaskDTO(task);
    }


    public TaskDTO findTaskById(String id_task) throws TaskNotFoundException {
        Task task = this.taskRep.findTaskById(id_task);
        if (task == null) throw new TaskNotFoundException(task + " not found!");
        return TaskMapper.convertToTaskDTO(task);
        
    }

    public TaskDTO updateTask(UpdateTaskDTO taskDTO, String taskId) throws UserStoryNotFoundException, TaskNotFoundException {
        UserStory userStory = userStoryRepository.findUserStoryById(taskDTO.getUserStoryId());
        if (userStory == null) throw new UserStoryNotFoundException("The suggested associated user story was not found!");

        Task task = this.taskRep.findTaskById(taskId);
        if (task == null) throw new TaskNotFoundException("The task with id '" + taskId + "' was not found!");

        task.setTitle(taskDTO.getTitle());
        task.setDescription(taskDTO.getDescription());
        task.setUserStory(userStory);
        task.setDone(taskDTO.isDone());

        taskRep.editTask(task);

        return TaskMapper.convertToTaskDTO(task);
    }

    public void deleteTask(String id_task) throws TaskNotFoundException {
        if (this.taskRep.findTaskById(id_task) == null) throw new TaskNotFoundException("The task with id '" + id_task + "' was not found! Operation was not successful!");
        this.taskRep.delTask(id_task);

    }

    public List<TaskDTO> getAllTask() {
        List<TaskDTO> taskFound = taskRep.getAll()
                                    .stream()
                                    .map(t -> TaskMapper.convertToTaskDTO(t))
                                    .collect(Collectors.toList());
        return taskFound;
    }
    
    public void setRealizada(String id_Task, String idUsuario) throws TaskNotFoundException, UserNotFoundException, TaskAlreadyDoneException, UnauthorizedAccessException {
    	Task task = this.taskRep.findTaskById(id_Task);
        if (task == null) throw new TaskNotFoundException(task + " not found!");
        User user = userRepository.getUserByUsername(idUsuario);
        if (user == null) throw new UserNotFoundException("The user '"  +idUsuario + "' wasn't found!");
        if (task.isDone() == false) {
            if (task.getUserStory().getDevs().contains(user) || task.getUserStory().getProject().getScrumMaster().equals(user)) {
                task.setDone(true);
            } else {
                throw new UnauthorizedAccessException("The user '" + user.getUsername() + "' has no permission to modify this task!")
;            }
        } else {
            throw new TaskAlreadyDoneException("The task is already done!");
        }
    }

    public void setToVerify(String id_Task, String idUsuario) throws TaskNotFoundException, UserNotFoundException, TaskAlreadyDoneException, UnauthorizedAccessException, WrongTaskStateException{
        Task task = this.taskRep.findTaskById(id_Task);
        if (task == null) throw new TaskNotFoundException(task + " not found!");
        User user = userRepository.getUserByUsername(idUsuario);
        if (user == null) throw new UserNotFoundException("The user '"  +idUsuario + "' wasn't found!");
        if (task.isDone() == false) {
            if (task.getUserStory().getDevelopmentState().toString() == "Work In Progress") {
                if (task.getUserStory().getDevs().contains(user) || task.getUserStory().getProject().getScrumMaster().equals(user)) {
                    task.getUserStory().getDevelopmentState().moveToNextStage();
                }
                else {
                    throw new UnauthorizedAccessException("The user '" + user.getUsername() + "' has no permission to modify this task!");
                }
            }
            else{
                throw new WrongTaskStateException("The stage of the task could not work in this action");
            }
        }

    }

    public void setDone(String id_Task, String idUsuario) throws TaskNotFoundException, UserNotFoundException, TaskAlreadyDoneException, UnauthorizedAccessException, WrongTaskStateException{


    }
    

    
}

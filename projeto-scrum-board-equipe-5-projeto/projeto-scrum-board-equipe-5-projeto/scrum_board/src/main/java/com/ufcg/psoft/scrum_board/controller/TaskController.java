package com.ufcg.psoft.scrum_board.controller;

import com.ufcg.psoft.scrum_board.dto.NewTaskDTO;
import com.ufcg.psoft.scrum_board.dto.TaskDTO;
import com.ufcg.psoft.scrum_board.dto.UpdateTaskDTO;
import com.ufcg.psoft.scrum_board.exception.TaskNotFoundException;

import com.ufcg.psoft.scrum_board.exception.UserStoryNotFoundException;
import com.ufcg.psoft.scrum_board.service.TaskService;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.util.UriComponentsBuilder;

@RestController
@RequestMapping("/task")
@CrossOrigin
public class TaskController {

    @Autowired
    private TaskService taskService;

    @PostMapping
    public ResponseEntity<?> create(@RequestBody NewTaskDTO newTaskDTO, UriComponentsBuilder ucBuilder) {
        try{
            TaskDTO task = taskService.addTask(newTaskDTO);
            return new ResponseEntity<>(task, HttpStatus.CREATED);
        } catch(UserStoryNotFoundException e){
            return new ResponseEntity<String>(e.getMessage(), HttpStatus.BAD_REQUEST);
        }
    }

    @RequestMapping(value = "/{idTask}", method = RequestMethod.GET)
    public ResponseEntity<?> get(@RequestParam("idTask") String id_Task){
        try{
            TaskDTO task = taskService.findTaskById(id_Task);
            return new ResponseEntity<>(task, HttpStatus.OK);
        } catch (TaskNotFoundException e){
            return new ResponseEntity<String>(e.getMessage(), HttpStatus.BAD_REQUEST);
        }
    }

    @GetMapping
    public ResponseEntity<?> list() {
        List<TaskDTO> task = taskService.getAllTask();
        return new ResponseEntity<>(task, HttpStatus.OK);
    }

    @RequestMapping(value = "/{idTask}", method = RequestMethod.PUT)
    public ResponseEntity<?> edit(@RequestBody UpdateTaskDTO taskDTO, @PathVariable("idTask") String id_Task){
        try {
            TaskDTO TaskEdited = taskService.updateTask(taskDTO, id_Task);
            return new ResponseEntity<>(TaskEdited, HttpStatus.OK);
        }catch(TaskNotFoundException | UserStoryNotFoundException e){
            return new ResponseEntity<String>(e.getMessage(), HttpStatus.BAD_REQUEST);
        }
    }

    @RequestMapping(value = "/{idTask}", method = RequestMethod.DELETE)
    public ResponseEntity<?> remove(@PathVariable("idTask") String id_Task){
        try{
            taskService.deleteTask(id_Task);
            return new ResponseEntity<String>("The task was deleted successfully!", HttpStatus.OK);
        } catch (TaskNotFoundException e){
            return new ResponseEntity<String>(e.getMessage(), HttpStatus.BAD_REQUEST);
        }
    }


    

    
}

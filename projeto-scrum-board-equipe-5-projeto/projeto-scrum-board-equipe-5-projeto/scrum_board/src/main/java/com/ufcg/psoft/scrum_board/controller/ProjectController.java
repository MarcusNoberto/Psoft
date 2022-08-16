package com.ufcg.psoft.scrum_board.controller;

import com.ufcg.psoft.scrum_board.dto.AddUserToProjectDTO;
import com.ufcg.psoft.scrum_board.dto.NewProjectDTO;
import com.ufcg.psoft.scrum_board.dto.ProjectDTO;
import com.ufcg.psoft.scrum_board.exception.InappropriateRoleException;
import com.ufcg.psoft.scrum_board.exception.ProjectNotFoundException;
import com.ufcg.psoft.scrum_board.exception.UnauthorizedAccessException;
import com.ufcg.psoft.scrum_board.exception.UnavailableRoleException;
import com.ufcg.psoft.scrum_board.exception.UserNotFoundException;
import com.ufcg.psoft.scrum_board.service.ProjectService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.List;


@RestController
@RequestMapping("/project")
@CrossOrigin
public class ProjectController {

    @Autowired
    private ProjectService projectService;


    @PostMapping(value = "/{loggedUsername}")
    public ResponseEntity<?> create(@RequestBody NewProjectDTO newProjectDTO, @PathVariable("loggedUsername") String loggedUsername) {
        try {
            ProjectDTO project = projectService.addProject(newProjectDTO, loggedUsername);
            return new ResponseEntity<>(project, HttpStatus.CREATED);
        } catch (UserNotFoundException e) {
            return new ResponseEntity<String>(e.getMessage(), HttpStatus.BAD_REQUEST);
        }
    }


    @RequestMapping(value = "/{projectId}", method = RequestMethod.GET)
    public ResponseEntity<?> get(@PathVariable("projectId") String projectId) throws ProjectNotFoundException {
        try {
            ProjectDTO project = projectService.findProjectById(projectId);
            return new ResponseEntity<>(project, HttpStatus.OK);
        } catch (ProjectNotFoundException e) {
            return new ResponseEntity<String>(e.getMessage(), HttpStatus.BAD_REQUEST);
        }
    }


    @GetMapping
    public ResponseEntity<?> list() {
        List<ProjectDTO> projects = projectService.getAllProjects();
        return new ResponseEntity<>(projects, HttpStatus.OK);
    }


    @RequestMapping(value = "/{loggedUsername}", method = RequestMethod.PUT)
    public ResponseEntity<?> edit(@RequestBody ProjectDTO projectDTO, @PathVariable("loggedUsername") String loggedUsername) throws ProjectNotFoundException {
        try {
            ProjectDTO projectEdited = projectService.updateProject(loggedUsername, projectDTO);
            return new ResponseEntity<>(projectEdited, HttpStatus.OK);
        } catch (ProjectNotFoundException | UnauthorizedAccessException e) {
            return new ResponseEntity<String>(e.getMessage(), HttpStatus.BAD_REQUEST);
        }
    }

    
    @RequestMapping(value = "/{loggedUsername}/{projectId}", method = RequestMethod.DELETE)
    public ResponseEntity<?> remove(@PathVariable("loggedUsername") String loggedUsername, @PathVariable("projectId") String projectId) {
        try {
            projectService.deleteProject(projectId, loggedUsername);
            return new ResponseEntity<String>("Project successfully deleted.", HttpStatus.OK);
        } catch (ProjectNotFoundException | UnauthorizedAccessException e) {
            return new ResponseEntity<String>(e.getMessage(), HttpStatus.OK);
        }
    }


    @PatchMapping(value = "/{loggedUsername}")
    public ResponseEntity<?> addUserToProject(@PathVariable("loggedUsername") String loggedUsername, @RequestBody AddUserToProjectDTO addUserToProjectDTO) {
        try {
            ProjectDTO projectDTO = this.projectService.addUserToProject(loggedUsername, addUserToProjectDTO);
            return new ResponseEntity<>(projectDTO, HttpStatus.OK);
        } catch (ProjectNotFoundException | UnauthorizedAccessException | UserNotFoundException
                | InappropriateRoleException | UnavailableRoleException e) {
            return new ResponseEntity<>(e.getMessage(), HttpStatus.BAD_REQUEST);
        }
    }

}

package com.ufcg.psoft.scrum_board.controller;

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
import com.ufcg.psoft.scrum_board.service.UserStoryService;
import com.ufcg.psoft.scrum_board.utils.CustomResponseMessage;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.util.UriComponentsBuilder;

@RestController
@RequestMapping("/us")
@CrossOrigin
public class UserStoryController {

    @Autowired
    private UserStoryService userStoryService;


    @PostMapping("/{loggedUsername}")
    public ResponseEntity<?> create(@PathVariable("loggedUsername") String loggedUsername, @RequestBody NewUserStoryDTO newUserStoryDTO) {
        try{
            UserStoryDTO userStoryDTO = userStoryService.addUserStory(newUserStoryDTO, loggedUsername);
            return new ResponseEntity<>(userStoryDTO, HttpStatus.CREATED);
        } catch(UserStoryAlreadyExistsException | ProjectNotFoundException | UserNotFoundException | UnauthorizedAccessException e){
            return new ResponseEntity<String>(e.getMessage(), HttpStatus.BAD_REQUEST);
        }
    }


    @RequestMapping(value = "/{idUserStory}", method = RequestMethod.GET)
    public ResponseEntity<?> get(@RequestParam("idUserStory") String id_UserStory){
        try{
            UserStoryDTO userStoryDTO = userStoryService.getUserStoryById(id_UserStory);
            return new ResponseEntity<>(userStoryDTO, HttpStatus.OK);
        } catch (UserStoryNotFoundException e){
            return new ResponseEntity<String>(e.getMessage(), HttpStatus.BAD_REQUEST);
        }
    }


    @GetMapping
    public ResponseEntity<?> list() {
        List<UserStoryDTO> userStoriesDTO = userStoryService.getAllUserStories();
        return new ResponseEntity<>(userStoriesDTO, HttpStatus.OK);
    }


    @RequestMapping(value = "/{loggedUsername}", method = RequestMethod.PUT)
    public ResponseEntity<?> edit(@RequestBody UpdateUserStoryDTO updateUserStoryDTO, @PathVariable("loggedUsername") String loggedUsername){
        try{
            UserStoryDTO userStoryEdited = userStoryService.updateUserStory(updateUserStoryDTO, loggedUsername);
            return new ResponseEntity<>(userStoryEdited, HttpStatus.OK);
        }catch(UserStoryNotFoundException | UnauthorizedAccessException e){
            return new ResponseEntity<String>(e.getMessage(), HttpStatus.BAD_REQUEST);
        }
    }


    @RequestMapping(value = "/{loggedUsername}/{idUserStory}", method = RequestMethod.DELETE)
    public ResponseEntity<?> remove(@PathVariable("idUserStory") String id_UserStory, @PathVariable("loggedUsername") String loggedUsername){
        try{
            this.userStoryService.deleteUserStory(id_UserStory, loggedUsername);
            return new ResponseEntity<>("UserStory successfully deleted.", HttpStatus.OK);
        } catch (UserStoryNotFoundException | UnauthorizedAccessException e){
            return new ResponseEntity<String>(e.getMessage(), HttpStatus.BAD_REQUEST);
        }
    }


    @PatchMapping(value = "/{loggedUserName}/{userStoryId}")
    public ResponseEntity<?> addUserToUserStory(@PathVariable("loggedUsername") String loggedUsername, @PathVariable String userStoryId) {
        try {
            UserStoryDTO userStoryDTO = this.userStoryService.joinUserStory(loggedUsername, userStoryId);
            return new ResponseEntity<>(userStoryDTO, HttpStatus.OK);
        } catch (UserNotFoundException | UserStoryNotFoundException | InappropriateRoleException e) {
            return new ResponseEntity<>(e.getMessage(), HttpStatus.BAD_REQUEST);
        }
    }
  



    
    
}

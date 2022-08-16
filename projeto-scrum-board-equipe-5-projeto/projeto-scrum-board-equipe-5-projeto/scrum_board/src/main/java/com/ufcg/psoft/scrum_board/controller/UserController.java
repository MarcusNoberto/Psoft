package com.ufcg.psoft.scrum_board.controller;

import com.ufcg.psoft.scrum_board.dto.UserDTO;
import com.ufcg.psoft.scrum_board.exception.UnavailableRoleException;
import com.ufcg.psoft.scrum_board.exception.UserAlreadyExistsException;
import com.ufcg.psoft.scrum_board.exception.UserNotFoundException;
import com.ufcg.psoft.scrum_board.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/user")
@CrossOrigin
public class UserController {

    @Autowired
    private UserService userService;


    @PostMapping
    public ResponseEntity<?> create(@RequestBody UserDTO userDTO) throws UserAlreadyExistsException {
        try {
            UserDTO user = userService.addUser(userDTO);
            return new ResponseEntity<>(user, HttpStatus.CREATED);
        } catch (UserAlreadyExistsException | UnavailableRoleException e) {
            return new ResponseEntity<String>(e.getMessage(), HttpStatus.BAD_REQUEST);
        }
    }

    @GetMapping(value = "/{username}")
    public ResponseEntity<?> get(@PathVariable("username") String username) throws UserNotFoundException {
        try {
            UserDTO user = userService.findUserByUsername(username);
            return new ResponseEntity<>(user, HttpStatus.OK);
        } catch (UserNotFoundException e) {
            return new ResponseEntity<String>(e.getMessage(), HttpStatus.BAD_REQUEST);
        }
    }

    @GetMapping
    public ResponseEntity<?> list() {
        List<UserDTO> users = userService.getAllUsers();
        return new ResponseEntity<>(users, HttpStatus.OK);
    }

    @RequestMapping(value = "/{loggedUsername}", method = RequestMethod.PUT)
    public ResponseEntity<?> edit(@RequestBody UserDTO userDTO, @PathVariable("loggedUsername") String loggedUsername) throws UserNotFoundException {
        try {
            UserDTO userEdited = userService.updateUser(userDTO, loggedUsername);
            return new ResponseEntity<>(userEdited, HttpStatus.OK);
        } catch (UserNotFoundException e) {
            return new ResponseEntity<String>(e.getMessage(), HttpStatus.BAD_REQUEST);
        }
    }

    @RequestMapping(value = "/{loggedUsername}", method = RequestMethod.DELETE)
    public ResponseEntity<?> removerUser( @PathVariable("loggedUsername") String loggedUsername) throws UserNotFoundException {
        try {
            userService.deleteUser(loggedUsername);
            return new ResponseEntity<String>("user successfully deleted.", HttpStatus.OK);
        } catch (UserNotFoundException e) {
            return new ResponseEntity<String>(e.getMessage(), HttpStatus.BAD_REQUEST);
        }
    }


    @GetMapping("/roles")
    public ResponseEntity<?> getAvailableRoles() {
        return new ResponseEntity<>(this.userService.getAvailableRoles(), HttpStatus.OK);
    }
}

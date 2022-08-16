package com.ufcg.psoft.scrum_board.model;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

import com.ufcg.psoft.scrum_board.states.DevelopmentState;
import com.ufcg.psoft.scrum_board.states.ToDo;

import lombok.Getter;
import lombok.Setter;

@Getter @Setter
public class UserStory {

    private String id;
    private String title;
    private String description;
    private Project project;
    private List<User> devs;
    private DevelopmentState developmentState;

    public UserStory(String title, String description, Project project){
        this.id = UUID.randomUUID().toString();
        this.title = title;
        this.description = description;
        this.project = project;
        this.devs = new ArrayList<>();
        this.developmentState = new ToDo(this);
    }
    
    public void moveToNextStage(){
        this.developmentState.moveToNextStage();

    }

    public void addDev(User user) {
        this.devs.add(user);
    }
}
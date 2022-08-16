package com.ufcg.psoft.scrum_board.dto;

import java.util.List;

import com.ufcg.psoft.scrum_board.model.User;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class UserStoryDTO {

    private String id;
    private String title;
    private String description;
    private String projectId;
    private List<User> devs;
    private String developmentState;
    
}

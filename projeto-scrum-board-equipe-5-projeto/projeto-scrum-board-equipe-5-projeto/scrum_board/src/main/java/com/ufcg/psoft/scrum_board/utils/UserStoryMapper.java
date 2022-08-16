package com.ufcg.psoft.scrum_board.utils;

import com.ufcg.psoft.scrum_board.dto.UserStoryDTO;
import com.ufcg.psoft.scrum_board.model.UserStory;

public class UserStoryMapper {
    

    public static UserStoryDTO convertToUserStoryDTO (UserStory userStory) {
        return new UserStoryDTO(
            userStory.getId(), userStory.getTitle(), userStory.getDescription(), 
            userStory.getProject().getId(), userStory.getDevs(), 
            userStory.getDevelopmentState().toString()
        );
    }

}

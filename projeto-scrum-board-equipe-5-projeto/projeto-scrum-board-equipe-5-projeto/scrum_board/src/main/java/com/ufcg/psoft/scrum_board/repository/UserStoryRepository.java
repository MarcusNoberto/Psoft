package com.ufcg.psoft.scrum_board.repository;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

import org.springframework.stereotype.Repository;

import com.ufcg.psoft.scrum_board.model.UserStory;

@Repository
public class UserStoryRepository {
    private Map<String, UserStory> userStories;

    public UserStoryRepository(){
        this.userStories = new HashMap<String, UserStory>();
    }

    public UserStory addUserStory(UserStory userStory) {
        this.userStories.put(userStory.getId(), userStory);
        return userStory;

    }

    public UserStory findUserStoryById(String id) {
        return this.userStories.get(id);
    }

    public void editUserStory(UserStory userStory) {
        this.userStories.replace(userStory.getId(), userStory);
    }

    public void delUserStory(String id) {
        this.userStories.remove(id);
    }

    public Collection<UserStory> getAll() {
        return userStories.values();
    }
    
}

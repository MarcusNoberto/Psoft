package com.ufcg.psoft.scrum_board.repository;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

import org.springframework.stereotype.Repository;

import com.ufcg.psoft.scrum_board.model.Task;

@Repository
public class TaskRepository {
    private Map<String, Task> task;

    public TaskRepository(){
        this.task = new HashMap<String, Task>();
    }

    public Task addTask(Task task) {
        this.task.put(task.getId(), task);
        return task;

    }

    public Task findTaskById(String id) {
        return this.task.get(id);
    }

    public void editTask(Task Task) {
        this.task.replace(Task.getId(), Task);
    }

    public void delTask(String id) {
        this.task.remove(id);
    }

    public Collection<Task> getAll() {
        return task.values();
    }
    
}

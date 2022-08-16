package com.ufcg.psoft.scrum_board.model;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

import com.ufcg.psoft.scrum_board.enums.ScrumRoleEnum;

@Getter
@Setter
@AllArgsConstructor
public class Project {

    public String id;
    public String name;
    public String description;
    public String partnerInstitution;
    public User scrumMaster;
    public User productOwner;
    public List<User> developers;
    public List<User> researchers;
    public List<User> trainees;

    public Project(String name, String description, String partnerInstitution, User scrumMaster) {
        this.id = UUID.randomUUID().toString();
        this.name = name;
        this.description = description;
        this.partnerInstitution = partnerInstitution;
        this.scrumMaster = scrumMaster;
        this.productOwner = new User();
        this.developers = new ArrayList<>();
        this.researchers = new ArrayList<>();
        this.trainees = new ArrayList<>();
    }

    public void addUserToProject(User user, ScrumRoleEnum sre) {
        if (sre.equals(ScrumRoleEnum.PRODUCT_OWNER)) this.productOwner = user;
        if (sre.equals(ScrumRoleEnum.DEVELOPER)) this.developers.add(user);
        if (sre.equals(ScrumRoleEnum.RESEARCHER)) this.researchers.add(user);
        if (sre.equals(ScrumRoleEnum.TRAINEE)) this.trainees.add(user);
    }
}

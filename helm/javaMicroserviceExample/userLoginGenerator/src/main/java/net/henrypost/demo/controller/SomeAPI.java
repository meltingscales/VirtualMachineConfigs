package net.henrypost.demo.controller;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;

import org.springframework.boot.autoconfigure.security.SecurityProperties.User;
import org.springframework.http.ResponseEntity;
import org.springframework.lang.NonNull;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import net.henrypost.demo.model.UserPOJO;

@RestController
@RequestMapping(path = "/api")
public class SomeAPI {

    @GetMapping(path = "/user/getRandom")
    public ResponseEntity<List<UserPOJO>> getRandomUsers() {
        
        List<UserPOJO> users = new ArrayList<>();

        for (int i = 0; i < 10; i++) {
            users.add(UserPOJO.newRandomUser());
        }

        //this sucks, this is what Jackson serialization eliminates
        // String ret = "{";

        // ret+= "userAge: "+users.get(0).age+","

        return ResponseEntity
                .ok()
                .body(users);
    }

    @PostMapping(path = "/user/create")
    public ResponseEntity<Map<?, ?>> createNewUser(
            @RequestBody @Validated @NonNull UserPOJO user) {
        Map<String, String> data = new HashMap<String, String>();

        data.put("msg", "thx for da user age %d called %s".formatted(user.age, user.name));
        data.put("what you gave us", user.toString());

        return ResponseEntity
                .ok()
                .body(data);
    }

    @GetMapping(path = "/", produces = "application/json")
    public ResponseEntity<Map<?, ?>> index() {
        Map<String, String> data = new HashMap<String, String>();

        data.put("msg", "welcome to da index brudda");
        data.put("path", "/");

        return ResponseEntity
                .ok()
                .body(data);
    }

    @GetMapping(path = "/someRandomStuff", produces = "application/json")
    public ResponseEntity<Map<?, ?>> getSomeRandomStuff() {
        Map<String, String> data = new HashMap<String, String>();

        data.put("wowItsARandomInt", "" + new Random().nextInt(1000));

        return ResponseEntity
                .ok()
                .body(data);
    }
}

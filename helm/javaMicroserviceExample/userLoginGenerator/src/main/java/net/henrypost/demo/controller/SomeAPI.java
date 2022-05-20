package net.henrypost.demo.controller;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;

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

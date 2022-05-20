package net.henrypost.demo.controller;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;

import org.springframework.boot.SpringBootConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(path = "/api")
public class SomeAPI {

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

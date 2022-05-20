package net.henrypost.demo.controller;

import java.util.HashMap;
import java.util.Map;

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
    public ResponseEntity<Map<?,?>> index() {
        Map<String,String> data = new HashMap<String, String>();

        data.put("msg", "welcome to da index brudda");
        data.put("path", "/");

        return ResponseEntity
                .ok()
                .body(data);
    }


    @GetMapping(path = "/someresource", produces = "application/json")
    public ResponseEntity<Map<?,?>> getSomethingidk() {
        Map<String,String> data = new HashMap<String, String>();

        data.put("someparamidk", "1234");

        return ResponseEntity
                .ok()
                .body(data);
    }
}

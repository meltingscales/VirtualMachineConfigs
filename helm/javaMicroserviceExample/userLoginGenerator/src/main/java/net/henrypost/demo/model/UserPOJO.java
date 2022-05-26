package net.henrypost.demo.model;

import java.util.Arrays;
import java.util.Random;

public class UserPOJO {

    public static final String[] names = "Henry Jill Jessica David".split(" ");

    public int age;
    public String name;

    public UserPOJO() {
        this.age = 24;
        this.name = "Henry";
    }

    public UserPOJO(int age, String name) {
        this.age = age;
        this.name = name;
    }

    @Override
    public String toString() {
        return "<%s name=%s age=%d>".formatted(
                this.getClass().getSimpleName(),
                this.name,
                this.age);
    }

    public static UserPOJO newRandomUser() {
        return new UserPOJO(
                new Random().nextInt(0, 99),
                Arrays.asList(names).get(new Random().nextInt(names.length)));
    }
}

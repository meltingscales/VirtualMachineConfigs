package Classes;

public class Person extends Organism {

    public String name = "noone";
    public String house = "the ground";

    public Person(int age, String name) {
        super(age);

        this.name = name;
    }
}

public class Person extends Organism {

    /**
     * What is this Person called?
     */
    public String name;

    /**
     * Where does this Person live?
     */
    public String address;

    public Person() {
        super();
    }

    public Person(String name, String birth) {
        // Call our constructor that just takes one argument.
        super(birth);

        this.name = name;
    }

    public Person(String name, String birth, String address) {
        // Call our two-argument constructor.
        this(name, birth);

        this.address = address;
    }

    public Person(String birth) {
        super(birth); // Pass the Organism constructor our birth date-string.
    }

    @Override
    public String toString() {
        return String.format("Person #%d\nName: %s\nAddress: %s\nBirth: %s\nCalories: %d\nAlive: %s",
                this.organismNumber, this.name, this.address, this.birth.toString(), this.calories, this.isAlive().toString());
    }

}

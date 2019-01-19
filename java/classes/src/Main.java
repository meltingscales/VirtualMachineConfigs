@SuppressWarnings("Duplicates")
public class Main {

    public static void main(String[] args) throws Exception {

        // A VERY old slug. Presumably Lovecraftian.
        Organism slug = new Organism("1937-03-15");

        // It's me! I hope I don't encounter an eldritch slug.
        Person henry = new Person("Henry", "1997-01-01", "Illinois Institute of Technology");

        System.out.println("Notice that the slug's toString looks different from henry's toString.");
        System.out.println();
        System.out.println(slug);
        System.out.println();
        System.out.println(henry);
        System.out.println();
        System.out.println("Even though the Organism.eat function takes an Organism, it works on any object which EXTENDS Organism.");
        System.out.println("Because `Person henry` is an Organism (by virtue of it being a Person), it can be consumed by our slug.");

        slug.eat(henry);


        System.out.println("Now let's take a look at both Organisms again.");
        System.out.println();
        System.out.println(slug);
        System.out.println();
        System.out.println(henry);
        System.out.println();
        System.out.println("Looks like the slug gained calories, and I perished.");


    }
}

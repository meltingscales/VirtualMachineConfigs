// See https://docs.oracle.com/javase/tutorial/java/IandI/abstract.html

public class main_class
{
    public static void main(String[] args)
    {
        /***
         * This is an example of polymorphism.<br>
         * 
         * You're allowed to say that 'd1' is an Organism because Deer can do everything that Organisms can.<br>
         * 
         * I.e. a Deer IS-A Organism.
         */
        Organism d1 = new Deer();

        /***
         * HOWEVER, you are NOT allowed to do this! (hence why it is commented out!)<br>
         * 
         * The reason being that the Organism class -would- be being instantiated, and we can't do that.<br>
         * 
         * You can't instantiate an Organism, and also, and Organism is NOT a deer.
         */
        // Deer d1 = new Organism();
        
        Deer d2 = new Deer();
        
        d1.eat();
        d2.eat();
        
        Organism w1 = new Wolf(); //Again we see polymorphism in action.
        
        w1.eat(d1); //Wolf 1 eats an Organism.

    }
}

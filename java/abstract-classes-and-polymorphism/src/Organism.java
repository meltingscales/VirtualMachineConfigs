/***
 *
 * As you can see, this is somewhat different than an interface. <br>
 * 
 * Similar to interfaces, though, this class can NOT be instantiated.<br>
 * 
 * You can extend this {@link #Organism}, and if you do, you must implement ALL abstract methods.
 */
public abstract class Organism
{

    /***
     * Here we have an 'instance variable'. It can be created when a subclass of Organism is instantiated.<br>
     * 
     * This is the first major difference between abstract classes and 'interfaces'.<br>
     * 
     * 'Interfaces' can NOT be instantiated, and are NOT allowed to have ANY instance variables, nor are they allowed to have methods with implementation.
     */
    public boolean alive;

    // Below here are a bunch of abstract methods.
    // This is similar to interfaces, except the 'abstract' modifier is added.
    // Note there is no method body.
    public abstract void live();

    public abstract void die();

    public abstract void eat(Organism o);
    
    public abstract void eat();

    public abstract void move();

    // And the last main difference, a method with a body.
    // Abstract classes have methods with bodies, but can not be called directly, and must be called by making something that 'extends' or 'subclasses' an Organism.
    public void test()
    {
        System.out.println("Hi! I'm a test method!");
    }

}
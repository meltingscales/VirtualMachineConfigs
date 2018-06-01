
public class Deer extends Organism
{

    /***
     * The default constructor.<br>
     * 
     * Called when a Deer is instantiated.
     */
    public Deer()
    {
        System.out.println("Who's instantiating the deer class?!");
    }

    @Override
    public void live()
    {
        System.out.println("I am a beautiful baby " + getClass().getSimpleName() + "!");
    }

    @Override
    public void die()
    {
        System.out.println("Me, a " + getClass().getSimpleName() + ", has died!");
        alive = false;
    }

    @Override
    public void eat(Organism o)
    {
        System.out.println("I can't eat that! It's another organism!");
    }

    @Override
    public void eat()
    {
        System.out.println("Mmm, grass!");
    }

    @Override
    public void move()
    {
        System.out.println("(gracefully prances)");
    }

}


public class Wolf extends Organism
{

    @Override
    public void live()
    {
        System.out.println("I am a fierce baby " + getClass().getSimpleName() + "!");
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
        System.out.println("Mmm, a meaty "+o.getClass().getSimpleName()+" to eat!");
        o.die();
    }

    @Override
    public void eat()
    {
        System.out.println("I can't eat grass, I'm a "+getClass().getSimpleName());
    }

    @Override
    public void move()
    {
        System.out.println("(silently lurks)");
    }

}

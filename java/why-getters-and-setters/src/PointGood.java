/***
 * Adding to the example set by {@link what_do_setters_do}, this class shows how
 * if you have multiple constructors, having a setter can simplify checking by
 * essentially putting all of the checking in one place.
 */

public class PointGood
{
    private double x;
    private double y;

    public void setX(double x)
    {
        if(x < 0)
        {
            throw new IllegalArgumentException("" + x);
        }

        this.x = x;
    }

    public void setY(double y)
    {
        if(y < 0)
        {
            throw new IllegalArgumentException("" + y);
        }

        this.y = y;
    }

    // As you can see, all of our constructors have no checks to ensure that any
    // arguments are below zero.
    
    // We can do this because our setters have checks!
    public PointGood()
    {
        this.setX(0);
        this.setY(0);
    }

    public PointGood(double n)
    {
        this.setX(n);
        this.setY(n);
    }

    public PointGood(double x, double y)
    {
        this.setX(x);
        this.setY(y);
    }
}
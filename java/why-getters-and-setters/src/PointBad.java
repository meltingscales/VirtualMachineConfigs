
public class PointBad
{
    public double x;
    public double y;

    // So, there's more repetition here.
    public PointBad()
    {
        this.x = 0;
        this.y = 0;
    }

    public PointBad(double n)
    {
        if(n < 0)
        {
            throw new IllegalArgumentException("" + n);
        }

        this.x = n;
        this.y = n;
    }

    public PointBad(double x, double y)
    {
        if(x < 0)
        {
            throw new IllegalArgumentException("" + x);
        }

        this.x = x;

        if(y < 0)
        {
            throw new IllegalArgumentException("" + x);
        }

        this.y = y;
    }

}

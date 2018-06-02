
public class Item
{
    public String name = "air";
    public double unitprice = 0.0;
    public String unit = "cubic meter";

    public Item(String n, double up, String u)
    {
        this.name = n;
        this.unitprice = up;
        this.unit = u;
    }

    @Override
    public String toString()
    {
        return String.format("%s at %.2f/%s", name, unitprice, unit);
    }
}

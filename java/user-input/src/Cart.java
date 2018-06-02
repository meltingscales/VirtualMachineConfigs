import java.util.HashMap;

public class Cart
{
    HashMap<Item, Integer> items = new HashMap<>();

    public Cart()
    {

    }

    /***
     * Adds an Item to our Cart
     * 
     * @param i
     * @return How many Items of this type we've seen.
     */
    public int add(Item i)
    {
        if(!items.containsKey(i)) // if we've never seen this item before,
        {
            items.put(i, 0); // set it to zero!
        }

        items.put(i, items.get(i) + 1);

        return items.get(i);
    }

    /***
     * Remove all Items of type i from our cart.
     * 
     * @param i
     *            The item to remove.
     */
    public void remove(Item i)
    {
        if(items.containsKey(i))
        {
            items.remove(i);
        }
    }

    /***
     * Counts up number of items.
     */
    public int totalItems()
    {
        int x = 0;

        for(Integer i : items.values())
        {
            x += i;
        }

        return x;
    }

    /***
     * Counts up total cost of all items.
     */
    public double totalCost()
    {
        double c = 0;

        for(Item i : items.keySet())
        {
            c += (i.unitprice * items.get(i)); // add (items * item_cost)
        }

        return c;

    }

    @Override
    public String toString()
    {
        String s = String.format("%d items for a total of %.2f:\n", totalItems(), totalCost());

        for(Item i : items.keySet())
        {
            int amt = items.get(i); // How many items?

            s += String.format("%d %ss at %.2f\n", amt, i.name, i.unitprice * amt);
        }

        return s;

    }

}

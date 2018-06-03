import java.util.ArrayList;
import java.util.Scanner;

/***
 * This class lets the user add an arbitrary number of items to their cart.
 * 
 * It is 'better' than the {@link GroceryBad} class for several reasons, and those reason will be discussed below.
 */
public class Grocery
{
    @SuppressWarnings({ "unchecked", "serial", "rawtypes" })
    public static void main(String[] args)
    {
        Scanner s = new Scanner(System.in);// System.in is keyboard input, and we use the Scanner class to request input from it.

        // This will hold our Items.
        Cart cart = new Cart();

        // This is a list of all possible items.
        ArrayList<Item> items = new ArrayList()
        { // This list, at least the way it is constructed, is the first reason that this class
          // is 'better' than our other Grocery class.

            // If you wanted to add a new item, with its own units, price, and name,

            // in this class:
            // You simply add a new ``add(new Item("name",price,"units")) call.

            // in our 'bad' class:
            // You must construct a bunch of extra variables,
            // hard-code a case statement,
            // and...it's just not maintainable!
            {
                add(new Item("Apple", 1.00, "pound"));
                add(new Item("Cherry", 2.50, "pound"));
            }
        };

        int c = 1;
        
        System.out.println("-1 will exit.");

        while(c >= 0) // While the user does not enter a negative number,
        {
            int i = 0;
            for(Item choice : items) // Print out all possible choices.
            {
                System.out.printf("(%d): %s\n", i++, choice.toString());
            }
            System.out.print(" > ");

            // Ask them what item they would like to add.
            c = s.nextInt();

            try
            {
                // Using their number, retrieve the Item from our ArrayList.
                Item chosenItem = items.get(c);

                // Add it to the cart.
                cart.add(chosenItem);
                System.out.println("Added one " + chosenItem.name + "!");
            }
            catch(IndexOutOfBoundsException e)
            {

            }

        }

        System.out.println(cart.toString());
    }
}
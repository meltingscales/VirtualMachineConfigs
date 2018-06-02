import java.util.ArrayList;
import java.util.Scanner;

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
        {
            {
                add(new Item("Apple", 1.00, "pound"));
                add(new Item("Cherry", 2.50, "pound"));
            }
        };

        int c = 1;

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
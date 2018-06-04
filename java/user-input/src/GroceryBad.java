import java.util.Scanner;

public class GroceryBad
{
    public static void main(String[] args)
    {
        // This is what I meant in the other file:

        // If you want a new item, like bananas, you must add three new variables.

        // Not only is that inconvenient, but there is no way to easily access these values!
        int appleAmt = 0;
        int cherryAmt = 0;

        double applePrice = 1.00;
        double cherryPrice = 2.50;

        String appleUnit = "pound";
        String cherryUnit = "pound";

        System.out.println("Enter -1 to quit.");
        int i = 0;
        System.out.println(i++ + " for apples," + i++ + " for cherries.");

        int input = 1;
        Scanner s = new Scanner(System.in);

        while(input >= 0)
        {
            System.out.print(" > ");
            input = s.nextInt();

            switch(input)
            {
            case 0: // These numbers are hard-coded, too.
            {
                appleAmt++;
                break;
            }
            case 1:
            {
                cherryAmt++;
                break;
            }
            }
        }
        // As are these print statements!
        // Super hard to add stuff, huh?
        System.out.printf("%d %ss at %.2f per %s\n", appleAmt, "apples", appleAmt * applePrice, appleUnit);
        System.out.printf("%d %ss at %.2f per %s\n", cherryAmt, "cherries", cherryAmt * cherryPrice, cherryUnit);
    }
}

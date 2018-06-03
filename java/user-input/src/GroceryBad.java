import java.util.Scanner;

public class GroceryBad
{
    public static void main(String[] args)
    {
        // This is what I mean:

        // If you want a new item, like bananas, you must add three new variables.

        // Not only is that inconvenient, but there is no way to easily access
        // these values!
        int appleAmt = 0;
        int cherryAmt = 0;

        double applePrice = 1.00;
        double cherryPrice = 2.50;

        String appleUnit = "pound";
        String cherryUnit = "pound";

        int input = 1;
        Scanner s = new Scanner(System.in);

        while(input > 0)
        {
            switch(input)
            {
            case 1: //These numbers are hard-coded, too.
            {
                appleAmt++;
            }
            case 2:
            {
                cherryAmt++;
            }
            }
        }

        System.out.printf("%d %ss at %.2f",appleAmt,);
    }
}

package slots;

//@formatter:off
/*
3-digit slot machine:

- The player starts with a double cash value that the user inputs.

- Three slots, each 0-9.

- Each spin costs $2.00.

- A winning spin consists of doubles or triples on one spin.
  i.    Doubles:  Money back plus 2x the bet. (i.e. 5 - 6 - 5 )
  ii.   Triples:  Money back plus 5x the bet. (i.e. 4 - 4 - 4 )
  iii.  Singles:  A losing bet.               (i.e. 4 - 5 - 9 )

- The game ends when a player decides to either cash out or when the user has less than $2.00

- After the game ends, the final output should show how much money the user either gained or lost while playing.

- It should ask the user if they want to play again.

*/
//@formatter:on

import java.util.Random;
import java.util.Scanner;

public class slots {

    //Ask the user for their initial money to start with, and return a double.
    public static Double get_initial_money() {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter starting money:\n > ");

        Double money = scanner.nextDouble();

        return money;
    }

    // Generate a random number between 0 and 9.
    public static Integer random_slot() {
        Random random = new Random();

        Integer random_number = random.nextInt(10);

        return random_number;
    }

    // Generate all three slots randomly.
    public static Integer[] random_slots() {

        // Start with three blank slots,
        Integer[] slots = new Integer[3];

        // From zero to two,
        for (int i = 0; i < slots.length; i++) {
            // Make a random number!
            slots[i] = random_slot();
        }

        // Return our three random slots.
        return slots;
    }

    // Print out slots in a human-readable format
    public static void print_slots(Integer[] slots) {
        System.out.printf("%d - %d - %d\n", slots[0], slots[1], slots[2]);
    }

    // Given three integers, tells you if they are doubles (n - ? - n) or not.
    public static boolean is_double(Integer[] slots) {

        // If the first and last are the same,
        if (slots[0].equals(slots[2])) {
            // Return true.
            return true;
        } else { //They're not, so...
            // Return false!
            return false;
        }

    }

    // Given three integers, tells you if they are triples (n - n - n) or not.
    public static boolean is_triple(Integer[] slots) {

        // If the first and second are the same, and the second and last,
        if (slots[0].equals(slots[1]) && slots[1].equals(slots[2])) {
            // Return true.
            return true;
        } else { //They're not all equal, so...
            // Return false!
            return false;
        }

    }


    public static void main(String[] args) {

        // Set up the variable to store our slots.
        Integer[] slots = null;

        // Set up the Scanner to read input from the user.
        Scanner scanner = new Scanner(System.in);

        // Set up a string to store their response.
        String input;

        // Ask the user for their initial money.
        double money = get_initial_money();

        while (true)
        {
            // Print their money.
            System.out.printf("You have $%.2f.\n", money);

            // Ask them if they want to spin.
            System.out.print("Spin the slots for $2.00? (Y/N)\n > ");

            // Get their response.
            input = scanner.nextLine();

            if(!(input.contains("Y") || input.contains("y"))) { // If they don't enter a 'y' or 'Y',

                // They do not want to spin any more.
                System.out.println("Goodbye!");

                // Exit this while loop.
                break;
            }

            // Check if they can afford it.
            if (money >= 2.00d) {

                // Deduct $2.00 from their money.
                money -= 2.00d;

                // Spin the wheel!
                slots = random_slots();

                // Print out the result.
                print_slots(slots);

                // If all three match,
                if (is_triple(slots)) {
                    System.out.println("Congrats! A triple!");

                    // Give them their bet back.
                    money += 2.00d;

                    // Give them back 5x what they bet.
                    money += (2.00d * 5);

                } else if (is_double(slots)) { //If two match,
                    System.out.println("Congrats! A double!");

                    // Give them their bet back.
                    money += 2.00d;

                    // Give them back 2x what they bet.
                    money += (2.00d * 2);

                } else { //If none match,
                    System.out.println("Drat! No matches.");
                }

            } else { // They cannot afford it.
                System.out.println("Sorry, but you can't afford to play.");
            }
        }
    }
}

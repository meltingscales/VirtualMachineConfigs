import java.util.Arrays;

public class ForLoopsDeconstructed {

    public static void main(String[] args) {

        double[] numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

        // Let's say we want to print out each number, but divided by two.

        for (int i = 0;  // The 'initialization condition'. The expression here is evaluated one time only.
            // Generally, we would assign a number to a variable that represents our 'starting point'.
            // Because we want to print out each number in an array (1 through 10), we start at 0.

             i < numbers.length; // The 'testing condition' tells us if we should continue the for loop.
            // At the end of one iteration of the for loop, this expression is evaluated, and if it is false, we stop
            // and quit the for loop.
            //
            // The reason we use 'i < numbers.length' is so that when `i` is greater than or equal to `numbers.length`,
            // the expression is `false` and we stop looping because that means we've reached the end of the array!
            //
            // If you want the for loop to run forever, you can put 'true' here!

             i = i + 1 // This is an expression (a statement in this case) that is executed every time the for loop
            // repeats, no matter what.

            // We can replace it with `i = i + 2` if we want every 2nd number, or with `i = i - 1` if we want to go
            // backwards.
        ) {
            // I'll leave the body of the for loop blank so that below, you can see the for loop without all of these comments:
        }

        System.out.println("USING TRADITIONAL FOR LOOPS: ");

        for (int i = 0; i < numbers.length; i = i + 1) {

            System.out.println("Position " + i + ": " + numbers[i] / 2);

        }

        // Something of importance to note is:
        //
        // Anything you can achieve with for loops can absolutely be done with while loops, and vice-versa.
        //
        // I'll demonstrate this with an equivalent while loop that looks somewhat similar to the above for loop.
        System.out.println("\nUSING AN EQUIVALENT WHILE LOOP: ");

        int i = 0; // Our initializer! We can see that it really does just execute once, just like a for loop.
        while (i < numbers.length) { // This is our 'testing condition'. We stop when this is `false`.

            System.out.println("Position " + i + ": " + numbers[i] / 2);

            i = i + 1; // An expression that we evaluate at the end of the for loop!
        }

    }
}

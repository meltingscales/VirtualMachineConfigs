public class ForLoopAsWhileLoopExamples {
    public static void main(String[] args) {

        // READ ME!
        // This file is all of the for loops, but as while loops to really demonstrate how you can use while OR for
        // loops in any situation.

        int[] numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        int i;

        System.out.println("Print all numbers.");


        i = 0;
        while (i < numbers.length) {
            System.out.print(numbers[i] + " ");
            i++;
        }

        System.out.println(); //New line after numbers.


        System.out.println("Print numbers from 3 to 5.");

        // Notice how I put "i < 6", and not "i < 5". Why do you think I put this here?
        //
        // HINT: This code would still work if I put "i <= 5" instead.
        i = 3;
        while (i < 6) {
            System.out.print(numbers[i] + " ");
            i++;
        }
        System.out.println(); //New line after numbers.


        System.out.println("Print every even number.");

        i = 0;
        while (i < numbers.length) {
            System.out.print(numbers[i] + " ");
            i = i + 2;
        }
        System.out.println(); //New line after numbers.


        System.out.println("Print every odd number.");

        i = 1;
        while (i < numbers.length) {
            System.out.print(numbers[i] + " ");
            i = i + 2;
        }
        System.out.println(); //New line after numbers.


        System.out.println("Print every number, but backwards");

        // Also, note how if I want to start at the end, I can't put `i = numbers.length`! I have to say
        // `i = numbers.length - 1` because the length of numbers is 10, but its last index is 9!
        i = numbers.length - 1;
        while (i >= 0) {
            System.out.print(numbers[i] + " ");
            i--;
        }
        System.out.println(); //New line after numbers.


        System.out.println("Print every number, but backwards, and only every 2nd number.");

        i = numbers.length - 1;
        while (i >= 0) {
            System.out.print(numbers[i] + " ");
            i = i - 2;
        }
        System.out.println(); //New line after numbers.


    }
}

public class ForLoopExamples {
    public static void main(String[] args) {

        int[] numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

        System.out.println("Print all numbers.");

        for (int i = 0; i < numbers.length; i++) {
            System.out.print(numbers[i] + " ");
        }
        System.out.println(); //New line after numbers.


        System.out.println("Print numbers from 3 to 5.");

        // Notice how I put "i < 6", and not "i < 5". Why do you think I put this here?
        //
        // HINT: This code would still work if I put "i <= 5" instead.
        for (int i = 3; i < 6; i++) {
            System.out.print(numbers[i] + " ");
        }
        System.out.println(); //New line after numbers.


        System.out.println("Print every even number.");

        for (int i = 0; i < numbers.length; i = i + 2) {
            System.out.print(numbers[i] + " ");
        }
        System.out.println(); //New line after numbers.


        System.out.println("Print every odd number.");

        for (int i = 1; i < numbers.length; i = i + 2) {
            System.out.print(numbers[i] + " ");
        }
        System.out.println(); //New line after numbers.


        System.out.println("Print every number, but backwards");

        // Also, note how if I want to start at the end, I can't put `i = numbers.length`! I have to say
        // `i = numbers.length - 1` because the length of numbers is 10, but its last index is 9!
        for (int i = numbers.length - 1; i >= 0; i--) {
            System.out.print(numbers[i] + " ");
        }
        System.out.println(); //New line after numbers.


        System.out.println("Print every number, but backwards, and only every 2nd number.");

        for (int i = numbers.length - 1; i >= 0; i = i - 2) {
            System.out.print(numbers[i] + " ");
        }
        System.out.println(); //New line after numbers.


    }
}

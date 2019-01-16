import java.util.Scanner;

public class Checkout {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int quit = 0;

        while (quit == 0) {

            String storeName;
            double[] prices;
            String[] names;
            int itemsInCheckout;
            double coupon;

            System.out.print("Enter store name: ");
            storeName = scanner.next();

            System.out.println("Enter number of items to check out: ");
            itemsInCheckout = scanner.nextInt();

            while (itemsInCheckout < 0) { // If they enter a negative number for items in checkout
                System.out.println("Can't check out anti-matter! It'd explode!");
                System.out.println("Enter a non-negative number of items to check out: ");
                itemsInCheckout = scanner.nextInt();
            }

            prices = new double[itemsInCheckout]; // If user enters '3', make a three long array.
            names = new String[itemsInCheckout];

            for (int i = 0; i < itemsInCheckout; i++) { // If user entered 3 items, ask them 3 times!

                System.out.println("Enter name of item " + (i + 1) + ":");
                names[i] = scanner.next();

                System.out.println("Enter price of item " + (i + 1) + ":");
                prices[i] = scanner.nextDouble();

                while (prices[i] < 0.0d) {// If they enter a negative number for price
                    System.out.println("Can't have negative-priced items!");
                    System.out.println("Enter a positive price: ");
                    prices[i] = scanner.nextDouble();
                }

            }

            System.out.println("Enter coupon percentage (0 for no coupon, 100 for free items):");
            coupon = scanner.nextInt();

            while (coupon > 100 || coupon < 0) {
                System.out.println("Error! Coupon is either over 100 or under 0.");

                System.out.println("Enter coupon percentage (0 for no coupon, 100 for free items):");
                coupon = scanner.nextInt();
            }

            coupon = (coupon / 100d); // Turn int into double

            System.out.println("--- RECEIPT ---");
            System.out.println("--- THANK YOU FOR SHOPPING AT " + storeName + " ---");

            // Print out the per-item prices.
            double subtotal = 0;
            for (int i = 0; i < itemsInCheckout; i++) {
                System.out.println("Item #" + (i + 1) + " - " + names[i] + " - $" + prices[i]);
                subtotal += prices[i]; // Add item to subtotal.
            }

            System.out.println("Subtotal: $" + (Math.round(subtotal * 100) / 100));

            double couponSavedYou = subtotal - (subtotal * (1.00 - coupon));

            subtotal = subtotal * (1.00 - coupon); // Apply coupons.

            if (couponSavedYou > 0) {
                System.out.println("Your coupon saved you $" + (Math.round(couponSavedYou * 100) / 100) + "!");
            }

            double tax = ((subtotal * 1.08) - subtotal);

            System.out.println("Tax is $" + ((subtotal * 1.08) - subtotal) + ".");

            double total = subtotal * 1.08; // 8% sales tax.

            System.out.println("Total w/ tax: $" + total);


            System.out.println("Enter 0 to run the program again.");
            quit = scanner.nextInt();
        }
    }
}

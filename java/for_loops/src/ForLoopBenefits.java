@SuppressWarnings("ALL")
public class ForLoopBenefits {

    public static void main(String[] args) {
        // Generally, whenever you see repetition in code, or want to perform some operation multiple times,
        // a for loop can be used to eliminate that repetition.

        // I will demonstrate this below by showing some repeated piece of code, and its equivalent for loop
        // directly below it.

        // Say we want to print out "Hi! " three times.

        // We could do it like this,
        System.out.print("Hi! ");
        System.out.print("Hi! ");
        System.out.print("Hi! ");

        System.out.println(); //(This just prints a new line.)

        // Or like this.
        for (int i = 0; i < 3; i++) {
            System.out.print("Hi! ");
        }

        // It might look like we've just made it harder to read or understand by using a for loop, but think of how
        // hard it might be to print out "Hi! " 100 or 1000 times without using some sort of loop!


        // The second benefit (the first being eliminating repetition) of for loops is
        // being able to define algorithms in terms of data.

        // What do I mean by that exactly?

        // Well, say you have a list of names, like "Jack", "Sally", "Fred", "Lucy".

        String[] names = {"Jack", "Sally", "Fred", "Lucy"};

        // If you wanted to print out those names individually, without loops, you'd have to write:
        {
            System.out.println(names[0]);
            System.out.println(names[1]);
            System.out.println(names[2]);
            System.out.println(names[3]);
        }

        // That's all well and good, (and it works), but there exists a fundamental issue here.

        // If we change the SIZE of our data, `names`, to include a THIRD PERSON, then our previous
        // algorithm (four println statements) ceases to function!

        // If we rather have an algorithm that is **defined in terms of the size of the input data**,
        // we should have a way to print a list of names that works **regardless of the size of the list**!

        // To show this point, let's redefine `names` to have a fifth person.
        names = new String[]{"Jack", "Sally", "Fred", "Lucy", "Bob"};

        // To demonstrate how our old algorithm does NOT work, let's use it and note that "Bob" does not
        // get printed.
        {
            System.out.println(names[0]);
            System.out.println(names[1]);
            System.out.println(names[2]);
            System.out.println(names[3]);
        }


        // And here is a for loop that works no matter the size of the input array, which prints out all elements:
        
        for(int i = 0; i < names.length; i++) {
            
            String singleName = names[i];
            
            System.out.println(singleName);
        }
        
        // You can see that instead of going from 0 to 3, we go from 0 to `names.length`.
        // Our algorithm is defined directly in terms of properties of the data we give it!
    }
}

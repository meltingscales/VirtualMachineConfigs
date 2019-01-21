// Hello!
// In this file, I will demonstrate to you and explain features of the Java language by using code.

import java.io.Serializable;

public class JavaBasics {
/*
This is a class.

Defining a class begins with an 'access modifier' which can be either:
public,
private,
or nothing.

Now you can choose if your class is 'static' or not. If it is, you can only ever have ONE instance of your class around.

Now you choose if your class is 'abstract' or not (means it does nothing.)
Don't worry about it, as it's probably not really super useful to you at this point.

The next part is the word 'class'.

After that goes the name of the class, in our case, 'JavaBasics'.

Finally, you can choose to extend the functionality of one class, and/or implement methods described by one or many
interfaces!

Our final 'list' of potential class constructions can look like any combination of the below:

public  static              class   MyCoolThing                                                                 {};
private                     class   ThingyMaBob     extends     Throwable                                       {};
                abstract    class   UltraClass                              implements Cloneable                {};
                            class   WoopityDoo      extends     Throwable   implements Cloneable, Serializable  {};
public  static  abstract    class   IDoNothing                                                                  {};


A note on general code markup around the world: [BRACKETED] things are optional, and <ANGLE BRACED> things are required!
Things in (PARENS PARENS2 ...) with dots like that can be one or many values.)

It can be generalized as:
[ACCESS-MODIFIER] [static] [abstract] class <CLASS-NAME> [extends OTHER-CLASS-NAME] [implements (INTERFACE-NAME-1, INTERFACE-NAME-2, ...)]

You can see the shortest class definition is just `class MyCoolThing {}`, as it just needs the `class` keyword, a name,
and then an empty body.

You'll notice that this class is named the same thing as the file that contains it (JavaBasics.java).
That's just a convention in Java.
*/

    public static void main(String[] args) {
        /*
        This is a function declaration.

        Function declarations generally take this form:

        [ACCESS-MODIFIER] [static] [abstract] <RETURN-TYPE> <FUNCTION-NAME> (ARGUMENT-TYPE ARGUMENT-NAME, ARGUMENT2-TYPE ARGUMENT2-NAME ...) {}

        The way to interpret this function declaration is:


            public static void main(String[] args) {
            XXXXXX

        We've got a function that is visible to every other java file that might reside next to us.


            public static void main(String[] args) {
                   XXXXXX

        This function can only exist for a single JavaBasics class,


            public static void main(String[] args) {
                          XXXX

        When you *call* the function, meaning that you perform all of the operations that the function describes
        (which is printing "Hello, World!"), this is what the function call will be evaluated to (replaced with).
        
        `void` means we return nothing, compared to a number or list of items.


            public static void main(String[] args) {
                               XXXX

        The function is called 'main'.


            public static void main(String[] args) {
                                   XXXXXXXXXXXXXXX

        The function accepts a list of String objects as its single argument, which is named `args`.
         */


        System.out.println("Hello World!");
        /*
        This line is somewhat self-explanatory, but I'll type stuff here anyways.

        Here we're passing what appears to be a piece of text as an *argument* to the `System.out.println` function.

        As an aside, and an excuse to describe a few of Java's built-in types, let's talk about what `System.out` can
        print!

        The `System.out` object, and by extension, all PrintStream objects, have quite a large amount of
        flexible `print` functions (printf, print, println) that can take the following types, to name a few:

        TYPE    EXAMPLE     DESC
        char    'x'         A single character.
        int     20          A whole number.
        long    99999999L   A large whole number.
        byte    (byte)255   A small whole number. (between 0 and 255)
        float   20.34f      A floating-point number, aka a fraction.
        double  20.34d      A 'doubly-precise' floating-point number.
        String  "asdfd"     A piece of text, like "beesechurger" or "nunget".

         */

        int x = 20; //TODO explain statements vs expressions :::DDD
    }
}

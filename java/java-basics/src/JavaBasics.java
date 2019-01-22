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
*/
// @formatter:off
    public  static              class   MyCoolThing                                                                 {};
    private                     class   ThingyMaBob     extends     Throwable                                       {};
                    abstract    class   UltraClass                              implements Cloneable                {};
                                class   WoopityDoo      extends     Throwable   implements Cloneable, Serializable  {};
    public  static  abstract    class   IDoNothing                                                                  {};
// @formatter:on


/*
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
        byte    (byte)255   A small whole number. (between 0 and 255) We use the (byte) in parens here because there' no "literal" form of a byte, only typecasting or autoboxing can give you a primitive byte.
        float   20.34f      A floating-point number, aka a fraction.
        double  20.34d      A 'doubly-precise' floating-point number.
        String  "asdfd"     A piece of text, like "beesechurger" or "nunget".

         */


        int x;
        /*
        This is a *declaration* of x. Right now, x holds a special value called `null` in Java.

        I use this to simplify my below explanation of a *statement*.

        I could use `int x = 20;` to save space, but I wanted to keep it simple and avoid explaining this below, so I
        moved it here.
         */

        x = 20;
        /*
        Here we have a little piece of code that does something that is one of the most fundamental concepts you will
        learn in imperative programming languages:

        The assignment of a value to a variable, or a little piece of data that can mutate and change throughout your program.

        This can be likened to the concept of variables in algebra.

        This specific piece of *syntax* is a special thing in some languages, and it is called a STATEMENT.

        Below is the general form of a statement.

        <VARIABLE-NAME> = <EXPRESSION>.

        It's as simple as that.

        The part here that allows for complex-looking statements is the definition of an expression, which I will cover next.
         */


        System.out.println(
                ((x * 20) / (2 + 1))
        );
        /*
        The next concept to learn is the idea of an *expression*, which is defined as:

        "Any valid unit of code that results in a single value".

        The act of reducing an expression to a single value is called "evaluating".

        You do this when calculating mathematical expressions, like ((20 * 20) / (2 + 1)).

        Here is an example of evaluating a Java expression ((20 * 20) / (2 + 1)) by hand:

        First, you find a sub-expression with ATOMIC values (indivisible) like (20 * 20) and calculate its value, 400.

        Then, you replace that sub-expression you just calculated with the value you got:

        (400 / (2 + 1))

        Now we rinse and repeat with all of the other expressions that are just in terms of operations upon atomic
        expressions (i.e. (1))

        (2 + 1) = 3

        Replacing (2 + 1) with 3 in (400 / (2 + 1)) gives us (400 / 3).

        Now, our last expression get evaluated as 133, since we round down for the Java `int`.

        You'll also notice how I put ((x * 20) / (2 + 1)). That `x` there gets replaced with the value of `x` that we
        assigned in an earlier statement! This is how variables (x) get *evaluated*.

        Java evaluation has well-defined rules, and if you don't feel like reading up on it, there are some
        generalizations we can make about the rules:

        1. Left-to-right.
        2. PEMDAS, or Parentheses, Exponentiation, Multiplication/Division, Addition, Subtraction.

        See https://introcs.cs.princeton.edu/java/11precedence/ for more info.
         */
    }
}

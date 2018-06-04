// I have always wondered why we have getters and setters.

// If you can modify an object's variable, i.e. 'Obj.x = 3.4', directly,
// Why the hell should we make an extra function to do it for us?

// Just for completion, below is a class WITHOUT a setter.

final class Thing
{
    public Thing thing;
}

// It doesn't help that most setters look like this:

final class Thing2
{
    private Thing2 thing;

    public void setThing(Thing2 t)
    {
        this.thing = t; // Why not just make 'thing' public?!?!
    }
}

// And...that's it. Why use it?

// If you want to strictly control exactly how your object's
// instance variables are modified, then that's when you'd use it.

// For example, with the 'thing' class I made above, suppose you
// have created a new Exception that you wish to throw if someone
// passes in a Thing that is actually `null`?

// The easiest way this can be ensured is just to force yourself to
// use a `setThing(...)` method that checks if the passed argument
// is null, and throws that exception.

// Example of this 'checking' for not null.
// Note: you can check if things are positive, negative, zero, etc.
// Whatever you might want to do to prevent an object being created
// with data you don't want it to have is totally possible.

/***
 * Thrown when someone passes you something that is totally wack.
 */
final class WackParameterException extends Exception // Our own special Exception class to throw.
{
    public WackParameterException(String s)
    {
        super(s);
    }
}

final class Thing3
{
    private Thing3 thing;

    public void setThing(Thing3 t) throws WackParameterException
    {
        if(t == null) // So, every time this is used, we do this check.
        {
            throw new WackParameterException("That thing was null! That is WACK!");
        }

        this.thing = t;
    }

}

public class what_do_setters_do
{
    public static void main(String[] args) throws WackParameterException
    {
        // So, let's see if we can protect ourselves against our 'thing' variable being
        // set to null.

        Thing thing1 = new Thing();
        thing1.thing = null; // I think you can guess that no Exception is thrown.

        Thing3 thing2 = new Thing3();
        thing2.setThing(null); // So, this will error, which is what we want.

    }
}

# Preamble

This demonstration intentionally forgoes an IDE (integrated development
environment) in order to teach you how all IDEs work under the hood.

You don't necessarily need to know this, but if IDE issues happen, knowing this
can help you make sense of causes of errors or error messages themselves.

# Installing a Java Development Kit (JDK) 

This lets you *compile* human-readable source code into a machine-executable format.

This will allow you to run commands like `javac my_cool_program.java` to produce
`my_cool_program.class`. `javac` meaning "Java Compiler".

See [this
link](https://www.oracle.com/technetwork/java/javase/downloads/index.html) for
the download of the latest Java Standard Edition JDK.

# Setting up your "environment variables".

These are useful paths to folders and programs that, when using a terminal or
command line (bash or cmd.exe), make your life easier by eliminating the need to
type the full path to a program.

For example, without setting up your environment variables, you'd need to type
this to compile my example program called "hello_world.java":

`C:\Program Files\Java\jdk-9.0.1\bin\javac.exe hello_world.java`

In contrast to this, below is what you'd need to type with the Windows PATH
environment variable having `C:\Program Files\Java\jdk-9.0.1\bin\` inside of it:

`javac hello_world.java`

As others have done it better than me (and I don't want to reinvent the wheel),
[here is a tutorial](https://stackoverflow.com/a/42897591/4262535) on how to set your PATH variable to include your Java
Development Kit's folder.

Make sure to look at the `B. Permanent` section in their tutorial.

## Troubleshooting

To check if it works (for Windows), run `where java` and `where javac`. It's
`which` for *nix.

If you get back a file path, you're good.

If you get `INFO: Could not find files for the given pattern(s).`, you haven't
set up the PATH correctly. Use Google (or ask me if I'm available).

By the way, when you modify the PATH environment variable, the change only
applies to NEW command-line windows. You may need to restart your computer or
restart `cmd.exe`.

# Writing a simple program.

This can be done using notepad, notepad++, Atom, or most other __simple__ text
editors.

MS Word and WordPad are not recommended, as they can insert extra crud into our
source code that makes it invalid code.

Because this isn't an interactive tutorial, just copy and paste the below code
into your editor and save it somewhere.

    public class hello_world {
    
      public static void main(String[] args) {
      
        System.out.println("Hello world!");
      
      }
      
    }
    
This is important: **Save the file as `hello_world.java`.** or it will not
compile.

This is just because Java imposes a restriction on filenames that relates to
class names.

If you don't feel like creating the file, there exists one in this directory
under the same name.

# Compiling your program

Compiling is the act of turning source code (seen above) into code that a
computer, tool, or other apparatus knows how to execute.

In Java's case, it runs a virtual machine (called the Java Virtual Machine or
JVM) that executes very simple instructions called "bytecode".

To compile a single file (let's use our `hello_world.java`), in terminal, you
type `javac hello_world.java` and you'll see that...absolutely nothing
happens. This means it worked!

If you examine the folder that the source code is in, you'll see a `hello_world.class` file! That's the compiled source code!

To execute it, type `java hello_world` and you should see a message.

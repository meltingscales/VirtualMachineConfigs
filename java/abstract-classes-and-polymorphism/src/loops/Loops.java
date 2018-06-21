package loops;

public class Loops
{

    public static void main(String[] args)
    {

        System.out.println("..........");

        int x = 5;

        while(x > 0)
        {
            x = x - 1;
            System.out.print('.');
        }

        int z = 5;

        for(; z > 0;)
        {
            z = z - 1;
            System.out.println('.');
        }

        for(int y = 0; y > 0; y = y - 1)
        {
            System.out.println('.');

        }

    }

}

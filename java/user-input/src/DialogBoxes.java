import javax.swing.JOptionPane;

public class DialogBoxes
{
    public static void main(String[] args)
    {
        int a = Integer.parseInt(JOptionPane.showInputDialog("Enter number"));
        
        System.out.println(a);
    }
}

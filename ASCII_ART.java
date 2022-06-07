import java.awt.*;
import java.awt.image.BufferedImage;

public class AsciiArt {
    public static void main(String[] args) {
        int width = 150;
        int height = 30;

        //määrame sõna suuruse
        BufferedImage image = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
        Graphics g = image.getGraphics();
        g.setFont(new Font("SansSerif", Font.BOLD, 24));

        //Määrame kirjutatava sõna
        Graphics2D g2 = (Graphics2D) g;
        g2.setRenderingHint(RenderingHints.KEY_TEXT_ANTIALIASING, RenderingHints.VALUE_TEXT_ANTIALIAS_ON);
        g2.drawString("Mariann", 10, 20);

        for (int y = 0; y < height; y++) {
            StringBuilder builder = new StringBuilder();

            for (int x = 0; x < width; x++) {
                builder.append(image.getRGB(x, y) == -16777216 ? " " : "@");
            }
            System.out.println(builder);
        }

        //Kalmaari Kalmer
        System.out.println(" _____");
        System.out.println("( , , )  ");
        System.out.println("(  O  )  ");
        System.out.println("   -  ");
        System.out.println(" \\/|\\/    ");
        System.out.println("   |   ");
        System.out.println(" // \\\\    ");

        //kuningas
        System.out.println("            +");
        System.out.println("            _");
        System.out.println(" __ __ __  ___ __ __ __ ");
        System.out.println("(-.(-.(-. (o.o) .-).-).-)");
        System.out.println(" -| -| -|  +|+  |- |- |-");
        System.out.println(" / \\/ \\/ \\ / \\ / \\/ \\/ \\ \n");

        //Kassipere
        System.out.println("|\\---/|       /\\_/\\");
        System.out.println("| o_o |      ( o.o )");
        System.out.println(" \\_^_/        > ^ < ");
    }
}

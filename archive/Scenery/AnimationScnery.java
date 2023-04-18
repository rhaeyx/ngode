
package Scenery;

import java.awt.*;
import javax.swing.*;
import java.awt.event.*;

public class AnimationScnery extends JComponent implements ActionListener {

  private int bastonx = 0;
  private int z = 0;
  private int ax = 0;
  private int ay = 180;
  private int az = 90;
  private int aw = 270;
  // private int size=15;

  public static void main(String[] args) {
    AnimationScnery game = new AnimationScnery();
    JFrame win = new JFrame("Maze Game");
    win.add(game);
    win.setSize(800, 600);
    win.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    win.setLocationRelativeTo(null);
    win.setVisible(true);
    Timer t = new Timer(10, game);
    t.start();

  }

  public void paintComponent(Graphics g) {
    g.setColor(new Color(0, 0, 200));
    g.fillRect(0, 0, 800, 600);
    g.setColor(Color.gray);
    g.fillRect(300, 10, 150, 150);
    g.setColor(Color.red);
    g.fillArc(300, 10, 150, 150, 0, 360);
    g.setColor(Color.YELLOW);
    g.fillArc(300, 10, 150, 150, ax, 45);
    g.setColor(Color.YELLOW);
    g.fillArc(300, 10, 150, 150, ay, 45);
    g.fillArc(300, 10, 150, 150, az, 45);
    g.fillArc(300, 10, 150, 150, aw, 45);
    g.setColor(Color.red);
    g.fillRect(bastonx, 210, 150, 15);
    if (bastonx > 100 && bastonx < 400) {
      g.fillRect(295, 470, 90, 50);
      g.setColor(Color.yellow);
      Font font = new Font("Courier", Font.BOLD, 40);
      g.setFont(font);
      g.drawString("Hi!!", 300, 500);
    }

  }

  public void actionPerformed(ActionEvent e) {
    System.out.println(e.getActionCommand());

    if (bastonx == 650)
      z = 1;
    if (bastonx == 5)
      z = 0;
    if (bastonx == 0) {
      bastonx = bastonx + 800;
    }

    else {
      bastonx = bastonx - 10;
    }

    ax = ax + 5;
    ay = ay + 5;
    az = az + 5;
    aw = aw + 5;
    repaint();
  }
}
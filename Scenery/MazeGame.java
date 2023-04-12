package Scenery;

import java.awt.*;
import javax.swing.*;
import java.awt.event.*;

public class MazeGame extends JComponent implements ActionListener {

  // player position
  private static int x = 300;
  private static int y = 300;

  // settings
  private static int step = 20;
  private static int playerSize = 50;

  // window size
  private static int width = 600;
  private static int height = 600;

  public static void main(String[] args) {
    MazeGame game = new MazeGame();
    JFrame win = new JFrame("Moving Objects");
    win.add(game);
    win.addKeyListener(new KeyAdapter() {
      public void keyPressed(KeyEvent e) {
        // wasd keys
        switch (e.getKeyChar()) {
          case 'w':
          case 'a':
          case 's':
          case 'd':
            move(e.getKeyChar());
            break;
          default:
            break;
        }

        // arrow keys
        int keyCode = e.getKeyCode();
        switch (keyCode) {
          case KeyEvent.VK_UP:
          case KeyEvent.VK_LEFT:
          case KeyEvent.VK_DOWN:
          case KeyEvent.VK_RIGHT:
            move(e.getKeyChar());
            break;
          default:
            break;
        }
      }
    });

    win.setSize(width, height);
    width = win.getWidth();
    height = win.getHeight() - 100;

    System.out.println(width);
    System.out.println(height);
    win.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    win.setLocationRelativeTo(null);
    win.setVisible(true);

    Timer t = new Timer(10, game);
    t.start();

  }

  public void paintComponent(Graphics g) {
    // info
    // border
    g.setColor(new Color(114, 134, 211));
    g.fillRect(0, 0, width, height);
    g.setColor(Color.blue);
    g.fillOval(x, y, playerSize, playerSize);
  }

  public void actionPerformed(ActionEvent e) {
    repaint();
  }

  public static void move(char c) {
    System.out.println(x);
    System.out.println(y);
    switch (c) {
      case 'w':
        if (y - step > 0)
          y -= step;
        break;
      case 'a':
        if (x - step > 0)
          x -= step;
        break;
      case 's':
        if (y + playerSize + step < height)
          y += step;
        break;
      case 'd':
        if (x + playerSize + step < width)
          x += step;
        break;
      default:
        break;
    }
  }

  public static void move(int c) {
    switch (c) {
      case KeyEvent.VK_UP:
        y -= step;
        break;
      case KeyEvent.VK_LEFT:
        x -= step;
        break;
      case KeyEvent.VK_DOWN:
        y += step;
        break;
      case KeyEvent.VK_RIGHT:
        x += step;
        break;
      default:
        break;

    }
  }

}
package Scenery;

import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.util.Random;

public class Maze extends JPanel implements ActionListener {

  // player position
  // private static int x = 280;
  // private static int y = 520;
  private static int x = 300;
  private static int y = 300;

  // settings
  private static int step = 10;
  private static int playerSize = 50;

  // window size
  private static int frameWidth = 600;
  private static int frameHeight = 600;

  // game variables
  private static int level = 2;
  private static boolean[] blocked = new boolean[3];

  private static int[] xs = new int[30];
  private static int[] ys = new int[30];

  public static void main(String[] args) {

    JFrame frame = new JFrame();
    frame.setTitle("Maze Game: Reach the Treasure Room");
    frame.setLayout(new BorderLayout());
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.addKeyListener(new KeyAdapter() {
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

    Maze maze = new Maze();
    maze.setPreferredSize(new Dimension(frameWidth, frameHeight));

    frame.add(maze, BorderLayout.CENTER);

    frame.setLocationRelativeTo(null);
    frame.pack();
    frame.setVisible(true);

    Random random = new Random();

    for (int i = 0; i < 30; i++) {
      int tempx = random.nextInt(600 - 0 + 1);
      int tempy = random.nextInt(600 - 0 + 1);
      xs[i] = tempx;
      ys[i] = tempy;
    }

    Timer t = new Timer(50, maze);
    t.start();

  }

  public void map1(Graphics g) {
    // background
    g.setColor(new Color(165, 215, 232));
    g.fillRect(0, 0, frameWidth, frameHeight);

    // blocks
    g.setColor(Color.BLACK);
    g.fillRect(0, 0, 300, 100); // top left
    g.fillRect(400, 0, 200, 100); // top right
    g.fillRect(0, 300, 200, 300); // bottom left
    g.fillRect(400, 400, 200, 200); // bottom right

    g.setColor(Color.RED);
    if (blocked[0]) {
      g.fillRect(300, 0, 100, 30);
    }

    if (blocked[1]) {
      g.fillRect(frameWidth - 20, 100, 20, 300);
    }

    g.setColor(Color.YELLOW);
    g.fillRect(200, frameHeight - 20, 200, 20);

    // player
    g.setColor(Color.BLUE);
    g.fillOval(x, y, playerSize, playerSize);
  }

  public void map2(Graphics g) {
    // background
    g.setColor(new Color(87, 108, 188));
    g.fillRect(0, 0, frameWidth, frameHeight);

    // blocks
    g.setColor(Color.BLACK);
    g.fillRect(0, 0, 100, 350); // top left
    g.fillRect(200, 0, 400, 100); // top right
    g.fillRect(0, 500, 200, 100); // bottom left
    g.fillRect(400, 300, 200, 300); // bottom right

    g.setColor(Color.RED);
    if (blocked[0]) {
      g.fillRect(200, 580, 200, 20);
    }

    if (blocked[1]) {
      g.fillRect(0, 350, 20, 150);
    }

    g.setColor(Color.YELLOW);
    g.fillRect(frameWidth - 20, 100, 20, 200);

    // player
    g.setColor(Color.blue);
    g.fillOval(x, y, playerSize, playerSize);
  }

  public void map3(Graphics g) {
    // background
    g.setColor(new Color(25, 55, 109));
    g.fillRect(0, 0, frameWidth, frameHeight);

    // blocks
    g.setColor(Color.BLACK);
    g.fillRect(0, 0, 200, 100); // top left
    g.fillRect(400, 0, 200, 300); // top right
    g.fillRect(0, 250, 100, 350); // bottom left
    g.fillRect(200, 500, 400, 100); // bottom right

    g.setColor(Color.RED);
    if (blocked[0]) {
      g.fillRect(200, 0, 200, 20);
    }

    if (blocked[1]) {
      g.fillRect(0, 100, 20, 150);
    }

    g.setColor(Color.YELLOW);
    g.fillRect(100, frameHeight - 20, 100, 20);

    // player
    g.setColor(Color.blue);
    g.fillOval(x, y, playerSize, playerSize);
  }

  public void map4(Graphics g) {
    // background
    g.setColor(Color.WHITE);
    g.fillRect(0, 0, frameWidth, frameHeight);

    // coins
    for (int i = 0; i < 30; i++) {
      g.setColor(Color.YELLOW);
      g.fillOval(xs[i], ys[i], 25, 25);
      g.setColor(Color.BLACK);
      g.drawOval(xs[i], ys[i], 25, 25);

      if (ys[i] > 600) {
        ys[i] = -20;
      } else {
        ys[i] += 5;
      }
    }

    // player
    g.setColor(Color.blue);
    g.fillOval(x, y, playerSize, playerSize);
  }

  public void paintComponent(Graphics g) {
    if (level == 0)
      map1(g);
    else if (level == 1)
      map2(g);
    else if (level == 2)
      map3(g);
    else if (level == 3)
      map4(g);

  }

  public void actionPerformed(ActionEvent e) {
    repaint();
  }

  public static boolean checkGame(int testx, int testy) {
    if (level == 0) {
      return checkMap1(testx, testy);
    } else if (level == 1) {
      return checkMap2(testx, testy);
    } else if (level == 2) {
      return checkMap3(testx, testy);
    }
    return true;
  }

  public static boolean checkMap1(int testx, int testy) {
    // top
    if (testy - step < 90) { // block y
      if ((testx >= 300 && testx <= 350)) { // block x
        if (testy - step < 20) { // red block
          blocked[0] = true;
          return false;
        }
        return true;
      }
      return false;
    }

    // right
    if (testx + playerSize + step > 400) { // block x
      if ((testy >= 100 && testy <= 350)) { // block y
        if (testx + playerSize + step > frameWidth - 10) { // red block
          blocked[1] = true;
          return false;
        }
        return true;
      }
      return false;
    }

    // left
    if (testx - step < 200) { // block x
      if ((testy >= 100 && testy <= 250)) { // block y
        if (testx == 0) { // proceed
          System.out.println("Next level.");
          level = 1;
        }
        return true;
      }
      return false;
    }
    return true;
  }

  public static boolean checkMap2(int testx, int testy) {
    // top right
    if ((testy - step < 90) && (testx + step > 160)) { // block y
      return false;
    }

    // top left
    if ((testy - step < 340) && (testx - step < 90)) { // block y
      return false;
    }

    // bottom left
    if ((testy + step > 460) && (testx - step < 190)) { // block y
      return false;
    }

    // bottom right
    if ((testy + step > 260) && (testx + step > 360)) { // block y
      return false;
    }

    // bottom block
    if ((testy + step == 550)) {
      blocked[0] = true;
      return false;
    }
    // left block
    if ((testx - step == 0)) {
      blocked[1] = true;
      return false;
    }

    if (testy - step == 0) {
      level = 2;
      blocked = new boolean[3];
    }

    return true;
  }

  public static boolean checkMap3(int testx, int testy) {
    // top right
    if ((testy - step < 290) && (testx + step > 360)) { // block y
      return false;
    }

    // top left
    if ((testy - step < 90) && (testx - step < 190)) { // block y
      return false;
    }

    // bottom left
    if ((testy + step > 210) && (testx - step < 90)) { // block y
      return false;
    }

    // bottom right
    if ((testy + step > 460) && (testx + step > 160)) { // block y
      return false;
    }

    // top block
    if ((testy - step == 0)) {
      blocked[0] = true;
      return false;
    }

    // left block
    if ((testx - step == 0)) {
      blocked[1] = true;
      return false;
    }

    if (testx + playerSize + step == frameWidth) {
      System.out.println("asdf");
      level = 3;
      blocked = new boolean[3];
    }

    return true;
  }

  public static void move(char c) {
    System.out.print("X: ");
    System.out.print(x);
    System.out.print("Y: ");
    System.out.println(y);

    int testx = x;
    int testy = y;
    switch (c) {
      case 'w':
        if (testy - step >= 0)
          testy -= step;
        break;
      case 'a':
        if (testx - step >= 0)
          testx -= step;
        break;
      case 's':
        if (testy + playerSize + step <= frameHeight)
          testy += step;
        break;
      case 'd':
        if (testx + playerSize + step <= frameWidth)
          testx += step;
        break;
      default:
        break;
    }
    int prevLevel = level;
    boolean allow = checkGame(testx, testy);
    int newLevel = level;
    if (allow) {
      if (prevLevel != newLevel) {
        if (newLevel == 1) {
          x = frameWidth - playerSize;
          blocked = new boolean[3];
        } else if (newLevel == 2) {
          y = frameHeight - playerSize;
        }

      } else {
        x = testx;
        y = testy;
      }
    }
  }

}

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */
package assignment.pkg1;

/**
 *
 * @author jkdyap
 */
public class Fights {

  // create deadPool object and set his accuracy to 1/3
  Combatant deadpool = new Combatant("Deadpool", 1.0 / 3.0);

  // create kingKong object and set his accuracy to 50%
  Combatant kingkong = new Combatant("Kingkong", 1.0 / 2.0);

  // create spiderman object and set his accuracy to 100%
  Combatant spiderman = new Combatant("Spiderman", 1.0);

  // fields to store the number of wins for each combatant, initialized to zeroes
  int deadpoolWins = 0;
  int kingkongWins = 0;
  int spidermanWins = 0;

  // total fights = the total number of fights to simulate
  int totalFights = 10;

  /**
   * Resets the number of wins of each combatant object
   */
  public void resetStats() {
    this.deadpoolWins = 0;
    this.kingkongWins = 0;
    this.spidermanWins = 0;
  }

  /**
   * Displays the number of wins of each combatant and equivalent percentage
   */
  public void displayStats() {
    System.out.println("Deadpool won " + Integer.toString(deadpoolWins) + " / 10,000 fights or "
        + Double.toString(((double) deadpoolWins / 10000) * 100) + "%");
    System.out.println("Kingkong won " + Integer.toString(kingkongWins) + " / 10,000 fights or "
        + Double.toString(((double) kingkongWins / 10000) * 100) + "%");
    System.out.println("Spiderman won " + Integer.toString(spidermanWins) + " / 10,000 fights or "
        + Double.toString(((double) spidermanWins / 10000) * 100) + "%");
  }

  public void singleFight(int strategy) {
    // start with all combatants alive

    // set all combatants alive
    deadpool.setIsAlive(true);
    kingkong.setIsAlive(true);
    spiderman.setIsAlive(true);

    // this will bet set to true if only one combatant is alive
    boolean oneManLeft = false;
    int roundNumber = 0; // this will be set to 1 to totalFights

    do {
      roundNumber++;
      Combatant target = spiderman;

      /* Deadpool first to shoot */
      // check who is alive and most accurate, ascending order
      if (kingkong.isAlive()) {
        target = kingkong;
      }

      if (spiderman.isAlive()) {
        target = spiderman;
      }

      // if its not the first round or the first strategy is used and deadpool is
      // alive
      if ((strategy == 1 || roundNumber > 1) && deadpool.isAlive()) {
        // strategy 1: shoot the most accurate person alive
        deadpool.shootAtTarget(target);
      } else if (strategy == 2 && roundNumber == 1) {
        // Deadpool will do nothing on 1st round if 2nd strategy is used
        // that is, intentionally miss
      }

      /* Kingkong second to shoot */
      // check who is alive and most accurate, ascending order
      if (deadpool.isAlive()) {
        target = deadpool;
      }

      if (spiderman.isAlive()) {
        target = spiderman;
      }

      // if kingkong is alive then he shoots
      if (kingkong.isAlive()) {
        /* Kingkong second to shoot */
        kingkong.shootAtTarget(target);
      }

      /* Spiderman last to shoot */
      // check who is alive and most accurate, ascending order
      if (deadpool.isAlive()) {
        target = deadpool;
      }

      if (kingkong.isAlive()) {
        target = kingkong;
      }

      // if spiderman is alive then he shoots
      if (spiderman.isAlive()) {
        spiderman.shootAtTarget(target);
      }

      // check if only one combatant is left
      oneManLeft = ((deadpool.isAlive() ^ kingkong.isAlive() ^ spiderman.isAlive())
          ^ (deadpool.isAlive() && kingkong.isAlive() && spiderman.isAlive()));
    } while (!oneManLeft); // loop will terminate if only one combatant is left

    if (deadpool.isAlive()) { // Deadpool wins
      deadpoolWins++;
      System.out.println(deadpool.getFighterName() + " wins."); // for visual check; commented in the final version
    } else if (kingkong.isAlive()) { // Kingkong wins
      kingkongWins++;
      System.out.println(kingkong.getFighterName() + " wins."); // for visual check; commented in the final version
    } else { // Spiderman wins
      spidermanWins++;
      System.out.println(spiderman.getFighterName() + " wins."); // for visual check; commented in the final version
    }
  }

  /**
   * fights() method simulates the number of fights determined by the field
   * totalFights it keeps track of the number of wins for each combatant and
   * displays the results by calling the displayStats() method
   *
   * @param strategy = 1 for 1st strategy and 2 for 2nd strategy
   *
   */
  public void fights(int strategy) {
    resetStats();
    for (int i = 1; i <= totalFights; i++) {
      singleFight(strategy);
    }
    displayStats();
  }

}

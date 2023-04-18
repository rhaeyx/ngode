/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */
package assignment.pkg1;

/**
 * Combatant class as prescribed by the instructions in the assignment
 * Encapsulates the required fields and methods for a combatant Setters and
 * getters are required as the fields are declared as private The significant
 * methods are shootAtTarget() and killed()
 *
 * 
 *
 */
public class Combatant {

  /* Class Fields */
  // fighter's name
  private String fighterName;
  // indicates whether fighter is alive or dead
  // initialize to true. i.e. fighter is alive upon
  private boolean alive = true;
  // indicates the shooting accuracy of the fighter
  // should be set at run time
  private double accuracy;

  /**
   * ****** SETTERS AND GETTERS ***************
   */
  /**
   *
   * @param fighterName = the value of this parameter is copied to the
   *                    fighterName field
   */
  public void setFighterName(String fighterName) {
    this.fighterName = fighterName;
  }

  /**
   *
   * @param alive = the value of this parameter is copied to the alive field
   */
  public void setIsAlive(boolean alive) {
    this.alive = alive;
  }

  /**
   *
   * @param accuracy = the value of this parameter is copied to the accuracy
   *                 field
   */
  public void setAccuracy(double accuracy) {
    this.accuracy = accuracy;
  }

  /**
   *
   * @return = the value of fighterName field
   */
  public String getFighterName() {
    return fighterName;
  }

  /**
   *
   * @return = the value of alive field
   */
  public boolean isAlive() {
    return alive;
  }

  /**
   *
   * @return = the value of accuracy field
   */
  public double getAccuracy() {
    return accuracy;
  }

  /**
   * ****** END OF SETTERS AND GETTERS ***************
   */
  /**
   * killed method called when a combatant is hit thereby setting the alive
   * field to false
   */
  public void killed() {
    this.setIsAlive(false);
  }

  /**
   *
   * @param fighterName = The initial fighters name
   * @param accuracy    = The initial accuracy Constructor for Combatant that
   *                    allows setting the name and accuracy upon object creation
   */
  public Combatant(String fighterName, double accuracy) {
    this.fighterName = fighterName;
    this.accuracy = accuracy;
  }

  /**
   *
   * @param target - of type Combatant too; The combatant will try to shoot
   *               this other combatant simulates a combatant shooting another
   *               combatant
   */
  public void shootAtTarget(Combatant target) {
    System.out.print(this.fighterName + " shoots " + target.getFighterName()); // for visual viewing of the simulation;
                                                                               // commented in the final version

    // Math.random() will return a random number between 0 and 1
    // if the accuracy is set to 1 then the condition will always be true
    // which corresponds to a 100% accuracy
    // if true (i.e. the random number is within the accuracy rate of the
    // combatant) then combantant will hit target
    if (Math.random() <= this.accuracy) { // within accuracy range
      target.killed();
      System.out.println(" - " + target.getFighterName() + " killed."); // for visual viewing of the simulation;
                                                                        // commented in the final version
    } else { // missed.
      System.out.println(" - missed."); // for visual viewing of the simulation; commented in the final version
    }
  }
}

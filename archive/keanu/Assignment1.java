/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package assignment.pkg1;

/**
 *
 * @author jkdyap
 */
public class Assignment1 {

  /**
   * 
   * 
   * 
   */
  /*
   * ANSWER TO THE QUESTION IN THE ASSIGNMENT
   * 
   * 
   * 
   */
  public static void main(String[] args) {

    // declare and instantiate fights object
    Fights fights = new Fights();
    // simulate the fights
    // argument: 1 for 1st strategy,
    System.out.println("Strategy 1");
    fights.fights(1);

    // argument: 2 for 2nd strategy
    System.out.println("\n\nStrategy 2");
    fights.resetStats(); // reset the number of wins first
    fights.fights(2);

  }
}

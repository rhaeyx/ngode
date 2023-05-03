/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package it2344assignment02;

/**
 *
 * @author jbcan
 */
public class ComputerScienceStud extends Student {
  private double msca = 0;
  private String prevStatus = "";

  public ComputerScienceStud(double wpa, double msca) {
    super(wpa);
    this.msca = msca;
    prevStatus = status();
  }

  public void newGrades(double wpa, double msca) {
    this.wpa = wpa;
    this.msca = msca;
    this.prevStatus = status();
  }

  public void printStatus() {
    System.out
        .println("Computer Science Student with " + Double.toString(this.wpa) + " WPA and " + Double.toString(this.msca)
            + " MSCA is " + this.prevStatus);
  }

  @Override
  public String status() {
    // by default a student is retained unless proven otherwise
    String stat = "retained";
    int fails = 0;

    // if student's wpa failed
    if (this.wpa < 80) {
      fails++;
    }

    // if student's msca failed
    if (this.msca < 80) {
      fails++;
    }

    // logic for students with one failure
    if (fails == 1) {
      // Students under probation and who failed at either of the criteria are advised
      // to shift
      if (this.prevStatus.equals("under_probation")) {
        stat = "advised_to_shift";
      } else { // Students not under probation but failed on one criteria are placed on
               // probation
        stat = "under_probation";
      }
    }

    // logic for students that failed both criterias
    if (fails == 2) {
      stat = "advised_to_shift";
    }

    return stat;
  }

}

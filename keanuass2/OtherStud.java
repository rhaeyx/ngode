/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package it2344assignment02;

/**
 *
 * @author jbcan
 */
public class OtherStud extends Student {
  private String prevStatus = "";

  public OtherStud(double wpa) {
    super(wpa);
    this.prevStatus = status();
  }

  public void newGrades(double wpa) {
    // The students cumulative WPA should be checked
    this.wpa = wpa;
    this.prevStatus = status();
  }

  public void printStatus() {
    System.out.println(
        "Regular Student with " + Double.toString(this.wpa) + " WPA is " + this.prevStatus);
  }

  @Override
  public String status() {
    // student is retained unless proven otherwise
    String stat = "retained";

    if (this.wpa < 75) {
      if (this.prevStatus.equals("under_probation")) {
        stat = "advised_to_shift";
      } else {
        stat = "under_probation";
      }
    }
    return stat;
  }
}

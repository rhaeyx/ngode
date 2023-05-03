/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package it2344assignment02;

/**
 *
 * @author jbcan
 */
public class ManagementEngineeringStud extends Student {
  private String prevStatus = "";

  public ManagementEngineeringStud(double wpa) {
    super(wpa);
    this.prevStatus = status();
  }

  public void newGrades(double wpa) {
    // The students cumulative WPA should be checked
    this.wpa = (this.wpa + wpa) / 2;
    this.prevStatus = status();
  }

  public void printStatus() {
    System.out.println(
        "Management Engineering Student with " + Double.toString(this.wpa) + " cumulative WPA is " + this.prevStatus);
  }

  @Override
  public String status() {
    // status is retained until proven otherwise
    String stat = "retained";

    // if wpa is less than 87, their status is advised_to_shift
    if (this.wpa < 87) {
      stat = "advised_to_shift";
    }

    // Students whose WPA is between 87% to 88.9% are retained but placed on
    // probation
    if (this.wpa >= 87 && this.wpa <= 88.9) {
      stat = "under_probation";
    }

    return stat;
  }

}

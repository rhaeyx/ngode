/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package it2344assignment02;

/**
 *
 * @author jbcan
 */
public class IT2344Assignment02 {

  /**
   * @param args the command line arguments
   */
  public static void main(String[] args) {
    // Computer Science Student
    System.out.println("Computer Science Student");
    ComputerScienceStud cs_stud = new ComputerScienceStud(87, 95);
    cs_stud.printStatus();
    // new semester
    cs_stud.newGrades(79, 86);
    cs_stud.printStatus();

    System.out.println("---------------------------------------------");

    // Management Engineering Student
    System.out.println("Management Engineering Student");
    ManagementEngineeringStud me_stud = new ManagementEngineeringStud(88);
    me_stud.printStatus();
    // new semester
    me_stud.newGrades(93);
    me_stud.printStatus();

    System.out.println("---------------------------------------------");

    // Management Engineering Student
    System.out.println("Regular Student");
    OtherStud regular_stud = new OtherStud(90);
    regular_stud.printStatus();
    // // new semester
    // regular_stud.newGrades(93);
    // regular_stud.printStatus();
  }

}

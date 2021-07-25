package com.exercise.module1;
import java.util.Arrays;
import java.util.HashMap;


public class Module1Exercise {

  public static void main(String[] args) {
    // startSimpleInterestCalculator();
    System.out.println("Computed raise: " + computeRaise(10000, "excellent"));
    long [] salaries = {500, 900, 1000, 1200, 5000, 5500, 2500, 3000, 4000, 1500};
    System.out.println("List of salaries: " + Arrays.toString(salaries));
    System.out.println("Average band salaries: " + computeAvgSalaryPerBand(salaries));
  }

  // 1. The input to the method includes the current annual salary for the employee and a number indicating
  // the performance rating ("excellent", "good", and "poor"). An employee with a rating of "excellent" will receive a 6% raise, an
  // employee with a rating of "good" will receive a 4% raise, and one with a rating of "poor" will receive a 1.5% raise

  public static double computeRaise(long currentAnnualSalary, String rating) {
    switch(rating.toLowerCase()){
      case "excellent":
        return currentAnnualSalary + (0.6 * currentAnnualSalary);

      case "good":
        return currentAnnualSalary + (0.4 * currentAnnualSalary);
      
      case "poor":
        return currentAnnualSalary + (0.15 * currentAnnualSalary);
      
      default:
        System.out.println("Error: Invalid rating!");
        return currentAnnualSalary;
    }
  }

  // 2. The input to the method includes a list of all salaries
  // compute the average of all the input salaries grouped by salary bands
  // "band1" : less than $1000, "band2": $1000 >= and <$5000, "band3": >= $5000

  public static HashMap<String, Long> computeAvgSalaryPerBand(long[] salaries) {
    HashMap<String, Long> averageSalaries = new HashMap<>();
    averageSalaries.put("band1", 0l);
    averageSalaries.put("band2", 0l);
    averageSalaries.put("band3", 0l);
    int band1_count = 0, band2_count = 0, band3_count = 0;
    for(int i=0; i<salaries.length; i++){
      if(salaries[i] > 0 && salaries[i] < 1000){
        band1_count++;
        averageSalaries.put("band1", averageSalaries.get("band1") + salaries[i]);
      }else if(salaries[i] >= 1000 && salaries[i] < 5000){
        band2_count++;
        averageSalaries.put("band2", averageSalaries.get("band2") + salaries[i]);
      }else if(salaries[i] >= 5000){
        band3_count++;
        averageSalaries.put("band3", averageSalaries.get("band3") + salaries[i]);
      }else{
        System.out.println("Error: Invalid input!");
        return null;
      }
    }
    if(band1_count > 0)
      averageSalaries.put("band1", averageSalaries.get("band1") / band1_count);
    if(band2_count > 0)
      averageSalaries.put("band2", averageSalaries.get("band2") / band2_count);
    if(band3_count > 0)
      averageSalaries.put("band3", averageSalaries.get("band3") / band3_count);
    return averageSalaries;
  }
}

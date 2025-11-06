// Java Program to demonstrate variables, arithmetic operations, and basic concepts

import java.util.Scanner; // for taking user input

public class Basics {
    public static void main(String[] args) {
        
        // Variable Declaration and Initialization
        int a = 10;           // integer variable
        double b = 5.5;       // decimal number
        char letter = 'A';    // single character
        String name = "Asmita"; // text (string)
        boolean isLearning = true; // true/false

        // Displaying the variables
        System.out.println("Name: " + name);
        System.out.println("Letter: " + letter);
        System.out.println("Is learning Java? " + isLearning);
        System.out.println("Initial values -> a: " + a + ", b: " + b);

        // Arithmetic Operations
        double sum = a + b;
        double difference = a - b;
        double product = a * b;
        double quotient = a / b;
        double remainder = a % b;

        System.out.println("\nArithmetic Operations:");
        System.out.println("Sum = " + sum);
        System.out.println("Difference = " +difference);
        System.out.println("Product = " + product);
        System.out.println("Quotient = " + quotient);
        System.out.println("Remainder = " + remainder);

        // 🔹 4. Taking user input
        Scanner input = new Scanner(System.in);
        System.out.print("\nEnter your age: ");
        int age = input.nextInt();

        // 🔹 5. Conditional Statement
        if (age >= 18) {
            System.out.println("You are an adult!");
        } else {
            System.out.println("You are still a teenager!");
        }

        // 🔹 6. Increment, Decrement, and Compound Assignment
        a++; // a = a + 1
        b += 2.5; // b = b + 2.5

        System.out.println("\nAfter updating values:");
        System.out.println("a = " + a);
        System.out.println("b = " + b);

        // 🔹 7. Type Casting Example
        int convertedB = (int) b; // converting double to int
        System.out.println("Converted b to int: " + convertedB);

        input.close(); // close scanner
    }
}

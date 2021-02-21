package com.github.varunkudva;

import java.util.Scanner;

public class Addition {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the first integer:");
        int num1 = input.nextInt();
        System.out.print("Enter the second integer:");
        int num2 = input.nextInt();

        int res = num1 + num2;
        System.out.printf("Sum is: %d", res);

    }
}

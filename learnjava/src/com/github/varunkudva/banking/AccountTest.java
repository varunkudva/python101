package com.github.varunkudva.banking;

import org.junit.Assert;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;

import java.util.Scanner;

import static org.junit.Assert.*;

public class AccountTest {
    private Account a1;
    private Account a2;

    @BeforeClass
    public static void setUp() throws Exception {
    }

    @Test
    public void setBalance() {
    }

    @Test
    public void TestDeposit() {
        Account a1 = new Account("Varun", 200);
        Account a2 = new Account("divya", 400);
        a1.deposit(100);
        System.out.println(a1);
        Assert.assertEquals(300.0, a1.getBalance(), 0.0);
    }

    @Test
    public void TestInteractive() {
        Scanner input = new Scanner(System.in);
        System.out.println("Input account name:");
        String name = input.nextLine();
        System.out.println("Input balance:");
        Double balance = input.nextDouble();
        Account newAccount = new Account(name, balance);
        System.out.println(newAccount);
    }
}
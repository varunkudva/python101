package com.github.varunkudva.student;

public class Student {
    private String name;
    private Double average;

    public Student(String name, double av) {
        this.name = name;
        if (av > 0 && av <= 100) {
            this.average = av;
        }
    }

    public String getLetterGrade() {
        String letterGrade = "";
        if (average >= 90.0) {
            letterGrade = "A";
        }

    }

}

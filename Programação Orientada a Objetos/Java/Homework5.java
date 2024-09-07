// File name - Homework5.java
// Duarte Rodrigues - a22206488
// Licenciatura de Engenharia Informática e Aplicações - IPLuso


import java.util.Date;
import java.lang.Math;

class Employee{
    String name;
    int age;
    String designation;
    double salary;

    public Employee(String name, int age, String designation, double salary){
        this.name = name;
        this.age = age;
        this.designation = designation;
        this.salary = salary;
    }

    public void displayInfo(){
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Designation" + designation);
        System.out.println("Salary: " + salary);
        System.out.println();
    }
}

class Bike{
    double price;
    String model;
    String colour;

    public Bike(double price, String model, String color){
        this.price = price;
        this.model = model;
        this.colour = color;
    }
    
    public double speed(){
        return price * 0.02;
    }

    public void printDetails(){
        System.out.println("Model: " + model);
        System.out.println("Price: " + price);
        System.out.println("Colour: " + colour);
        System.out.println("Speed: " + speed() + " Mph");
        System.out.println();
    }
}

class Student{
    private int enrollmentNumber;
    private String courseName;
    private Date birthDate;

    public Student(int enrollmentNumber, String courseName, Date birthDate){
        this.enrollmentNumber = enrollmentNumber;
        this.courseName = courseName;
        this.birthDate = birthDate;
    }

    public long calculateAgeInDays(){
        Date currentDate = new Date();
        long ageInMillis = currentDate.getTime() - birthDate.getTime();
        return ageInMillis / (24*60*60*1000);
    }

    public void printDetails(){
        System.out.println("Enrollment Number: " + enrollmentNumber);
        System.out.println("Course Name: " + courseName);
        System.out.println("Age in days: " + calculateAgeInDays() + " days");
        System.out.println();
    }
}

class Data{
    private int day;
    private int month;
    private int year;

    public void setDay(int day) {
        if (isValidDate(day, month, year)) {
            this.day = day;
        } else {
            System.out.println("Invalid day for the given month and year.");
        }
    }

    public int getDay() {
        return day;
    }

    public void setMonth(int month) {
        if (isValidDate(day, month, year)) {
            this.month = month;
        } else {
            System.out.println("Invalid month for the given day and year.");
        }
    }

    public int getMonth() {
        return month;
    }

    public void setYear(int year) {
        if (isValidDate(day, month, year)) {
            this.year = year;
        } else {
            System.out.println("Invalid year for the given day and month.");
        }
    }

    public int getYear() {
        return year;
    }

    public boolean isValidDate(int day, int month, int year) {
        if (year >= 1 && month >= 1 && month <= 12) {
            int maxDay = 31;
            if (month == 4 || month == 6 || month == 9 || month == 11) {
                maxDay = 30;
            } else if (month == 2) {
                if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
                    maxDay = 29; // Leap year
                } else {
                    maxDay = 28; // Non-leap year
                }
            }
            return day >= 1 && day <= maxDay;
        }
        return false;
    }
}

class Animal{
    private String skinColour;
    private String name;

    public Animal(String skinColor, String name){
        this.skinColour=skinColor;
        this.name = name;
    }

    public void voice(){
        System.out.println(name + " makes a sound");
    }

    public void sleep(){
        System.out.println(name + " sleeps all day long");
    }

    public void printDetails(){
        System.out.println("Name: " +name);
        System.out.println("Skin colour: "+skinColour);
    }
}

class Weather{
    private String season;
    private double temperature;

    public Weather(String season, double temperature){
        this.season=season;
        this.temperature=temperature;
    }

    public void predictRain(){
        if(season.equalsIgnoreCase("Spring") && temperature >= 15 && temperature <=25){
            System.out.println("It may rain today.");
        }
        if(season.equalsIgnoreCase("Summer") && temperature >= 25 && temperature <=35){
            System.out.println("It may rain today.");
        }
        if(season.equalsIgnoreCase("Fall") && temperature >= 10 && temperature <=20){
            System.out.println("It may rain today.");
        }
        if(season.equalsIgnoreCase("Winter") && temperature >= 0 && temperature <=10){
            System.out.println("It may rain today.");
        } else {
            System.out.println("No chance of rain in the current weather conditions.");
        }
    }
}

class Cow{
    String country;
    int age;
    String colour;
    boolean produce_milk;

    public Cow(String country, int age, String colour, boolean produce_milk){
        this.country = country;
        this.age = age;
        this.colour = colour;
        this.produce_milk = produce_milk;
    }

    public void cowInfo(){
        System.out.println("Country: " +country);
        System.out.println("Age" + age);
        System.out.println("Colour: " + colour);
        System.out.println("Produces Milk: "+ (produce_milk ? "Yes" : "No"));
    }
}

class factorial_calculator{
    public int calculateFactorial(int number) {
        if (number == 0 || number == 1) {
            return 1;
        } else{
            int result = 1;
            for (int i = 2; i <= number; i++) {
                result *= i;
            }
            return result;    
        }
    }
}

class Account{
    private double balance;

    public Account(double initialBalance){
        balance = initialBalance;
    }

    public void deposit(double amount){
        if (amount > 0) {
            balance += amount;
            System.out.println("Deposited: $" + amount);
        } else{
            System.out.println("Invalid deposit amount");
        }
    }

    public void withdraw (double amount){
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            System.out.println("Withdrawn: $" + amount);
        } else{
            System.out.println("Invalid withdrawal amount or insufficient balance.");
        }
    }

    public void displayBalance(){
        System.out.println("Current Balance: $" + balance);
    }
}

class BMI_Calculator{
    private double height;
    private double weight;

    public BMI_Calculator(double height, double weight){
        this.height = height;
        this.weight = weight;
    }

    public double calculateBMI(){
        return weight / (height*height);
    }

    public void checkObesityStatus(){
        double bmiValue = calculateBMI();
        System.out.println("BMI: " + bmiValue);
        if (bmiValue >= 50) {
            System.out.println("BMI indicates obesity");
        } else{
            System.out.println("BMI does not indicate obesity");
        }
    }
}

class Triangle{
    private double side1;
    private double side2;
    private double side3;

    public Triangle(double side1, double side2, double side3){
        this.side1 = side1;
        this.side2 = side2;
        this.side3 = side3;
    }

    public double area(){
        double s = (side1+side2+side3)/2;
        return Math.sqrt(s*(s-side1)*(s-side2)*(s-side3));
    }

    public double longest_side_range(){
        double longestSide = Math.max(side1, Math.max(side2, side3));
        return longestSide;
    }
}

class Shape{
    public double getPerimeter(){
        return 0.0;
    }

    public double getArea(){
        return 0.0;
    }
}

class CircleShape extends Shape{
    private double radius;

    public CircleShape(double radius){
        this.radius = radius;
    }

    @Override
    public double getPerimeter(){
        return 2*Math.PI*radius;
    }

    @Override
    public double getArea(){
        return Math.PI * radius * radius;
    }
}

class RectangleShape extends Shape{
    private double length;
    private double width;

    public RectangleShape(double length, double width){
        this.length = length;
        this.width = width;
    }

    @Override
    public double getPerimeter(){
        return 2*(length + width);
    }

    @Override
    public double getArea(){
        return length * width;
    }
}


class TriangleShape extends Shape{
    private double side1;
    private double side2;
    private double side3;

    public TriangleShape(double side1, double side2, double side3){
        this.side1 = side1;
        this.side2 = side2;
        this.side3 = side3;
    }

    @Override
    public double getPerimeter(){
        return side1+side2+side3;
    }

    @Override
    public double getArea(){
        double s = getPerimeter() /2;
        return Math.sqrt(s*(s-side1)*(s-side2)*(s-side3));
    }
}

class EletronicDevice{
    private String name;
    private String brand;
    private String model;
    private String specifications;

    public EletronicDevice(String name, String brand, String model, String specifications){
        this.name = name;
        this.brand = brand;
        this.model = model;
        this.specifications = specifications;
    }

    public void specification(){
        System.out.println("Name: " +name);
        System.out.println("Brand: " +brand);
        System.out.println("Model: " +model);
        System.out.println("Specifications: " +specifications);
        System.out.println();
    }
}

class CurrencyChangerCalculator{
    private double amount;
    private double exchangeRate;

    public CurrencyChangerCalculator(double exchangeRate){
        this.exchangeRate = exchangeRate;
    }

    public void setAmount(double amount){
        this.amount = amount;
    }

    public double displayAmount(){
        return amount;
    }

    public double convertCurrency(){
        return amount * exchangeRate;
    }
}

class Encoded_Greeting{
    private String greeting;

    public Encoded_Greeting(String greeting){
        this.greeting = greeting;
    }

    public void encode_G(){
        StringBuilder encodedGreeting = new StringBuilder();
        for(char c : greeting.toCharArray()){
            encodedGreeting.append((char) (c+1));
        }
        System.out.println("Original Greeting: " + greeting);
        System.out.println("Encoded Greeting: " + encodedGreeting.toString());
    }
}

public class Homework5{
    public static void main(String[] args){
        Employee employee1 = new Employee("John Doe", 30, "Manager", 500);
        Employee employee2 = new Employee("Alice Smith", 25, "Engineer", 350);
        Employee employee3 = new Employee("Bob Johnson", 35, "Designer", 420);
        Employee employee4 = new Employee("Eva Green", 28, "Developer", 380);

        Employee[] employees = {employee1, employee2, employee3, employee4};

        Bike bike1 = new Bike(300, "Mountain Bike", "Red");
        Bike bike2 = new Bike(250, "City Bike", "Blue");
        Bike bike3 = new Bike(400, "Road Bike", "Black");
        Bike bike4 = new Bike(350, "Hybrid Bike", "Green");

        Date birthDate1 = new Date(2000-1900, 5, 15);
        Student student1 = new Student(101, "Computer Science", birthDate1);

        Date birthDate2 = new Date(1999-1900, 8, 20);
        Student student2 = new Student(102, "Mathematics", birthDate2);

        Data date = new Data();

        Animal animal1 = new Animal("Brown", "Lion");
        Animal animal2 = new Animal("Gray", "Elephant");

        Weather todayWeather = new Weather("Spring", 20.0);

        Cow cow1 = new Cow("India", 5, "Brown", true);
        Cow cow2 = new Cow("USA", 6, "Black & White", false);

        int num = 5;

        int factorial = new factorial_calculator().calculateFactorial(num);

        Account account = new Account(1000.0);

        BMI_Calculator person1 = new BMI_Calculator(1.75, 80.0);

        Triangle triangle1 = new Triangle(3.0,4.0,5.0);
        double area1 = triangle1.area();
        double longestside1 = triangle1.longest_side_range();
        Triangle triangle2 = new Triangle(5.0,6.0,3.0);
        double area2 = triangle2.area();
        double longestside2 = triangle2.longest_side_range();

        Shape shape1 = new CircleShape(5.0);
        Shape shape2 = new RectangleShape(3.0, 4.0);
        Shape shape3 = new TriangleShape(3.0, 4.0, 5.0);

        EletronicDevice device1 = new EletronicDevice("Laptop", "Dell", "XPS 13", "Intel i7, 16GB RAM, 512GB SSD");
        EletronicDevice device2 = new EletronicDevice("Smartphone", "Apple", "iPhone 13 Pro", "A15 Bionic, 128GB storage");
        EletronicDevice device3 = new EletronicDevice("TV", "Samsung", "QLED 4K", "55-inch display, HDR10+");
        EletronicDevice device4 = new EletronicDevice("Tablet", "Samsung", "Galaxy Tab S7", "Snapdragon 865+, 128GB storage");
        EletronicDevice device5 = new EletronicDevice("Smart Speaker", "Amazon", "Echo Dot", "Voice-controlled, Bluetooth speaker");

        CurrencyChangerCalculator converter = new CurrencyChangerCalculator(1.2);
        converter.setAmount(100.0);
        double convertedAmount = converter.convertCurrency();

        Encoded_Greeting greeting = new Encoded_Greeting("Happy Birthday");

        for (Employee employee : employees){
            if (employee.salary < 400){
                employee.displayInfo();
            }
        }

        System.out.println("Details of Bike 1:");
        bike1.printDetails();

        System.out.println("Details of Bike 2:");
        bike2.printDetails();

        System.out.println("Details of Student 1:");
        student1.printDetails();

        System.out.println("Details of Student 2:");
        student2.printDetails();

        date.setYear(2023);
        date.setMonth(10);
        date.setDay(20);
        System.out.println("Year: " + date.getYear());
        System.out.println("Month: " + date.getMonth());
        System.out.println("Day: " + date.getDay());

        System.out.println("Details of Animal 1: ");
        animal1.printDetails();
        animal1.voice();
        animal1.sleep();

        System.out.println("Details of Animal 2:");
        animal2.printDetails();
        animal2.voice();
        animal2.sleep();

        todayWeather.predictRain();

        System.out.println("Cow 1 Info:");
        cow1.cowInfo();

        System.out.println("Cow 2 Info:");
        cow2.cowInfo();

        System.out.println("Factorial of " + num + " is: " + factorial);

        account.displayBalance();
        account.deposit(500.0);
        account.displayBalance();
        account.withdraw(300.0);
        account.displayBalance();
        account.withdraw(1500.0);
        account.displayBalance();

        person1.checkObesityStatus();

        System.out.println("Triangle 1 Area: " + area1);
        System.out.println("The longest side of the triangle is: " + longestside1);
        System.out.println("Triangle 2 Area: " + area2);
        System.out.println("The longest side of the triangle is: " + longestside2);

        System.out.println("Shape 1 Perimeter: " + shape1.getPerimeter());
        System.out.println("Shape 1 Area: " + shape1.getArea());
        System.out.println("Shape 2 Perimeter: " + shape2.getPerimeter());
        System.out.println("Shape 2 Area: " + shape2.getArea());
        System.out.println("Shape 3 Perimeter: " + shape3.getPerimeter());
        System.out.println("Shape 3 Area: " + shape3.getArea());

        System.out.println("Electronic Device 1 Specification:");
        device1.specification();
        System.out.println("Electronic Device 2 Specification:");
        device2.specification();
        System.out.println("Electronic Device 3 Specification:");
        device3.specification();
        System.out.println("Electronic Device 4 Specification:");
        device4.specification();
        System.out.println("Electronic Device 5 Specification:");
        device5.specification();

        System.out.println("Amount in source currency: " + converter.displayAmount());
        System.out.println("Converted amount in target currency: " + convertedAmount);

        greeting.encode_G();
    }
}
## File Name - Exercises.py
## Duarte Rodrigues - a22206488
## Licenciatura de Engenharia Informática e Aplicações - IPLuso

import Classes
import math
from datetime import datetime

def Q1():
    ## Write a program with four instance variables - name, age, designation and salary. The class employee has one explicitly defined constructor, which takes a parameter. Create four object and print employee info of only those employee whose salary is less than 400 euro.
    # Create four objects for the 'Employee' class.
    employee1 = Classes.Employee("John Doe", 30, "Software Engineer", 350)
    employee2 = Classes.Employee("Alice Smith", 28, "Data Analyst", 420)
    employee3 = Classes.Employee("Bob Johnson", 35, "Manager", 380)
    employee4 = Classes.Employee("Eva Brown", 27, "Designer", 300)

    # Store the objects within a list.
    employees = [employee1, employee2, employee3, employee4]

    # Print to terminal the info of the employee objects whose salary is less than 400 euro.
    for employee in employees:
        if employee.salary < 400:
            print(f"Name: {employee.name}")
            print(f"Age: {employee.age} years")
            print(f"Designation: {employee.designation}")
            print(f"Salary: {employee.salary}€")
            print()
    pass        

def Q2():
    ## Write a Program to create a class “bike with price, Model and color attribute. Create four instances of “bike” class and create two objects and print the model, weight, price, color and speed().
    # Create four objects for the 'Bike' class.
    bike1 = Classes.Bike(500, "Mountain Bike", "Red", 15)
    bike2 = Classes.Bike(600, "Dirt Bike", "Blue", 14)
    bike3 = Classes.Bike(400, "Pedestrian Bike", "Green", 16)
    bike4 = Classes.Bike(700, "Sports Bike", "Yellow", 13)

    # Print to terminal the info of the first two bike objects
    print("Bike 1 Information:")
    print(f"Model: {bike1.model}")
    print(f"Weight: {bike1.weight} kg")
    print(f"Price: {bike1.price} euros")
    print(f"Color: {bike1.colour}")
    print(f"Speed: {bike1.speed()} km/h\n")

    print("Bike 2 Information:")
    print(f"Model: {bike2.model}")
    print(f"Weight: {bike2.weight} kg")
    print(f"Price: {bike2.price} euros")
    print(f"Color: {bike2.colour}")
    print(f"Speed: {bike2.speed()} km/h\n")
    pass

def Q3():
    ## Write a program to create a class called "Students" with an enrollment number and a course name attribute and a method to change age into day. Create two instances of the “student” class, define their attributes using the constructor and print their name and age in days.
    # Creating birthdates for each object in the 'Students' class, assuming you have birthdates in the format "YYYY-MM-DD"
    birthdate1 = datetime(2000, 5, 15)
    birthdate2 = datetime(1998, 8, 22)

    # Create two objects for the 'Students' class
    student1 = Classes.Students(100, "Mathematics", birthdate1)
    student2 = Classes.Students(305, "Science", birthdate2)

    # Print to terminal the info of each student
    print("Student 1 Information:")
    print(f"Enrollment Number: {student1.enrollment_number}")
    print(f"Course Name: {student1.course_name}")
    print(f"Age in Days: {student1.calculateAgeInDays()} days\n")

    print("Student 2 Information:")
    print(f"Enrollment Number: {student2.enrollment_number}")
    print(f"Course Name: {student2.course_name}")
    print(f"Age in Days: {student2.calculateAgeInDays()} days\n")
    pass

def Q4():
    ## Write a program to implement a class called Date that has private member variables for day, month, and year. Include member functions to set and get these variables, as well as to validate if the date is valid.
    # Create an object for the 'Date' class
    date = Classes.Date(1, 1, 2023)

    #Set a new date
    date.setDate(31, 12, 2023)

    # Get and print the date components
    print(f"Day: {date.getDay()}")
    print(f"Month: {date.getMonth()}")
    print(f"Year: {date.getYear()}\n")
    pass

def Q5():
    ## Write a program to create a class called "Animal" with a skin color and name attribute. Create two instances of the "Animal" class, set their attributes using the constructor, and print their attribute and call method voice () and sleep ().
    # Create two objects for the 'Date' class
    animal1 = Classes.Animal("Brown", "Lion")
    animal2 = Classes.Animal("White", "Polar Bear")

    # Print to terminal the attributes and call methods for both animals
    print(f"The {animal1.name} has {animal1.skin_colour} fur")
    animal1.voice()
    animal1.sleep()
    print(f"The {animal2.name} has {animal2.skin_colour} fur")
    animal2.voice()
    animal2.sleep()
    pass

def Q6():
    ## Write a Program to create a class Weather with two instance variables season and temperature and set their attributes using the constructor and write a method that predict today is rain or not using two instance variables temperature and season(hint: if else)
    # Create an object for the 'Weather' class
    todayWeather = Classes.Weather("Spring", 15)

    # Predict the weather and print to terminal the results of the prediction method
    prediction = todayWeather.predictWeather()
    print(f"Today's weather prediction: {prediction}")
    pass

def Q7():
    ## Write a program to create a class Cow with Instance Variables; String country;    int age;    String color;   Bol produce_milk; And print Cow_info();
    # Create two objects for the 'Cow' class
    cow1 = Classes.Cow("India", 5, "Brown", True)
    cow2 = Classes.Cow("United States", 4, "Black & White", False)
    
    # Print to terminal the attributes of the cows
    print("Cow Information:")
    print(cow1.cowInfo())
    print(cow2.cowInfo())
    pass

def Q8():
    ## Write a program to create a class factorial_calculator and use an anonymous object and print the factorial of any given number
    # Use an anonymous object to calculate the factorial of a number
    n = 5
    # Create an object for the 'Factorial_Calculator' class
    result = Classes.Factorial_calculator().calculate_factorial(n)

    # Print to terminal the result of the factorial of the number
    print(f"The factorial of {n} is {result}")
    pass

def Q9():
    ## Write a program to create an Account class which has deposit () and withdraw () methods  and display the result
    # Create an object for the 'Account' class with an initial balance
    account = Classes.Account(1000)

    # Perform deposit and withdrawal operations and display the results
    print(account.deposit(500))
    print(account.withdraw(300))
    print(account.withdraw(1500))
    pass

def Q10():
    ## Write a program to create a class BMI_Calculator with instance variable of height and weight and print the result BMI lies in obsessed or not.  
    # Ask the user to input the height and weight for BMI calculation
    height = float(input('Enter your height in centimeters: '))
    weight = float(input('Enter your weight in kilograms: '))

    # Create an object for the 'BMI_Calculator' class
    bmiCalc = Classes.BMI_Calculator(height, weight)

    # Calculate BMI and determine if it indicates obesity
    bmi = bmiCalc.calculateBMI()
    result = bmiCalc.isObese(bmi)

    # Print to terminal the result of the BMI calculation and if the person is obese or not
    print(f"Your BMI is {round(bmi, 2)} which means you are {result}") 
    pass

def Q11():
    ## Write a Program to create a triangle class with two methods area () and longest _side_range() then print out the results
    ## Ask the user to atribute the values to each side of the triangle.
    side1 = float(input("Enter the length of the first side: "))
    side2 = float(input("Enter the length of the second side: "))
    side3 = float(input("Enter the length of the third side: "))

    # Create an object for the 'Triangle' class
    triangle = Classes.Triangle(side1, side2, side3)

    # Calculate the area of the triangle
    area = triangle.area()

    # Determine the range of the longest side
    range_result = triangle.longestSideRange()

    # Print to terminal the area of the triangle and the longest side of the triangle
    print(f"The area of the triangle is: {area:.2f} square units.")
    print(range_result) 
    pass

def Q12():
    ## Write a Java program to create a class called Shape with methods called getPerimeter() and getArea(). Create the three objects of shape class and display their results.
    # Create objects for the 'Shape' class
    rectangle = Classes.RectangleShape(5,4)
    circle = Classes.CircleShape(3)
    triangle = Classes.TriangleShape(6,4)

    # Print to terminal the perimeter and area results
    print("Rectangle - Perimeter:", rectangle.getPerimeter())
    print("Rectangle - Area:", rectangle.getArea())

    print("Circle - Perimeter:", circle.getPerimeter())
    print("Circle - Area:", circle.getArea())

    print("Triangle - Perimeter:", triangle.getPerimeter())
    print("Triangle - Area:", triangle.getArea())
    pass

def Q13():
    ## Write a java program to create class electronic devices with specification method which display the information of at least five object of class electronic device.
    # Create five objects for the 'EletronicDevice' class
    device1 = Classes.ElectronicDevice("Apple", "iPhone 13", 2021, 999.99)
    device2 = Classes.ElectronicDevice("Samsung", "Galaxy S21", 2021, 799.99)
    device3 = Classes.ElectronicDevice("Sony", "PlayStation 5", 2020, 499.99)
    device4 = Classes.ElectronicDevice("Dell", "XPS 13", 2022, 1199.99)
    device5 = Classes.ElectronicDevice("LG", "OLED TV", 2021, 1499.99)

    # Print to terminal the info of each eletronic device
    print("Electronic Device Specifications:")
    device1.specification()
    device2.specification()
    device3.specification()
    device4.specification()
    device5.specification()
    pass

def Q14():
    ## Write a program to create class currency_Changer_calculator in which you have to write a function for currency changer and set the instance variables of class currency_changer_calculator using constructor.
    # Create an object for the 'CurrencyChangerCalculator' class
    calculator = Classes.CurrencyChangerCalculator(0.85)

    # Use the currencyChanger method to convert currency
    amount = 100
    fromCurrency = "USD"
    toCurrency = "EUR"
    result = calculator.currencyChanger(amount, fromCurrency, toCurrency)

    # Print to terminal the conversion result
    print(result)
    pass

def Q15():
    ## Write a java class of Encoded_Greeting to print “happy birthday” and then encode it and display result using string type instance variable and method encode_G().
    # Create an object for the 'EncondedGreeting' class
    greeting = "happy birthday"
    greetingInstance = Classes.EncodedGreeting(greeting)

    # Print to terminal the original greeting
    print("Original Greeting:", greeting)

    # Encode the greeting and print to terminal the result
    encodedMessage = greetingInstance.encodeG()
    print("Encoded Greeting:", encodedMessage)
    pass
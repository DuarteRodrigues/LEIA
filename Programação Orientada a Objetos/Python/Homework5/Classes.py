## File Name - Classes.py
## Duarte Rodrigues - a22206488
## Licenciatura de Engenharia Informática e Aplicações - IPLuso

import math
from datetime import datetime

class Employee():
    # Class constructor
    def __init__(self, name, age, designation, salary):
        self.name = name
        self.age = age
        self.designation = designation
        self.salary = salary
        pass

class Bike():
    # Class Constructor
    def __init__(self, price ,model, colour, weight):
        self.price = price
        self.model = model
        self.colour = colour
        self.weight = weight
        pass

    # Method to determine the speed of the bike
    def speed(self):
        return (1000/self.weight) * (self.price/100)
        pass

class Students():
    # Class Constructor
    def __init__(self, enrollment_number, course_name, birthdate):
        self.enrollment_number = enrollment_number
        self.course_name = course_name
        self.birthdate = birthdate
        pass

    # Method to determine the number of days since the student was born
    def calculateAgeInDays(self):
        today = datetime.now()
        daysSinceBirth = (today-self.birthdate).days
        return daysSinceBirth
        pass

class Date():
    #Class Constructor
    def __init__(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year
        pass
    
    # Setter for day, month and year
    def setDate(self, year, month, day):
        if self.isValidDate(year, month, day):
            self.__year = year
            self.__month = month
            self.__day = day            
        else:
            print("Invalid date. Date not set.")
        pass

    # Getter for day
    def getDay(self):
        return self.__day
        pass
    
    # Getter for month
    def getMonth(self):
        return self.__month
        pass
    
    # Getter for year
    def getYear(self):
        return self.__year
        pass

    # Method to validate the inputed date
    def isValidDate(self, year, month, day):
        if month < 1 or month > 12:
            return False
        
        daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if year %  4 == 0 and (year % 100 != 0 or year % 400 == 0):
            daysInMonth[1] = 29;
        
        if day < 1 or day > daysInMonth[month-1]:
            return False
        return True
        pass

class Animal():
    # Class constructor
    def __init__(self, skin_colour, name):
        self.skin_colour = skin_colour
        self.name = name
        pass

    # Method to notify the user when the animal makes a sound
    def voice(self):
        print(f"The {self.name} makes a sound.")
        pass

    # Method to notify the user when the animal is sleeping
    def sleep(self):
        print(f"The {self.name} is sleeping\n")
        pass

class Weather():
    # Class constructor
    def __init__(self, season, temperature):
        self.season = season
        self.temperature = temperature
        pass

    # Method to predict the weather based on input
    def predictWeather(self):
        if self.season.lower() == "Winter" and self.temperature < 0:
            return "It might snow or rain.\n"
        elif self.season.lower() == "Spring" and self.temperature >=10:
            return "It's likely to rain today.\n"
        elif self.season.lower() == "Summer" and self.temperature >= 25:
            return "There's a chance of rain or a thunderstorm.\n"
        elif self.season.lower() == "Fall" and self.temperature >= 10:
            return "Expect some rain today.\n"
        else:
            return "Today's weather is uncertain.\n"
        pass

class Cow():
    # Class constructor
    def __init__(self, country, age, colour, produceMilk):
        self.country = country
        self.age = age
        self.colour = colour
        self.produceMilk = produceMilk
        pass

    # Method to display the cow's info
    def cowInfo(self):
        milkStatus = "Produces milk" if self.produceMilk else "Does not produce milk"
        info = f"Country: {self.country}\nAge: {self.age} years\nColor: {self.color}\nMilk Status: {milkStatus}\n"
        return info
        pass

class Factorial_calculator():
    # Method that calculates factorial of an input number
    def calculate_factorial(self, n):
        if n==0:
            return 1
        else: 
            return n*self.calculate_factorial(n-1)
        pass

class Account():
    # Class constructor
    def __init__(self, balance=0):
        self.balance = balance
        pass

    # Method that deposits money into the account
    def deposit(self, amount):
        if amount>0:
            return f"Deposited {amount} euros. New balance: {self.balance} euros."
        else:
            return "Invalid deposit amount."
        pass

    # Method that withdraws money from the account
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount} euros. New balance: {self.balance} euros."
        elif amount > self.balance:
            return "Insufficient balance."
        else:
            return "Invalid withdrawal amount."
        pass

class BMI_Calculator():
    # Class Conductor
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        pass

    # Method that calculates BMI using height in cm and weight in kg
    def calculateBMI(self):
        # Formula to calculate BMI: weight (kg) / (height (m) * height (m))
        heightInMeters = self.height / 100  # Convert height from centimeters to meters
        bmi = self.weight / (heightInMeters * heightInMeters)
        return bmi
        pass

    # Method to determine obesity based on BMI
    def isObese(self, bmi):
        if bmi >= 30:
            return "BMI indicates obesity"
        else:
            return "BMI does not indicate obesity"
        pass

class Triangle:
    # Class Conductor
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        pass

    # Method to calculate the area of the triangle
    def area(self):
        # Heron's formula to calculate the area of a triangle
        s = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return area
        pass

    # Method to determine the size of the longest side
    def longestSideRange(self):
        longest = max(self.side1, self.side2, self.side3)
        shortest = min(self.side1, self.side2, self.side3)
        return f"The range of the longest side is between {shortest} and {longest}."
        pass

class Shape:
    # Getter for the perimeter of the shape
    def getPerimeter(self):
        pass  # This method should be implemented in derived classes

    # Getter for the area of the shape    
    def getArea(self):
        pass  # This method should be implemented in derived classes

class RectangleShape(Shape):
    # Class Conductor
    def __init__(self, width, height):
        self.width = width
        self.height = height
        pass

    # Getter for the perimeter of the rectangle
    def getPerimeter(self):
        return 2 * (self.width + self.height)
        pass

    # Getter for the area of the rectangle
    def getArea(self):
        return self.width * self.height
        pass

class CircleShape(Shape):
    # Class Conductor
    def __init__(self, radius):
        self.radius = radius
        pass

    # Getter for the perimeter of the circle
    def getPerimeter(self):
        return 2 * 3.14159 * self.radius
        pass

    # Getter for the area of the rectangle
    def getArea(self):
        return 3.14159 * self.radius * self.radius
        pass

class TriangleShape(Shape):
    # Class Conductor
    def __init__(self, base, height):
        self.base = base
        self.height = height
        pass

    def getPerimeter(self):
        # Assuming it's an equilateral triangle for simplicity
        return 3 * self.base
        pass

    # Getter for the area of the rectangle
    def getArea(self):
        return 0.5 * self.base * self.height
        pass

class ElectronicDevice():
    # Class Conductor
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        pass

    # Method to display the info on the eletronic device
    def specification(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year of Release: {self.year}")
        print(f"Price: ${self.price:.2f}")
        print()
        pass

class CurrencyChangerCalculator():
    # Class Conductor
    def __init__(self, exchangeRate):
        self.exchangeRate = exchangeRate
        pass

    # Method to exchange the currency
    def currencyChanger(self, amount, fromCurrency, toCurrency):
        convertedAmount = amount * self.exchangeRate
        return f"{amount} {fromCurrency} is equal to {convertedAmount} {toCurrency}"
        pass

class EncodedGreeting:
    # Class Conductor
    def __init__(self, greeting):
        self.greeting = greeting
        pass

    # Method to encode the message
    def encodeG(self):
        encodedMessage = ""
        for char in self.greeting:
            encodedMessage += chr(ord(char) + 1)  # Shift each character by one
        return encodedMessage
        pass
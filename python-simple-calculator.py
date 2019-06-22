# Simple Calculator for Add, Sub, Mul and Div
# StudyGyaan.com

def Addition (num1,num2):
   return num1+num2

def Substraction (num1,num2):
   return num1-num2

def Multiplication (num1,num2):
   return num1*num2

def Division (num1,num2):
   return num1/num2

print("Enter two number for calculation")

num1 = int(input("Enter a number1: "))
num2 = int(input("Enter a number2: "))

print("Enter your choice \n 1. Addition \n 2. Substraction \n 3. Multiplication \n 4.Division")
choice = int(input())

if choice == 1:
   #Addition
   print("Addition",Addition(num1,num2))
elif choice ==2:
   #Substraction
   print("Substraction",Substraction(num1,num2))
elif choice ==3:
   #Multiplication
   print("Multiplication",Multiplication(num1,num2))
elif choice == 4:
   #Division
   print("Division",Division(num1,num2))

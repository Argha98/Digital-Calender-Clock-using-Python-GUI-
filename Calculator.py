#-------------------------------------------------------------------------------
# Name:        Simple Calculator
# Purpose: This is my 1st python project
#
# Author:      Argha
#
# Created:     06-02-2022
# Copyright:   (c) Argha 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

first = input("Enter first number : ")
second = input("Enter second number : ")

first = int(first)
second = int(second)
print("press keys for operator (+,-,*,/,%)")

operator = input("Enter operator : ")
if operator == "+":
  print(first + second)
elif operator == "-":
  print(first - second)
elif operator == "*":
  print(first * second)
elif operator == "/":
  print(first / second)
elif operator == "%":
  print(first % second)
else:
  print("Invalid Operation")
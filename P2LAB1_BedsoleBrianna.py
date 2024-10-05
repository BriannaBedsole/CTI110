#Brianna Bedsole
#10/4/2024
#P2LAB1
#In this lab we will be making a program that can calculate the diameter, circumference, and area of a circle. The program will ask what the radius of the circle is and calculate based off your response.

import math

radius = float(input("What is the radius of the circle? "))

diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print(f"The diameter of the circle is {diameter:.1f}")
print(f"The circumference of the circle is {circumference:.2f}")
print(f"The area of the circle is {area:.3f}")

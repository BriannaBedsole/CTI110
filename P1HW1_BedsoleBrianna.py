#Brianna Bedsole
#9/24/2024
#P1HW1
#In this assignment we use Pythons input and print functions to create a calculator program that calculates exponets, addition, and subtraction. The program will let you insert any integers and will calculate them for you.  

print("-----Calculating Exponents----")
base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))

result_exponent = base ** exponent
print(f"{base} raised to the power of {exponent} is {result_exponent} !!")

print("\n-----Addition and Subtraction----")
start = int(input("Enter a starting integer: "))
add = int(input("Enter an integer to add: "))
subtract = int(input("Enter an integer to subtract: "))

result_math = start + add - subtract
print(f"{start} + {add} - {subtract} is equal to {result_math}")

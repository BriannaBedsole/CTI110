# Brianna Bedsole
# 10/5/2024
# P2LAB2
# In this assignment we will make a program that will give you the MPGs of different cars and it will calculate how many gallons of gas you need based off of how many miles you are going to use on the car.

vehicles = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

keys = vehicles.keys()

print(keys)

selected_vehicle = input("Enter a vehicle to see its mpg: ")

mpg = vehicles[selected_vehicle]
print(f"The {selected_vehicle} gets {mpg} mpg.")

miles = float(input(f"How many miles will you drive the {selected_vehicle}? "))

gallons_needed = miles / mpg

print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {selected_vehicle} {miles} miles.")

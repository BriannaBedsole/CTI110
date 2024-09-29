#Brianna Bedsole
#9/29/2024
#P1HW2
#In this project we will make a program that will calculate travel expenses. The program will ask you questions about your budget and location that you can answer, and it will give you the results of your travel expenses.

"""
Pseudocode:
1. Print program introduction
2. Input budget from user
3. Input travel destination from user
4. Input gas expense from user
5. Input accommodation expense from user
6. Input food expense from user
7. Calculate total expenses (gas + accommodation + food)
8. Calculate remaining balance (budget - total expenses)
9. Print travel expense report
   - Print location
   - Print initial budget
   - Print individual expenses (fuel, accommodation, food)
   - Print remaining balance
"""
print("This program calculates and displays travel expenses")

budget = int(input("\nEnter Budget: "))

destination = input("\nEnter your travel destination: ")

gas = int(input("\nHow much do you think you will spend on gas? "))

accommodation = int(input("\nApproximately, how much will you need for accommodation/hotel? "))

food = int(input("\nLast, how much do you need for food? "))

total_expenses = gas + accommodation + food

remaining_balance = budget - total_expenses

print("------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}")
print()
print(f"Fuel: {gas}")
print(f"Accommodation: {accommodation}")
print(f"Food: {food}")
print()
print(f"Remaining Balance: {remaining_balance}")

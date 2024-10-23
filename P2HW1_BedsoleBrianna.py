# Brianna Bedsole
# 10/23/2024
# P2HW1
# In this assignment we will be making a calculator that calculates travel expenses.

print('This program calculates and displays travel expenses')
print()

budget = float(input('Enter Budget: '))
destination = input('Enter your travel destination: ')
gas = float(input('How much do you think you will spend on gas? '))
hotel = float(input('Approximately, how much will you need for accommodation/hotel? '))
food = float(input('Last, how much do you need for food? '))

remaining = budget - gas - hotel - food

print()
print('------------Travel Expenses------------')
print(f'{"Location:":<20} {destination}')
print(f'{"Initial Budget:":<20} ${budget:,.2f}')
print(f'{"Fuel:":<20} ${gas:,.2f}')
print(f'{"Accommodation:":<20} ${hotel:,.2f}')
print(f'{"Food:":<20} ${food:,.2f}')
print('----------------------------------------')
print(f'{"Remaining Balance:":<20} ${remaining:,.2f}')

# Brianna Bedsole
# 11/17/2024
# P5LAB
# In this lab we will make a self-checkout calculator that will tell you how much you owe and give you your calculated change based off how much money you put into the self-checkout. 

import random

def disperse_change(change_amount):

    pennies = round(change_amount * 100)
    
    dollars = pennies // 100
    pennies = pennies % 100
    
    quarters = pennies // 25
    pennies = pennies % 25
    
    dimes = pennies // 10
    pennies = pennies % 10
    
    nickels = pennies // 5
    pennies = pennies % 5
    
    if dollars > 0:
        print(f"{dollars} Dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        print(f"{quarters} Quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        print(f"{dimes} Dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        print(f"{nickels} Nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        print(f"{pennies} Penn{'ies' if pennies > 1 else 'y'}")

def main():
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You Owe ${amount_owed:.2f}")
    
    cash_input = float(input("How much cash will you put in the self-checkout? "))
    
    change = round(cash_input - amount_owed, 2)
    
    print(f"Change is: ${change:.2f}\n")
    
    disperse_change(change)

if __name__ == "__main__":
    main()

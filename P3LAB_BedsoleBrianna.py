# Brianna Bedsole
# 10/23/2024
# P3LAB
# In this lab we make a program that takes an amount of money as input and calculates what the amount is made up of, such as dollars, quarters, dimes, etc.

def main():
    user_input = input("Enter the amount of money as a float: ").strip().replace('$', '')
    amount = float(user_input)
    
    if amount == 0:
        print("No change")
        return
        
    cents = int(round(amount * 100))
    
    dollars = cents // 100
    remaining = cents % 100
    
    quarters = remaining // 25
    remaining = remaining % 25
    
    dimes = remaining // 10
    remaining = remaining % 10
    
    nickels = remaining // 5
    pennies = remaining % 5
    
    if dollars > 0:
        print(f"{dollars} {'Dollar' if dollars == 1 else 'Dollars'}")
            
    if quarters > 0:
        print(f"{quarters} {'Quarter' if quarters == 1 else 'Quarters'}")
            
    if dimes > 0:
        print(f"{dimes} {'Dime' if dimes == 1 else 'Dimes'}")
            
    if nickels > 0:
        print(f"{nickels} {'Nickel' if nickels == 1 else 'Nickels'}")
            
    if pennies > 0:
        print(f"{pennies} {'Penny' if pennies == 1 else 'Pennies'}")

if __name__ == "__main__":
    main()

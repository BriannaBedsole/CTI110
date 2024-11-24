# Brianna Bedsole
# 11/24/2024
# P5HW
# In this assignment we will be making a Math quiz program that will test your addition or subtraction skills.

import random

def generate_numbers():
    """Generate two random numbers between 1 and 100"""
    return random.randint(1, 100), random.randint(1, 100)

def addition_quiz():
    """Function to handle addition problems"""
    num1, num2 = generate_numbers()
    correct_answer = num1 + num2
    guesses = 0
    
    print(f"    {num1}")
    print(f"+   {num2}\n")
    print("Enter Answer.")
    
    while True:
        try:
            guess = int(input())
            guesses += 1
            
            if guess == correct_answer:
                print("Congratulations!!!! Your answer is correct.")
                print(f"Number of guesses: {guesses}\n")
                break
            elif guess < correct_answer:
                print("Sorry, guess is too low.\n")
                print("Try again: ")
            else:
                print("Sorry, guess is too high.\n")
                print("Try again: ")
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

def subtraction_quiz():
    """Function to handle subtraction problems"""
    num1, num2 = generate_numbers()
    correct_answer = num1 - num2
    guesses = 0
    
    print(f"    {num1}")
    print(f"-   {num2}\n")
    print("Enter Answer.")
    
    while True:
        try:
            guess = int(input())
            guesses += 1
            
            if guess == correct_answer:
                print("Congratulations!!!! Your answer is correct.")
                print(f"Number of guesses: {guesses}\n")
                break
            elif guess < correct_answer:
                print("Sorry, guess is too low.\n")
                print("Try again: ")
            else:
                print("Sorry, guess is too high.\n")
                print("Try again: ")
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

def main():
    """Main program loop"""
    while True:
        print("MAIN MENU")
        print("--------------------")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit\n")
        print("Please choose one of the menu options: ", end="")
        
        try:
            choice = int(input())
            
            if choice == 1:
                addition_quiz()
            elif choice == 2:
                subtraction_quiz()
            elif choice == 3:
                print("Thank you for playing...")
                print("Bye!!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue

if __name__ == "__main__":
    print("Welcome to Math Quiz\n")
    main()

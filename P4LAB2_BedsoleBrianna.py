def main():
    while True:
        try:
            number = int(input("Enter an integer: "))
            
            if number < 0:
                print("This program does not handle negative numbers")
            else:
                for i in range(1, 13):
                    print(f"{number} * {i} = {number * i}")
        
        except ValueError:
            print("Please enter a valid integer")
            continue
        
        while True:
            run_again = input("Would you like to run the program again? ").lower()
            if run_again in ["yes", "no"]:
                break
            print("Please enter 'yes' or 'no'")
        
        if run_again == "no":
            print("Exiting program . . .")
            break

if __name__ == "__main__":
    main()

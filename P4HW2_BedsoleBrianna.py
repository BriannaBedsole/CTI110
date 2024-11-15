# Brianna Bedsole
# 11/10/2024
# P4HW2
# In this assignment we will be making a calculator that calculates an employees Hours, Pay Rate, OverTime, OverTime Pay, RegHour Pay, and Gross Pay. The calculator will then put out the total of all employee's information.

"""
PSEUDOCODE:
1. Create variables to keep track of:
   - How much paid for overtime
   - How much paid for regular time
   - Total money paid to employees
   - How many employees processed

2. Start the main program loop:
   a.) Ask for employee name
   b.) If name is "Done", the program will exit the loop
   c.) If not done the program will:
      - Get hours worked and pay rate
      - Calculate overtime hours (up to 40)
      - Calculate regular hours (up to 40)
      - Calculate overtime pay (overtime hours * 1.5 * pay rate)
      - Calculate regular pay (regular hours * pay rate)
      - Calculate gross pay (overtime pay + regular pay)
      - Display individual employee results
      - Add to running totals
      - Increment employee count
   
3. After loop ends, display final totals:
   - Total employees
   - Total overtime pay
   - Total regular pay
   - Total gross pay
"""

total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

while True:
    name = input("\nEnter employee's name or \"Done\" to terminate: ")
    
    if name.lower() == "done":
        break
        
    hours = float(input(f"How many hours did {name} work? "))
    pay_rate = float(input(f"What is {name}'s pay rate? "))
    
    overtime_hours = max(0, hours - 40)
    regular_hours = min(40, hours)

    overtime_pay = overtime_hours * 1.5 * pay_rate
    regular_pay = regular_hours * pay_rate
    gross_pay = overtime_pay + regular_pay

    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1
    
    print(f"\nEmployee name: {name}\n")
    print("Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay")
    print("-------------------------------------------------------------------------------")
    print(f"{hours:<14.1f} {pay_rate:<11.2f} {overtime_hours:<10.1f} ${overtime_pay:<12.2f} ${regular_pay:<11.2f} ${gross_pay:<.2f}")

print(f"\nTotal number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")

# Brianna Bedsole
# 11/2/2024
# P3HW2
# In this assignment we make a calculator that will calculate an employee's hours, pay rate, overtime, overtime pay, regular pay, and gross pay by entering the employee's name, number of hours worked, and pay rate.

employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    reg_hours_pay = 40 * pay_rate
else:
    overtime_hours = 0
    overtime_pay = 0
    reg_hours_pay = hours_worked * pay_rate

gross_pay = reg_hours_pay + overtime_pay

print('-' * 40)
print(f'Employee name: {employee_name}')
print('\nHours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay')
print('-' * 70)
print(f'{hours_worked:<14.1f}{pay_rate:<11.1f}{overtime_hours:<11.1f}${overtime_pay:<14.2f}${reg_hours_pay:<13.2f}${gross_pay:<10.2f}')

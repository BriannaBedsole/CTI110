#Brianna Bedsole
#10/5/2024
#P2HW2
#In this assignment we will make a program that can calculate your lowest grade, highest grade, sum, and average of grades. The program will ask the user what their grades are for the 6 modules and calculate them based on input. 

# Pseudocode:
# 1. Create empty list for the grades
# 2. Ask user to input grades for each module and append to the list
# 3. Calculate lowest grade using min() function
# 4. Calculate highest grade using max() function
# 5. Calculate sum of grades using sum() function
# 6. Calculate average by dividing sum by length of the list
# 7. Display results formatted as required

grades = []

grades.append(float(input("Enter grade for Module 1: ")))
grades.append(float(input("Enter grade for Module 2: ")))
grades.append(float(input("Enter grade for Module 3: ")))
grades.append(float(input("Enter grade for Module 4: ")))
grades.append(float(input("Enter grade for Module 5: ")))
grades.append(float(input("Enter grade for Module 6: ")))

lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)

print("------------Results------------")
print(f"Lowest Grade: {lowest_grade}")
print(f"Highest Grade: {highest_grade}")
print(f"Sum of Grades: {sum_of_grades}")
print(f"Average: {average_grade:.2f}")

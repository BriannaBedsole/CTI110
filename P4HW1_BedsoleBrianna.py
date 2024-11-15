# Brianna Bedsole
# 11/10/2024
# P4HW1
# In this assignment we will be making a calculator that calculates scores from 0-100. It gives out the Lowest score, Modified list, Scores average, and Grade.

"""
PSEUDOCODE:
1. Prompt user for number of scores to enter
2. Create empty list to store scores
3. For each score (using loop):
   a.) Ask user for score
   b.) While score is invalid (not between 0-100): It will output an error message and ask you to enter a valid score
   c.) Add valid score to list
4. Find and store the lowest score
5. Remove the lowest score from list
6. Calculate the average of remaining scores
7. Determine letter grade based on average
8. Display results:
   - Lowest score
   - Modified list
   - Average
   - Letter grade
"""

def get_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

num_scores = int(input("How many scores do you want to enter? "))

scores = []

for i in range(num_scores):
    while True:
        score = float(input(f"Enter score #{i+1}: "))
        
        if 0 <= score <= 100:
            scores.append(score)
            break
        else:
            print("\nINVALID Score entered!!!!")
            print("Score should be between 0 and 100")
            print(f"Enter score #{i+1} again: ")

lowest_score = min(scores)
scores.remove(lowest_score)
average = sum(scores) / len(scores)
grade = get_letter_grade(average)

print("\n--------------Results---------------")
print(f"Lowest Score  : {lowest_score}")
print(f"Modified List : {scores}")
print(f"Scores Average: {average:.2f}")
print(f"Grade         : {grade}")
print("----------------------------------")

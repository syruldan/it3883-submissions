# Program Name: Assignment2.py
# Course: IT3883/Section W01
# Student Name: Arvin Van
# Assignment Number: Assignment 2
# Due Date: 10/02/2026
# Purpose:
# This program reads student names and six grades from a file,
# calculates each student's average, sorts the students by
# average in descending order, and displays the results.
#
# Resources Used:
# Course notes, textbook, and personal coding practice.

# List to store student names and averages
student_grades = []

# Open the input file
with open("Assignment2input.txt", "r") as input_file:

    # Process each line in the file
    for line in input_file:

        # Split the line into fields
        fields = line.strip().split()

        # First field is the student name
        student_name = fields[0]

        # Remaining fields are grades
        scores = [float(score) for score in fields[1:]]

        # Calculate the average
        average_score = sum(scores) / len(scores)

        # Store the student's name and average
        student_grades.append((student_name, average_score))

# Sort by average in descending order
student_grades.sort(key=lambda student: student[1], reverse=True)

# Print the results
for student_name, average_score in student_grades:
    print(f"{student_name} {average_score:.2f}")
# zyDE 9.16.1: Iterating over a dictionary example: Gradebook statistics.
# Write a program that uses the keys(), values(), and/or items() dict methods to find statistics about the student_grades dictionary. Find the following:

# Print the name and grade percentage of the student with the highest total of points.
# Find the average score of each assignment.
# Find and apply a curve to each student's total score so the best student has 100% of the total points.

# student_grades contains scores (out of 100) for 5 assignments
student_grades = {
    'Andrew': [56, 79, 90, 22, 50],
    'Nisreen': [88, 62, 68, 75, 78],
    'Alan': [95, 88, 92, 85, 85],
    'Chang': [76, 88, 85, 82, 90],
    'Tricia': [99, 92, 95, 89, 99]
}

student_totals = {}

for name, grades in student_grades.items():
    total = sum(grades)
    student_totals[name] = total

print(student_totals)

best_student = max(student_totals, key=student_totals.get)
print(f"The best student is {best_student} with {student_totals[best_student]} points.")


num_assignments = len(next(iter(student_grades.values())))
for i in range(num_assignments):
    avg = sum(grades[i] for grades in student_grades.values()) / len(student_grades)
    print(f"Average for assignment {i+1}: {avg:.2f}")

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

Fail = range(0, 70)
Acceptable = range(71, 80)
Exceeds_Expectations = range(81, 90)
Outstanding = range(91, 100)

student_grades = {}

for student, score in student_scores.items():
    if score in Fail:
        student_grades[student] = "Fail"
    elif score in Acceptable:
        student_grades[student] = "Acceptable"
    elif score in Exceeds_Expectations:
        student_grades[student] = "Exceeds Expectations"
    elif score in Outstanding:
        student_grades[student] = "Outstanding"
        
for student, grade in student_grades.items():
    print(f"{student}: {grade}")

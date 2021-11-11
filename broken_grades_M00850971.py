exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))

exam_three = int(input("Input exam grade three: "))

grades = [exam_one, exam_two, exam_three]
total = 0
for i in grades:
    total = exam_one + exam_two + exam_three
avg = total / len(grades)


if avg > 89:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg >= 70 and avg < 80:
    letter_grade = "C"
elif avg >= 60 and avg < 70:
    letter_grade = "D"
else:
    letter_grade = "F"

print("Exam: ", (grades))
print("Average: ", round(float((avg))))
print("Grade: ", str((letter_grade)))

if letter_grade == "F":
    print("Student is failing.")
else:
    print("Student is passing.")

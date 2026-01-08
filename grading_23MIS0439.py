marks = int(input("Enter student marks: "))

if marks >= 90:
    grade = "Outstanding"
elif marks >= 80:
    grade = "Excellent"
elif marks >= 70:
    grade = "Good"
elif marks >= 60:
    grade = "Average"
elif marks >= 50:
    grade = "Fair"
else:
    grade = "Fail"

print("Grade:", grade)

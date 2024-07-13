print('the marks of five subjects')
subject_1 = 50
subject_2 = 70
subject_3 = 90
subject_4 = 65
subject_5 = 75

total = subject_1 + subject_2 + subject_3 + subject_4 + subject_5
average = total / 5.0

if average >= 90:
    grade = 'A'
elif average >= 80 and average < 90:
    grade = 'B'
elif average >= 70 and average < 80:
    grade = 'C'
elif average >= 60 and average < 70:
    grade = 'D'
else:
    grade = 'E'

print ("\nThe Total marks is:   \t", total, "/ 500.00")
print ("\nThe Average marks is: \t", average)
print ("\nThe Grade is:         \t", grade)
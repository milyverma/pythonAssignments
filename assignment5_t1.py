student_marks = {'Mily':98, 'Rachel':88, 'Theresa':76, 'Kevin':77, 'Adam':86}
student = input('Enter the student\'s name:').strip()

if student in student_marks:
    print(student+'\'s marks: ',student_marks[student])
else:
    print('Student not found.')
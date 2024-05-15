grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

list_students = sorted(students)
average_grades = [sum(student_grades) / len(student_grades) for student_grades in grades]
students_dict = dict(zip(list_students, average_grades))

print(students_dict)
print(type(students_dict))

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_students = list(students)
list_students.sort()
average_grades = [sum_grades/len_grades for sum_grades, len_grades in zip(map(int, list(map(sum, grades))), map(int, list(map(len, grades))))]
students_dict = dict(zip(list_students,average_grades))

print(students_dict)
print(type(students_dict))
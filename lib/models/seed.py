with open('seeds.sql', 'r') as sql_file:
    sql_script = sql_file.read()
# Then we can use execute script to run it
cursor.executescript(sql_script)
# Don't forget the commit
connection.commit()


# #here is where you create data and append to functions in model.py

# #here is creating/saving a student/donor-corresponsde to -- save_student and all_students in model
# print("Creating students")
# all_students = []
# for i in range(1000):
#     student = Student(
#         name = faker.name(),
#         emergency_phone= random.randint(1000000000,9999999999)
#     )
#     student.save_student()
#     all_students.append(student)

#     #
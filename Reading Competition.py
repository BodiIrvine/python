#this is where you enter how many students per class, how many classes total, and the reading goal
students_per_class = 30
amount_of_classes = 12
total_pages = 10000

#this the calculations take place
total_students = students_per_class * amount_of_classes
average_pages_per_student = total_pages // total_students

#here is where evreything is printed
print("There are " + str(total_students) + " students!")
print("To reach the goal of " + str(total_pages) + " pages, each student would need to read " + str(average_pages_per_student) + " pages.")



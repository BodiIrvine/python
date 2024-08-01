students_per_class = 30
amount_of_classes = 12
total_pages = 10000


total_students = students_per_class * amount_of_classes


average_pages_per_student = total_pages // total_students


print("There are " + str(total_students) + " students!")
print("To reach the goal of " + str(total_pages) + " pages, each student would need to read " + str(average_pages_per_student) + " pages.")



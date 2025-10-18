import matplotlib.pyplot as plt
students_name = ["Sanjay" , "Wasim" , "Rahul" , "Mohhamed" , "Virat" , "John" , "Ramesh" , "Aryan" , "Ajay" , "Priya" ]

students_marks = [ 34 , 56 , 60 , 70 , 58.5 , 56.5 , 67.5 , 49.5 , 28.5 , 50.5 ]

marks_percentage = []
for x in students_marks:
    res = (x/70)*100
    marks_percentage.append(res)

print(marks_percentage)
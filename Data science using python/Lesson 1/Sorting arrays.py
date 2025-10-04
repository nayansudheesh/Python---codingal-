import numpy as np

data_type = [("name" ,"S15"), ("class" , int ), ("height" , float) ]
student_details = [("James" , 5 , 42.5) , ("Martin" , 6 , 40.11), ("Paul", 7 , 45.04) , ("nail " , 6 , 52.5)]


students = np.array(student_details , dtype = data_type)
print(f"original array:{students}")
print("array sorted by height:")
print(np.sort(students, order="height"))
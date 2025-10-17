import pandas as pd
import numpy as np
print("program to enter and display the general data regarding your class")
class_data = {"name": [input("enter name"),input("enter name"),input("enter name"),input("enter name"),input("enter name")],
"number of days present": [int(input("enter num of days present")), int(input("enter num of days present")) , int(input("enter num of days present")) , int(input("enter num of days present")) , int(input("enter num of days present"))],
"number of days absent": [int(input("enter num of days absent")) , int(input("enter num of days absent")) , int(input("enter num of days absent")) , int(input("enter num of days absent")) , int(input("enter num of days absent"))],
"performance": [input("enter performance") , input("enter performance"), input("enter performance") , input("enter performance") , input("enter performance")] }

df = pd.DataFrame(class_data)
print(df)
import pandas as pd
import numpy as np

exam_data = {"name" : ["Kathernine" , "Dima" , "Virat" , "James" , "Emily" , "Michael" , "Kevin" , "Matthew" , "Laura" , "Ana"],
"score": [12.5 , 9 , np.nan , 16 , 17.5 , 20 , np.nan , 19.5 , np.nan ,7.5],
"attempts": [1 , 3 , 2 , 1 , 2 , 3 , 1 , 1 , 1 ,1 ] ,
"qualify" : ["yes" , "no" , "no" , "yes" , "yes" , "yes" , "no" , "yes" , "no" , "no"]}

labels =["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j"]

df = pd.DataFrame(exam_data , index=labels)
print("summary of the basic information about this dataframe and its data:")
print(df.info())

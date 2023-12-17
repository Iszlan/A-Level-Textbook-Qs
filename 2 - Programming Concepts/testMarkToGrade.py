import numpy as np
import pandas as pd


df = pd.read_excel('marks.xlsx', index_col=0)
marks = np.array(df)
print(marks)
length = marks.__len__()


i = 0

while i < length:
    mark = marks[i, 0]

    if mark >= 90:
        grade = "A*"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    elif mark >= 50:
        grade = "D - FAIL"
    else:
        grade = "F - FAIL"
    
    print(f'Student {i + 1} has a grade of {grade}.')

    i += 1

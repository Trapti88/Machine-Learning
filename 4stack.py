"Stack Project"

import pandas as pd

import matplotlib.pyplot as plt

data_frame = pd.read_csv("C:/Data/Data.csv")
#print(data_frame)

test1 = data_frame["Serial No."].tolist()
print(test1)

test2 = data_frame["SOP"].tolist()
print(test2)

test3 = data_frame["LOR"].tolist()
print(test3)

test4 = data_frame["CGPA"].tolist()
print(test4)

plt.stackplot("Serial No.,SOP,LOR,CGPA")
plt.xlabel("x- Axis")
plt.ylabel("y-Axis")
plt.title("stack Project")
plt.legend()
plt.show()
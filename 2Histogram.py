"Histogram Project"

import pandas as pd

import matplotlib.pyplot as plt

data_frame = pd.read_csv("C:/Data/Data.csv")
#print(data_frame)

test1 = data_frame["Serial No."].tolist()
print(test1)

test2 = data_frame["GRE Score"].tolist()
print(test2)

plt.hist(test1,test2, histtype="bar", rwidth=0.9)

plt.title("Getting Good Marks")
plt.xlabel("Serial No.")
plt.ylabel("GRE Score")
plt.legend()
plt.show()
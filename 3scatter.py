"Scatter Project"

import pandas as pd

import matplotlib.pyplot as plt

data_frame = pd.read_csv("C:/Data/Data.csv")
print(data_frame)

test1 = data_frame["Serial No."].tolist()
print(test1)

test2 = data_frame["Change of Admit"].tolist()
print(test2)

plt.scatter(test1,test2, label="Great Score")
plt.xlabel=("Serial No.")
plt.ylabel=("Change of Admit")
plt.title("Scatter Plots")
plt.legend()
plt.show()
"Adding Grid lines"

import pandas as pd

import matplotlib.pyplot as plt

data_frame = pd.read_csv("C:/Data/Data.csv")
#print(data_frame)

test1 = data_frame["Serial No."].tolist()
print(test1)

test2 = data_frame["GRE Score"].tolist()
print(test2)

plt.plot(test1,test2)
plt.xlabel("Serial No.")
plt.ylabel("GRE Score")
plt.minorticks_on()
plt.grid(b=True , which="major")
plt.show()
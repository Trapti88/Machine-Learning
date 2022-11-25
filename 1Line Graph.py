"""" This is  My Machine learning Project """

## Name - TRAPTI (Aliya) MESHRAM
## DATE - 25/11/2022

import matplotlib.pyplot as plt
import pandas as pd

data_frame = pd.read_csv("C:/Data/Data.csv")
#print(data_frame)

test1 = data_frame["Serial No."].tolist()
print(test1)

test2 = data_frame["TOEFL Score"].tolist()
print(test2)

plt.plot(test1,test2, label="Great Score")
plt.title("Getting Good Marks")
plt.xlabel("Serial No.")
plt.ylabel("TOEFT Score")
plt.legend()
plt.show()
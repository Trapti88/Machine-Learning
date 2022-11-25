"Pie Chart Project"

import matplotlib.pyplot as plt

work= ["Sleeping", "Exercise", "Music", "Coding", "Eating"]

time = [8,2,2,5,1]

plt.pie(time, labels=work, explode=(0,0,0,0.3,0) ,autopct="%0.2f%%")
plt.title("Daily Rutine")
plt.legend()
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["A", "B", "C", "D"],
    "Marks": [80, 90, 70, 85]
}

df = pd.DataFrame(data)
print(df)
plt.plot(df["Name"], df["Marks"], marker='o')

plt.title("Student Marks")
plt.xlabel("Name")
plt.ylabel("Marks")

plt.show()

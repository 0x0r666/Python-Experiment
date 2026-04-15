# Aim: program to implement numpy and pandas

import numpy as np
import pandas as pd
# Numpy 
arr = np.array([10, 20, 30, 40, 50])
print("NumPy Array:", arr)

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))

# Pandas
data = {
    "Name": ["Amit", "Rahul", "Neha"],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data)

print("\nPandas DataFrame:")
print(df)

print("\nColumn Names:")
print(df["Name"])

print("\nAverage Marks:", df["Marks"].mean())


#Aim: Write a program to demonstrate list & related functions in python.


# Create List
Network = ["5G","upto 10GBPS","6G","1m/s","VRIAR","4G","Transport","Smart","Factories","New Radio","mmwave","sub-6GHZ","Spectrum","Frequency","INR"]

# Slicing
print("Slicing:", Network[1:5])

# Append
Network.append("Ultra-reliable")

# Insert / Modify
Network[3] = "Throughput"
print("After Insert/Modify:", Network)

# Remove
Network.remove("INR")
print("After Remove:", Network)

# Index
L = Network.index("5G")
print("Index of 5G:", L)

# Copy
Network1_copy = Network.copy()
print("Copied List:", Network1_copy)

# Concatenation
conca = Network1_copy + Network
print("Concatenated List:", conca)

# Looping using for
print("\nFor Loop Output:")
for item in Network[:5]:
    print(item)

# While loop
print("\nWhile Loop Output:")
i = 0
while i < len(Network):
    print(Network[i])
    i += 1

# Clear
temp = Network1_copy
temp.clear()
print("\nAfter clear:", temp)
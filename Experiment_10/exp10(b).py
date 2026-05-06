import matplotlib.pyplot as plt

# Sample data
names = ["A", "B", "C", "D"]
marks = [80, 90, 70, 85]

# LineGraph
plt.plot(names, marks)
plt.title("Line Graph")
plt.show()

# BarGraph
plt.bar(names, marks)
plt.title("Bar Graph")
plt.show()

# PieChart
plt.pie(marks, labels=names, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()

# Histogram
plt.hist(marks)
plt.title("Histogram")
plt.show()
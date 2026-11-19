import os
import matplotlib.pyplot as plt

dates = []
products = []
sales = []

# Get path of sales.csv from same folder as this script
file_path = os.path.join(os.path.dirname(__file__), "sales.csv")

# Read CSV file
with open(file_path, "r") as file:
    data = file.read()
    lines = data.strip().split("\n")

    for row in lines[1:]:
        values = row.split(",")

        dates.append(values[0])
        products.append(values[1])
        sales.append(int(values[2]))

# Display data
print("Dates:", dates)
print("Products:", products)
print("Sales:", sales)

# Line Graph
plt.figure(figsize=(8, 5))
plt.plot(dates, sales, marker='o')
plt.title("Retail Sales")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(dates, sales, color="skyblue")
plt.title("Product Sales")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()
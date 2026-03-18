# This code analyzes heart rate data from a survey, categorizes the heart rates into low, normal, and high, and visualizes the distribution of these categories using a pie chart.
import matplotlib.pyplot as plt
hearts_rate = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]
print("there are", len(hearts_rate), "participatents in the survey")
print("the average heart rate is",round(sum(hearts_rate) / len(hearts_rate), 2))
category = {"low": 0, "normal": 0, "high": 0}
for heart in hearts_rate:
    if heart < 60:
        category["low"] += 1
    elif heart <= 120:
        category["normal"] += 1
    else:
        category["high"] += 1
print("the number of low heart rate is", category["low"])
print("the number of normal heart rate is", category["normal"])
print("the number of high heart rate is", category["high"])

# This part is to avoid the situation where there are multiple categories with the same maximum value, we will print all categories that have the maximum value.
max_value = max(category.values())
for cate in category:
    if category[cate] == max_value:
        print("the most common heart rate category is", cate)

# Plotting the heart rate categories
plt.pie(category.values(), labels=category.keys(), autopct="%1.1f%%")
plt.title("Heart Rate Categories")
plt.show()
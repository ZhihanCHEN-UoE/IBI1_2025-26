# Pseudocode:
# 1) Initialize starting infected count and daily growth rate.
# 2) Track the current day and a list of daily totals.
# 3) While total infected is below class size, grow by the rate each day.
# 4) Record the day and infected count, then print summary and log.

# a = infected students on day 1; b = daily growth rate
a = 5
b = 0.4
c = a # current infected students
cnt = 1 # current day count
information = [['day1', 5.0]] # list of [day_label, infected_count]
while c < 91:
    c = c*(1+b)
    cnt += 1
    information.append(["day"+str(cnt),round(c,2)])
print("it takes",cnt,"days to infect all the student in ibi1 class")
print("daily information is ",information)
# result of this programme: it takes 10 days to infect all the student in ibi1 class
#it takes 10 days to infect all the student in ibi1 class
#daily information is  [['day2', 7.0], ['day3', 9.8], ['day4', 13.72], ['day5', 19.21], ['day6', 26.89], ['day7', 37.65], ['day8', 52.71], ['day9', 73.79], ['day10', 103.31]]

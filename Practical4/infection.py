# a = first day illness student and b = growth rate
a = 5
b = 0.4
c = a #c is current infected student
cnt = 1
information = [['day1', 5.0]]
while c < 91:
    c = c*(1+b)
    cnt += 1
    information.append(["day"+str(cnt),round(c,2)])
print("it takes",cnt,"days to infect all the student in ibi1 class")
print("daily information is ",information)
# result of this programme: it takes 10 days to infect all the student in ibi1 class
#it takes 10 days to infect all the student in ibi1 class
#daily information is  [['day2', 7.0], ['day3', 9.8], ['day4', 13.72], ['day5', 19.21], ['day6', 26.89], ['day7', 37.65], ['day8', 52.71], ['day9', 73.79], ['day10', 103.31]]

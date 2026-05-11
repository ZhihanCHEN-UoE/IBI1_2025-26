a = 5080000 # population in 2004
b = 5330000 # population in 2014
c = 5550000 # population in 2024
d = b - a # calculate the growth between 2004 and 2014
e = c - b # calculate the growth between 2014 and 2024
if d > e: # compare
    print("d is larger, which means population growth is decelerating")
elif d == e:
    print("they are equal")
else:
    print("e is larger, which means population growth is accelerating")
# Based on current values, d is larger than e.

results = []
labels = ["X and Y", "X or Y", "not (X and Y)", "not (X or Y)"]

for X in [True, False]:
    for Y in [True, False]:
        values = [X and Y, X or Y, not (X and Y), not (X or Y)]
        results.append({"X": X, "Y": Y, "results": dict(zip(labels, values))})

print(results)
# All True/False combinations for X and Y are tested above.
a = 5080000
b = 5330000
c = 5550000
d = b-a
e = c-b
if d>e:
    print("d is larger, that means population growth decelerating")
elif d == e:
    print("they are equal")
else:
    print("e is larger,that means population growth accelerating")

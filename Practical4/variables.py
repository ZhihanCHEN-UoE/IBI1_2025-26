a = 5080000 #population in 2004
b = 5330000 #population in 2014
c = 5550000 #population in 2024
d = b-a #calculate the growth between 2004 and 2014"
e = c-b #calculate the growth between 2014 and 2024"
if d>e: #compare
    print("d is larger, that means population growth decelerating")
elif d == e:
    print("they are equal")
else:
    print("e is larger,that means population growth accelerating")

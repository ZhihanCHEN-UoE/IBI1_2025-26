age = int(input("age (in years)"))
while age >= 100:
    print("please input a valid age!")
    age = int(input("age (in years)"))
weigh = int(input("weight (in kg)"))
while weigh <= 20 or weigh >= 80:
    print("please input a valid weigh!")
    weigh = int(input("weight (in kg)"))
genger = input("gender, for male please input 0, for female please input 1")
gender = [1,0.85][gender]
cr = input("Cr")
rate = ((140-age)*weigh)/(72*cr)*gender
print(rate)

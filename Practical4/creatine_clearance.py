'''
Pseudocode
1. Ask user to enter age (repeat until age is 0-100)
2. Ask user to enter weight (repeat until weight is 21-79 kg)
3. Ask user to enter gender (0=male, 1=female) → set coefficient (male=0.85, female=1)
4. Ask user to enter Cr value
5. Calculate rate = ((140 - age) × weight / (72 × Cr)) × coefficient
6. Print the calculated rate
'''

age = int(input("age (in years)"))
while age >= 100 or age < 0:
    print("please input a valid age!")
    age = int(input("age (in years)"))
weigh = int(input("weight (in kg)"))
while weigh <= 20 or weigh >= 80:
    print("please input a valid weigh!")
    weigh = int(input("weight (in kg)"))
gender = int(input("gender, for male please input 0, for female please input 1"))
gender = [1,0.85][gender]
cr = float(input("Cr"))
while cr <= 0 or cr > 100:
    print("please input a valid Cr!")
    cr = float(input("Cr"))
rate = ((140-age)*weigh)/(72*cr)*gender
print(rate)

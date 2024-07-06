#Adhvika
a=float(input("Enter Weight "))
b=float(input("Enter Height "))
BMI=a/b**2
if BMI<18.:
    print("Underweight")
if 18.5 < BMI < 24.9:
    print("Normal Weight")
if 25 < BMI < 29.9:
    print("Over Weight")
if BMI > 30:
    print("Obsity")


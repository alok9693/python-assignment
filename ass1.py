# Question1

P = int(input("Enter First Number : "))
Q = int(input("Enter Second Number : "))
R = int(input("Enter Third Number : "))
S = P + Q + R
average = S / 3
print("Average of three number is : ", average)

# Question2

G_I = int(input("Enter the Gross Income : "))
D = int(input("Enter Dependent : "))
S_D = 10000
D_D_A = D * 3000
Taxable_Income = G_I - S_D - D_D_A
Tax = float((20 / 100) * (Taxable_Income))  # Tax is 20% of Taxable_Income
print("Your income tax : ", Tax)

# Question3

sid=input("Enter SID:")
name=input("Enter name:")

gender=input("Enter Gender:")

course=input("Enter course name:")
cgpa=float(input("Enter CGPA"))

student=[sid,name,gender,course,cgpa]

print(student)

# Question4

A = int(input('marks of studentA: '))
B = int(input('marks of studentB: '))
C = int(input('marks of studentC: '))
D = int(input('marks of studentD: '))
E = int(input('marks of studentE: '))
list = [A,B,C,D,E]
print(list)

# question 5a

color=['red','Green', "White",'Black', 'Pink', 'Yellow']
color.pop(3)
print(color)

# question 5b

color=['red','Green', "White",'Black', 'Pink', 'Yellow']
color[color.index("Black")]="Purple"; color[color.index("Pink")]="Purple"
print(color)

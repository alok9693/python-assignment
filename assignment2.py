#Que1
#Program to input given string “Python is a case sensitive language” and use string related functions.
print("Que1")
p="Python is a case sensitive language"
print(p)
#(a)
print("\nPart a")
print("length of the string is", len(p))
#(b)
print("\nPart b")
print("The string in reverse order is:", p[::-1])
#(c)
print("\nPart c")
c=p[10:27]
print(c)
#(d)
print("\nPart d")
a=p.replace("a case sensitive", "object oriented")
print("After replacing in input string:", a)
b=c.replace("a case sensitive", "object oriented")
print("After replacing in new string:", b)
#(e)
print("\nPart e")
print(p.index("a"))
#(f)
print("\nPart f")
print(p.replace(" ",""))
#End of program 1
print("\n")


#Que2
name="alok kumar vishwakarma"
SID=21104127
department_name="EE"
CGPA="9.5"

print("Hey,%s Here!"%(name))
print("My SID is %d"%(SID))
print("I am from %s department and my CGPA is %s"%(department_name,CGPA))


#Que3
#Program about using bitwise operators
print("Que3")
a=56
b=10
print("a=", a)
print("b=", b)
print("\nPart a")
print("a&b:", a&b)
print("\nPart b")
print("a|b:", a|b)
print("\nPart c")
print("a^b:", a^b)
print("\nPart d")
print("Left shifting both a and b with 2 bits:", a<<2, b<<2)
print("\nPart e")
print("Right shifting a with 2 bits and b with 4 bits:", a>>2, b>>4)
print("\n")


#Que4
x=int(input("Give a number:"))
y=int(input("Give a number:"))
z=int(input("Give a number:"))

if(x>y):
    if(x>z):
        print(x,"is greatest number")
    else:
        print(y,"is greatest number")
else:
    if(y>z):
        print(y,"is greatest number")
    else:
        print(z,"is greatest number")


#Que5
user_input=input("Give a word:")
if("name"in user_input):
    print("Yes")
else:
    print("No")


#Que6
a=int(input("Give a number:"))
b=int(input("Give a number:"))
c=int(input("Give a number:"))

if(a+b>c and b+c>a and a+c>b):
    print("The triangle is possible")
else:
    print("The triangle is not possible")

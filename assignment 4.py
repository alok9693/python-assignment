#QUES 1
print("ANS 1")
def TowerOfHanoi(n , fromRod, toRod, middleRod):
	if n == 0:
		return
	TowerOfHanoi(n-1, fromRod, middleRod, toRod)
	print("Move disk",n,"from rod",fromRod,"to rod",toRod)
	TowerOfHanoi(n-1, middleRod, toRod, fromRod)
n = 3
TowerOfHanoi(n, 'A', 'C', 'B')
print("\n")

#QUES 2
print("ANS 2")
from math import factorial, remainder
from tracemalloc import start
n=int(input('Enter the size of pascals triangle '))

print("USING LOOPS")

for i in range(n):
	for j in range(n-i+1):
		print(end=" ") #spacing

	for j in range(i+1):
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")	# nCr = n!/((n-r)!*r!)
	print()	# for printing new line
print("\n\n")

print("USING RECURSSIONS")

def pascal_triangle(n,original_length=n):
    if n == 0:
        return
    pascal_triangle(n-1,original_length)
    # spacing
    print('  '*(original_length-n), end='')

    #first number is always 1
    start = 1
    for i in range(1, n+1):

        print(start, end ='   ')

        #by Binomial Coefficient
        start = start * (n - i) // i
    print()
pascal_triangle(n)
print("\n")

#QUES 3
print("ANS 3")
print("part(a)")
def fun(a, b):
    quotient = a // b
    remainder = a % b
    print("The quotient is:", quotient)
    print("The remainder is", remainder)
    result = [quotient, remainder]
    return result

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
result = fun(a, b)
print(result)
print("Callable:", callable(fun))

print("part(b)")
print("a is zero:", a == 0)
print("b is zero:", b == 0)
print("quotient is zero:", result[0] == 0)
print("remainder is zero:", result[1] == 0)
if (a == 0):
    print("a is zero")

print("part(c)")
alist = []
for i in result:
    if i > 4:
        alist.append(i)
print("The values greater than 4 are:", alist)

print("part(d)")
aset = set(alist)
print(aset)

print("part(e)")
immutable_set = frozenset(aset)
print("The required immutable set", immutable_set)

print("part(f)")
maxval = 0
for i in immutable_set:
    if i > maxval:
        maxval = i
print("The required max value is:", maxval)
print("The required hash value is:", hash(maxval))
print("Done")

#QUES 4
print("ANS 4 ")
class Student:
    def __init__(self, student,roll_number):
        self.name = student
        self.roll_number = roll_number

    def __del__(self):
        print("Object destroyed")

#creating object
student1 = Student("ALOK KUMAR VISHWAKARMA", 21104127)
print("Object is created")
#printing the assigned value
print(f"The name of the student it {student1.name} and SID is {student1.roll_number}.")
#deleting the object
del student1
print("\n")

#QUES 5
print("ANS 5")
class EmployeeDetails:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def func(self):
        print("Name of employee is:", self.name, "and salary is:", self.salary)

Emp_1 = EmployeeDetails("Mehak", 40000)
Emp_2 = EmployeeDetails("Ashok", 50000)
Emp_3 = EmployeeDetails("Viren", 60000)
Emp_1.func()
Emp_2.func()
Emp_3.func()

print("part(a)")
# updating salary of Mehak
Emp_1.salary = 70000
print("The updated salary of Mehak is:", Emp_1.salary)

print("part(b)")
# deleting the record of Viren
del Emp_3
print("The record of Viren has been successfully deleted")
print("Done")

#QUES 6
print("ANS 6")
# we will use the concept of anagrams
def anagram(word):
    if len(word) == 1:
        return [word];
    partial_words = anagram(word[1:])
    char = word[0]
    mylist = []
    for perm in partial_words:
        for i in range(len(perm) + 1):
            mylist.append(perm[:i] + char + perm[i:])
    return mylist

George_word = input("Enter the word by George:")
Possible_words = anagram(George_word)
Barbie_word = input("Enter word by Barbie:")
print("Possible Words are:", Possible_words)
print("If Barbie's word is present in the list , then their friendship is real.")

if Barbie_word in Possible_words:
    print("Your Friendship is real.")
else:
    print("Your Friendship is fake.")
print("Done")

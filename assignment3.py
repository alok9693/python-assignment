Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#question 1
print("question 1")
#taking input from user
sentence = input("Please give an input- ")
sentence=sentence.lower().strip()
i=0
#defining empty dictionary to use later to store element
dict={}

#checking if the string input is a word or a sentence
if " " not in sentence:
     #searching for common elements
     while i<len(sentence):
          counter=0
          k=0
          while k<len(sentence):
               if sentence[i]==sentence[k]:
                    counter=counter+1
                    k=k+1
               else:
                    k=k+1
          #storing the values in dictionary
          dict[f"{sentence[i]}"]=counter
          i=i+1

else:
     #making a list of words using split method
     list = str.split(sentence)
     #searching for common words
     while i<len(list):
          counter=0
          k=0
          while k<len(list):
               if list[i]==list[k]:
                    counter=counter+1
                    k=k+1
               else:
                    k=k+1
                    #storing the pairs in dictionary
          dict[f"{list[i]}"]=counter
          i=i+1
#Printing the final result
print("Total occurances")
for key,value in dict.items():
    print(f"{key}-{value}")

# question 2
print("question 2")
# Condition for leap year
year = int(input("Input a year: "))
1800 <= year <= 2025
if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

# Condition for months
month = int(input("Input a month [1-12]: "))
if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30

# Condition for day
day = int(input("Input a day [1-31]: "))
if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))

#question 3
print("question 3")
my_list = [3, 9, 10]
print("The list is")
print(my_list)
print("The resultant tuple is : ")
my_result = [(val, pow(val, 2)) for val in my_list]
print(my_result)

#question 4
print("question 4")
print("enter your grade point")
gradepoint=int(input())
if gradepoint==4:
    print("Your Grade is 'D' and Poor Performance")
elif gradepoint==5:
    print("Your Grade is 'C' and Below Average Performance")
elif gradepoint==6:
    print("Your Grade is 'C+' and Average Performance")
elif gradepoint==7:
    print("Your Grade is 'B' and Good Performance")
elif gradepoint==8:
    print("Your Grade is 'B+' and Very Good Performence")
elif gradepoint==9:
    print("Your Grade is 'A' and Excellent Performence")
elif gradepoint==10:
    print("Your Grade is 'A+' and Outstanding Performence")
else:
    print("error")

#question 5
print("question 5")
n = 6
for i in range(n):
    # printing spaces
    for j in range(i):
        print(' ', end='')
    # printing alphabet
    for j in range(2*(n-i)-1):
        print(chr(65 + j), end='')
    print()

#question 6
print("question 6")
condition=True
#Defining dictionary to store the values
Dictionary={}
prompt="y"
while condition:
    if prompt.lower()=="y":
        SID=int(input("Please Enter SID of Student:- "))
        name=input("Please enter the name of the Student:- ")
        Dictionary[SID]=name
        prompt= input("If you want to enter more details press Y/N:- ")
        condition = True
    else:
        condition = False

print("Part a")
for key,value in Dictionary.items():
    print(f"{key} is {value}")
print("")

print("Part b")
Val_sort_dict= sorted(Dictionary.values())
print(f"value sorted dictionary is {Val_sort_dict}")
print("")

print("Part c")
Key_sort_dict= sorted(Dictionary.keys())
print(f"Keys sorted dictionary is {Key_sort_dict}")
print("")

print("Part D")
SID_tbf=int(input("Please enter the student's SID whose detail you need- "))
if SID_tbf in Dictionary.keys():
    print(f"Name of the required student is {Dictionary[SID_tbf]}")
else:
    print("The SID is not present in the given Data")
print("")

#question 7
print("question 7")
number=int(input("Total elements of Fibonacci sequence that you want(must be greater than 1)- "))
a_n1=1
a_n2=0
n=0
#initializing sum with first two terms
sum=a_n1+a_n2

#printing the initial two terms as the recursion is not valid on them
print(f"Fibonnaci sequence with {number} terms")
print(a_n2)
print(a_n1)

#Printing the remaining fibonnaci terms
while n<number-2:
    a_n=a_n2+a_n1
    a_n2=a_n1
    a_n1=a_n
    print(a_n)
    n=n+1
    sum+=a_n
average=sum/number
print(f"Average of total {number} terms of sequence is {average}")
print("END")

#question8
print("question 8")
set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}
#(a.)
list=[]
for a in set1:
  if a not in set2:
        list.append(a)
for a in set2:
  if a not in set1:
      list.append(a)
s=set(list)
print(f"a.{s}")

#(b.)
list=[]
for a in set1:
    if a not in set2 and a not in set3:
        list.append(a)
for a in set2:
    if a not in set1 and a not in set3:
        list.append(a)
for a in set3:
    if a not in set1 and a not in set2:
        list.append(a)
s=set(list)
print(f"b.{s}")

#(c.)
list = []
for a in set1:
    if a in set2 and a not in set3:
        list.append(a)
for a in set2:
    if a in set1 and a not in set2:
        list.append(a)
for a in set3:
    if a in set1 and a not in set2:
        list.append(a)
s=set(list)
print(f"c.{s}")

#(d.)
list=[]
for i in range (1,11):
    if i not in set1:
        list.append(i)
s=set(list)
print(f"d.{s}")

#(e.)
list=[]
for i in range(1,11):
    if i not in set1 and i not in set2 and i not in set3:
        list.append(i)
s=set(list)
print(f"e.{s}")
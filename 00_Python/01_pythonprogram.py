# --------------------------------------------
# INPUT IN PYTHON------------------------------------
# --------------------------------------------
# light=input("what is the colour of light:")

# if light=="red":
#     print("STOP")
# elif light=="yellow":
#     print("LOOK")
# elif light=="green":
#     print("GO")
# else:
#     print("The light is broken....")

#===========================================================

# marks=int(input("marks:="))     
# if marks>=90:
#     print("A")
# elif (marks>=80 and marks<90):
#     print("B")
# elif(marks>=70 and marks<80):
#     print("C")
# else:
#     print("D")

#===========================================================

# food =input("food:")
# eat="yess" if food=="cake" else "no"
# print(eat,"eat",food)

#-============================================================
# you can select the desired thing to be made into comment 
# then press ctrl+/


# ARITHMETIC OPERATORS----------------------------------
# a=5
# b=2

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)    # remainder
# print(a**b)    # a^b

#==========================================================

#RELATIONAL OPERATORS-----------------------------------
# a=50
# b=20
# print(a==b)  # False
# print(a!=b)  #True
# print(a>=b)  #True
# print(a>b)  #True 
# print(a<=b)   #False
# print(a<b)    #False

#========================================================

#ASSIGNMENT OPERATOR---------------------------------------
# num=10
# num=num+10   # num=10+10 => 20 or (num+=10)
# # or num+=10
# print(num)

#===========================================================

#LOGICAL OPERATORS---------------------------------------
# a=50
# b=30
# print(not False)
# print(not (a>b))

# val1=True
# val2=True
# print("and operator:",val1 and val2)
# print("or operator:", val1 or val2)

#===========================================================

#TYPE CONVERSION----------------------------------
# a,b=1,2
# sum=a+b
# print(sum)

# a,b=1,"2"
# sum=a+b
# print(sum)  # type error as one is int and one is str


# a="hello"+"world"
# print(a)  #  concatenation

# str="college"
# len1=len(str)
# print(len1)
# str="bharat college"
# print(str[4:9])
# print(str[4:]) #[5:len(str)]
# print(str[:4])  #[0:4]
# print(str[-7:-1])

#=========================================================
#STRING FUNCTIONS----------------------------------------
# str="i am studying python from apnacollege"
# print(str.capitalize())  # to capitalize first letter only tempororily
# str=str.capitalize() # to capitalize permanently
# print(str)
# print(str.replace("python","javascript"))
# print(str.find("o"))
# print(str.count("o"))
# print(str.endswith("ege"))

#NESTING---------------------------------------------------
# age=int(input("enter the age:"))
# if age>=18:
#     if age>=80:
#         print("cannot drive")
#     else:
#         print('can drive')
# else:
#     print ("cannot drive")

#EVEN AND ODD NO.
# 80

#LARGEST NUMBER AMONG THREE-----------------------------
# a=int(input("enter the first number:"))
# b=int(input("enter the second number:"))
# c=int(input("enter the third number:"))
# if a>=b and a>=c:
#     print("first number is larger:",a)
# elif b>=c:
#     print("second number is largest",b)
# else:
#     print("third number is largest",c)

#=========================================================

#LIST IN PYTHON---------------------------------
#--------------- list is mutable 

# marks=[94.4,98,78,60,89]
# print(marks)
# print(marks[1:4])  # list slicing - similar to string slicing

# LIST METHODS------
#---------------
# list=[2,1,3,4]
# list.append(6) #adds one element in end
# print(list) 
# list.sort() # sorts in ascending order
# print(list)  
# list.sort(reverse=True) #sorts in descending
# print(list) 
# list.reverse() #reverses list
# print(list) 
# list.insert(2,9) # list.insert(index,element)
# print(list)
# list.remove(1)
# print(list)

#=======================================================

#TUPLES IN PYTHON---------------
#----------------- immutable
# tuple=("bike", 10,80,10)
# print(tuple)
# print(type(tuple))
# print(tuple[0])
# print(tuple.count(10))
# -----------------------------------------------------------
#write a program to ask the user about their 
 #3 favorite movies and store them in a list.

# m1=input("enter the name of first fav movie:")
# m2=input("enter the name of second fav movie:")
# m3=input("enter the name of third fav movie:")
# list=[m1,m2,m3]
# print(list)
# --------------------------------------------------------------
# write the program to check if a list contains 
# PALINDROME of elements.[hint- use copy()]
# palindrome - a word, sentence, verse, or even number that reads
#               the same backward or forward
# list=[1,2,1]
# list1=[1,2,3]
# copy_list=list.copy() # make a copy of "list"
# copy_list.reverse() # reverse the copy 
# if copy_list==list: # compare reversed copy to original
#     print("palindrome")
# else:
#     print("not palindrome")

#     #ALSO

# my_list=[1,2,1]                 # this version avoids copying and is more 
#                                  #pythonic using slicing ([::-1] reverses the list)
# if my_list==my_list[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")

#====================================================

#DICTIONARY IN PYTHON.---------------
#--------------------- mutable
# info={"key":"value",
#       "name":"Himani",
#       "learning":"python",
#       "age":"18"}
# print(info)
# print(info["learning"])

# DICT METHODS----
#----------------
# info={"key":"value",
#       "name":"Himani",
#       "learning":"python",
#       "age":"18"}
# print(info.keys())  # returns all the keys
# print(info.values())  #returns all values
# print(info.items())  # returns all (key,val) pairs a tuples
# print(info.get("name"))  # returns the key according to value

# dictionary={"cat":"a samll animal",
#             "table":["a piece of furniture","list of facts and figures"]}
# print(dictionary)
# ----------------------------------------------------------------
#write a program toenter marks of 3 subjects from the 
# user and store them in a dictionary.
# start with an empty dictionary and add one by one.
# use subject name as key and marks as value
# marks={}
# x=int(input("enter phy:"))
# marks.update({"phy":x})

# y=int(input("enter chem:"))
# marks.update({"chem":y})

# z=int(input("enter maths:"))
# marks.update({"maths":z})
# print(marks)


#==================================================================

#SETS IN PYTHON---------
#---------------
# collection={1,2,3,4,"hello"}
# print(collection)

# # null_set=set()
# #SET METHODS--------

# collection.add(78) # adds and element in the collection
# collection.remove(1)
# #collection.clear()  # empties the set
# collection.pop() # removes a random value
# print(collection)
#print(collection.pop()) # pops a random value out of set

# set1={1,2,3}
# set2={2,3,4}
# print(set1.union(set2))
# print(set1.intersection(set2))

#===> you are given a list of subjects for students.
#  assume one classroomis required for 1 subject. 
# howmany classrooms are needed by all students.???
#"python", "java","c++","python","javascript","java","python","java","c++","c"
# subjects={"python", "java","c++","python",
#           "javascript","java","python","java","c++","c"}
# print(subjects) # even if the thing is repeated it gives unique value only
# print(len(subjects))

#==========================================================
# LOOPS IN PYTHON------
#-----------------
# #while loops
# count = 1                     
# while count<=5:
#     print("hello",count)
#     count+=1
# print(count)
# #print numbers from 1 to 100.
# i=1
# while i<=100:
#     print(i)
#     i+=1
#------------------------------------
# #print numbers from 100 to 1.
# i=100
# while i>=1:
#     print(i)
#     i-=1
#-------------------------------------
# #print the multiplication table of number n.
# i=1
# while i<=10:
#     print(3*i)
#     i+=1
#--------------------------------------
# i=1
# while i<=10:
#     print(17*i)
#     i+=1
#--------------------------------------------
#print the elements of the following list using a loop:
#[1,4,9,16,25,36,49,64,81,100]
#        index=0,1,2,3........len(list)-1.
# nums=[1,4,9,16,25,36,49,64,81,100]
# idx=0
# while idx<len(nums):
#     print(nums[idx])# nums[0], nums[1], nums[2]...
#     idx+=1 
#-----------------------------------------------
#search for a number x in this tuple using loop.
# nums=(1,4,9,16,25,36,49,64,81,100)
# x=36
# i=0
# while i<len(nums):
#     if(nums[i]==x):
#         print("Found at index",i)
#         break
#     else:
#         print("not found")
#     i+=1
# print("end of loop")
#-------------------------------------
#BREAK AND CONTINUE
# i=0
# while i<=5:
#     print(i)
#     if i==3:
#         break
#     i+=1
# print("end of loop")
#-------------------------------------
# i=0
# while i<=5:
#     if i==3:
#         i+=1
#         continue
#     print(i)
#     i+=1
#-------------------------------------
# i=0
# while i<5:
#     if (i%2==0):
#         i+=1

#     print(i)
#     i+=1
#---------------------------------------
# i=0
# while i<5:
#     if (i%2!=0):
#         i+=1

#     print(i)
#     i+=1
#--------------------------------------
# i=0
# while i<=10:
#     if i%2==0:
#         print(i)
#     i+=1 # important: increase i in each loop
# -------------------------------------------------
#FOR LOOPS
# val=[1,2,3,4,5,6,7,8,9,10]
# for i in val:
#     print(i)
# ---------------------------------------------------
# str="bharatcollege"
# for i in str:
#     if(i=='e'):
#         print("e found")
#         break
#     print(i)
# print("end")
# -------------------------------------------------------
#search x in tuple using for loop.
# val=(1,4,9,49,25,36,49,64,49,100)
# x=49
# idx=0
# for i in val:
#     if i==x:
#         print("number found at index",idx)
#         break # use break if you want only at first index else remove it 
#     idx+=1
# -----------------------------------------------------------
# val=(1,4,9,49,25,36,49,64,49,100)
# x=49
# idx=0
# for i in val:
#     if i==x:
#         print("number found at index",idx)
#          # don't use break if you want every index at which x is present
#     idx+=1
# --------------------------------------------------------------
#RANGE()
#range functions returns a sequence of numbers starting from 0 by default, and 
# increments by 1(bydefault)and stops before a specifies number
#range(start,stop,step)

# for i in range(5):
#     print(i)

# for i in range(20):
#     print(i)

# for i in range(1,5):
#     print(i)

# for i in range(2,10,2):
#     print(i)
# ----------------------------------------------------------
# print number from 1 to 100:
# for i in range(1,101):
#     print(i)
# ------------------------------------------------------------
# #print number from (100 to 1)
# for i in range(100,0,-1): # starts from 100 stops at number
#                           # less then stop value and gap is of -1
#     print(i)
# -----------------------------------------------------------------
# multiplication table of number n
# for i in range(1,11):
#     print(9*i)

# for i in range(1,11):
#     print("8 *",i,"=",8*i)
# ------------------------------------------------------------
#PASS:- pass is a null statement that does nothing.
#  it is used as a placeholder for future code
# for i in range(5):
#     pass
# print("work done!!")
# ---------------------------------------------------------------
# sum of n natural numbers.
# => using for loop
# n=5
# sum=0
# for i in range(1,n+1):
#     sum+=i
    
# print("total sum:", sum)
#=> using while loop
# n=7
# sum=0
# i=1
# while i<=n:
#     sum=sum+i 
#     i+=1
# print("Total sum=",sum)
# -------------------------------------------------------------------
#write the program to write factorial of n numbers.
# n=4
# fact=1 # to calculate factorial always initialize the variable with 1
# for i in range(1,n+1):
#     fact*=i

# print("factorial=",fact)

# #using while loop
# n=5
# fact=1
# i=1                   # i need to be defined when using while loop but not in for loop
# while i<=n:
#     fact*=i
#     i+=1
# print("factorial=",fact)

# ====================================================================

#FUNCTIONS IN PYTHON---------
#-------------------
# def func_name(param1,param2): # function defination
#     #some work
#     return val
#func_name(arg1,arg2) # function call
# def sum(a,b):
#     s=a+b
#     return s
# print(sum(2,3))
# -------------------------------
# def calc_sum(a,b):
#     sum=a+b
#     print(sum)
#     return sum

# calc_sum(5,10)
#------------------ OR--------------
# def calc_sum(a,b):
#     return a+b

# sum=calc_sum(13333,333)
# print(sum)
# ------------------------------------
# def print_hello():
#     print("hello")

# i=0 
# for i in range(10):
#     print_hello()
#  -------------------------   
# def print_hello():
#     print("hello")

# output=print_hello()
# print(output) # it will give the output as none because the function doesnot contain return
# -------------------------------------------------------------------------------------------------------
#average of three numbers
# def avg(a,b,c):
#     avg=(a+b+c)/3
#     print(avg)
#     return avg #(optional)

# avg(2,3,4)
# --------------------------------------------------------
#FUNCTIONS IN PYTHON
#----> BUILT IN FUNCTIONS-print(), len(), type(),range()

# def cal_prod(a=4,b=9):
#     print(a*b)
#     return a*b
# cal_prod() # no need to give arguments here as it is already 
#             #defined in the function defination part
# ---------------------------------------------------------------
# cities=["delhi","gurgaon","noida","pune","mumbai","chennai"]
# heroes=["thor","ironman","batman","spiderman"]   


# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(heroes)      
# -----------------------
# def print_list(list):
#     for i in list:
#         print(i,"-",end=" ")

# print_list(heroes)
# print_list(cities)
# -------------------------------------------------------
#write to find the factorial of n. (n is the parameter)
# n=5
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)

# factorial(5)
# ----------------------------------------------------------
#write a function to covert USD to INR

# def converter(usdval):
#     inrval=usdval*83
#     print(usdval,"USD=",inrval,"INR")

# converter(90)
# ------------------------------------
# def num(a):
#     if n%2==0:
#         print(a,"is an even number")
#     else:
#         print(a,"is an odd number ")


# n=int(input("Enter the number:"))
# num(n)

# ============================================================

#RECURSION.-:when a function calls itself repeadtedly

#prints n to 1 backwords

# def show(n):
#     if(n==0):   #-----
#  #                   | when n becomes 0 it stops the function and dont print the 0
#         return  #-----
#     print(n)
#     show(n-1)
    
# show(5)
# ------------------------------------------------------------
#returns n!
# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return fact(n-1)*n
# a=fact(5)
# print(a)
# -----------------------------------------------------------------
# recursion function of calculate sum of first n natural number
# def calc_sum(n):
#     if n==0:
#         return 0
   
#     return calc_sum(n-1 )+ n

# print(calc_sum(5))
# ------------------------------------------------------------------
# #write a recursive function to print all elements in a list
# #use list and index as parameters

# def print_list(list,idx=0):
#     if (idx==len(list)):
#         return
#     print(list[idx])
#     print_list(list,idx+1)

# fruits=["banana","mango","litchi","apple"]
# print_list(fruits)

# ===================================================================================

#FILE INPUT AND OUTPUT---------------------------
# ----------------------
# f=open("demo.txt","r")
# data=f.read()  # to read data
# print(data)
# print(type(data))
# f.close()   #to close the file is necessary

# f=open("demo.txt","r")
# data=f.read()  # to read data
# print(data)
# line1=f.readline()
# print(line1)

#writing into the file
# -------------------------
# f=open("demo.txt","w")
# f.write("I will learn javascript for web development,after thar nodejs")

# f.close()
# -------------------------------
# to delete a file-----
#import os
#os.remove("sample.txt")
# ------------------------------------------------------------------------

#Create a new file “practice.txt” using python. Add the following data in it:
# Hi everyone
# we are learning File I/O
# using Java.
# I like programming in java

# with open("practice.txt","w") as f:
#     f.write("Hi everyone\n")
#     f.write("we are learning File I/O\n")  #dont need to close file if using ("with open() as f") as it automatically closes the file
#     f.write("using Java.\n")
#     f.write("I like programming in java\n")
# --------------------------------------------------------------------------------------------------------------------------------------
# WAF that replace all occurrences of “java” with “python” in above file.
# with open("practice.txt","r") as f:
#     data=f.read()
# new_data=data.replace("Java","python") # replace is used to replace a word with another in a file
# print(new_data)

# # To save this in the file we need to overwrite the data so open file in write mode.
# with open("practice.txt","w") as f:
#     f.write(new_data)
# ------------------------------------------------------------------------------------------------------------
#Search if the word “learning” exists in the file or not.
# with open("practice.txt","r") as f:
#     data=f.read()
#     if "learning" in data:
#         print("The word 'learning' was found in file")
#     else:
#         print("The word 'learning' was NOT found in file")  
# 
# -------------------OR THE OTHER WAY IS--------------------------
# def check_for_word():
#     word="learning"
#     with open("practice.txt","r") as f:
#         data=f.read()
#         if(data.find(word)!=-1):
#             print("found")
#         else:
#             print("not found")
# check_for_word()
# --------------------------------------------------------------------------------------------------------------
#WAF to find in which line of the file does the word “learning” occur first.
# with open("practice.txt","r") as f:
#     lines=f.readlines()
#     for i in lines:
#         if "learning" in i:
#             print("The word 'learning' occurs first in line ",{i})
# ---------------------------------OR THE OTHER WAY IS------------------------------
# def check_for_line():
#     word="learning"
#     data=True
#     line_no=1
#     with open("practice.txt","r") as f:
#         while data:
#             data=f.readline()
#             if (word in data):
#                 print(line_no)
#                 return
#             line_no+=1

#     return-1
# check_for_line()
# -------------------------------------------------------------------------------------------------------------------        
  
#From a file containing numbers separated by comma, print the count of even numbers.
# count=0
# with open("number.txt","r") as f:
#     data=f.read()
    

#     nums=data.split(",")
#     for val in nums:
#         if int(val)%2==0:
#             count+=1

# print(count)
# --------------------------------------------
# to print even numbers between 1 to 50
# i=0 # or i=1, if its i=1 then it will print the numbers from 2
# while i<=50:
#     if i%2==0:
#         print(i)
#     i=i+1 # or i+=2
# --------------------------------------------
# # all the multiples of 5 between 10 and 25.
# for i in range(10,26):
#     if i%5==0:
#         print(i)
#     i+=1
# --------------------------------------------
# total=0
# for i in range(5):
#     num=float(input("enter the number "))
#     total=total+num
# average=total/5
# print("The averaged is:",average)

# def interest(principal, time =2, rate=0.10):
#     return principal*rate*time
# --------------------------------------------

# print=float(input("Enter principal amount :"))
# print("Simpleinterest with default ROI and time values is :")
# si1=interest(prin)
# print("Rs.", si1)
# roi=float (input("Enter rate of interest (ROI):"))
# time=int(input("Enter time in years:"))
# print("Simple interest with your provided ROI and time values is:")
# si2=interest(prin, time, roi/100)
# print("Rs.", si2)
# 
# variable="Himani"
# print(f"hello {variable}!")
# --------------------------------------------

# def greet(name):
#     return f"Hello\n{name}!"
# print(f"{greet('Himani')} welcome to python.")

# f=lambda a:a*a
# result=f(5)
# print(result)

# --------------------------------------------
# def swap(x,y):
#     temp = x
#     x = y
#     y = temp

# x=3
# y=4
# swap(x,y)
# print(x)
# print(y)
# --------------------------------------------
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(4))

# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)

# print(fibonacci(10))

# --------------------------------------------
# LAMBDA FUNCTIONS( FOR WRITING CODE IN ONE LINE)-------------
# --------------------------------------------

#positive and negative number using lamda functions
# n= lambda x: "positive" if x>0 else "negative" if x<0 else "zero"
# print(n(5))
# print(n(-5))
# print(n(0))

# #sum using lambda function
# sum= lambda x,y: x+y
# print(sum(7,8))

#****************************************************************
# OOPS(OBJECT ORIENTED PROGRAMMING)--------------------
#*****************************************************************

#Create a student class that takes name and marks of 3 subjects as 
# arguments in constructor.then create a method to print average.

# class Students:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print("hi",self.name,"your avg score is:",sum/3)

# s1=Students("tony stark",[99,98,97])
# s1.get_avg()

# s1.name="ironman"  #manipulating the values or attributes
# s1.get_avg()
# --------------------------------------------------------------------------------------------------------------
#Implementing abstratction............
# class Car:
#     def __init__(self):
#         self.acc=False
#         self.clutch=False
#         self.brk=False

#     def start(self):
#         self.clutch=True
#         self.acc=True
#         print("Car started...")

# car1=Car()
# car1.start()
# --------------------------------------------------------------------------------------------------------------
#Create a account class with 2 attributes -balance and account no.
#create methods for debit, credit, printing the balance 

# class Account:
#     def __init__(self,acc,bal):
#         self.account_no=acc
#         self.balance=bal

#     #debit method
#     def debit(self,amount):
#         self.balance = self.balance-amount
#         print("Rs.",amount, "was debited from your account")
#         print("total balance=", self.get_balance())

#     #credit method
#     def credit(self,amount):
#         self.balance = self.balance+amount
#         print("Rs.",amount, "was credited to your account")
#         print("total balance=", self.get_balance())
 
#     def get_balance(self):
#         return self.balance


# acc1=Account(12345,10000)
# print("your account number is:",acc1.account_no)
# print("your bank balance is:",acc1.balance)
# acc1.debit(1000)
# acc1.credit(500)
# acc1.credit(40000)

# ------------------------------------------------------------------------------------------------------------------
#INHERITANCE
# class Car:
#     @staticmethod
#     def start():
#         print("car started...")
    
#     @staticmethod
#     def stop():
#         print("car stopped..")

# class Toyotacar(Car):
#     def __init__(self,name):
#         self.name=name

# car1=Toyotacar("Fortuner")
# car2=Toyotacar("Prius")
# print(car1.start())
# print(car1.name)

#USING SUPER METHOD
# class Car:
#     def __init__(self,type):
#         self.type=type
    
#     @staticmethod
#     def start():
#         print("car started...")
    
#     @staticmethod
#     def stop():
#         print("car stopped..")

# class Toyotacar(Car):
#     def __init__(self,name,type):
#         super().__init__(type)
#         self.name=name
#         super().start()
        
# car1=Toyotacar("Fortuner","electric")
# print(car1.type)

#COMPLEX NUMBERS----

# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img

#     def showNumber(self):
#         print(self.real,"i +",self.img,"j")

#     def add(self,num2):
#         newreal = self.real + num2.real
#         newimg = self.img + num2.img
#         return Complex(newreal,newimg)

# num1=Complex(1,3)
# num1.showNumber()

# num2=Complex(4,8)
# num2.showNumber()

# num3=num1.add(num2)
# num3.showNumber()

#Define a circle class to create a circle with radius r using constructor.
# define an area() method of the class which calculates the area of the circle.
# define the perimeter() method of the class which allows you to calculate the perimeter of the circle.

# class Circle:
#     def __init__(self,radius):
#         self.radius=radius

#     def Area(self):
#         return 3.14 * self.radius ** 2
    
#     def Perimeter(self):
#         return 2 * 3.14 * self.radius
    
# c1=Circle(21)
# print("Perimeter of the circle is:",c1.Perimeter())
# print("Area of the circle is:",c1.Area())

#Defien a Employee class with the attributes role,department and salary.
# this class also has a showDetails() method.
# Create an Engineer class which inherits the properties from Employee and have the attributes : name and age

# class Employee:
#     def __init__(self,role,department,salary):
#         self.role=role
#         self.department=department
#         self.salary=salary

#     def showDetails(self):
#         print("Role=",self.role)
#         print("department=",self.department)

# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         super().__init__("Engineer","IT","75,000")

# engg1=Engineer("Elon Musk",40)
# engg1.showDetails()

# # Taking input from the user
# num = int(input("Enter a value: "))

# add = num + 5

# # Output
# print("The sum is %d" %add)

# class Student:
#     def __init__(self,name,marks):
#         print("adding a student in the database")

#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#         print("adding a student in the database")

# s1=Student("karan singh",90)
# print(s1.name,s1.marks)

# s1=set()
# s1=set("GeeksForGeeks")
# print("Set with the use of string:",s1)
# s2=set(["Geeks","For","Geeks"])
# print("Set with the use of list:",s2)

# with open("practice.txt","w") as f:
#     f.write("Hi everyone\n")
#     f.write("we are learning File I/O\n")  #dont need to close file if using ("with open() as f") as it automatically closes the file
#     f.write("using Java.\n")
#     f.write("I like programming in java\n")

# class Car:
#     def __init__(self, model, year, variant, colour, for_sale):
#         self.model = model
#         self.year = year
#         self.variant = variant
#         self.colour = colour
#         self.for_sale = for_sale

# car1 = Car("Mercedes-Benz E-Class", 2024,"E 220d","Obsidian Black", "Available")
# car2 = Car("BMW 5 SERIES")

# arr = [-1,0,3,4,5,9,12]
# target = 5
# st = 0
# end = len(arr)-1
# flag = 0

# while st<=end:
#     mid = (st+end)//2

#     if arr[mid] == target:
#         print("Element found at index: ",mid)
#         flag = 1
#         break
#     elif arr[mid]<target:
#         st=mid+1
#     else:
#         end=mid-1
# if flag == 0:
#     print("Element not found")

# def bs(arr,start,end,tar):
#     if start>end:
#         return -1
#     mid=(start+end)//2
#     if arr[mid] == tar:
#         return mid
#     elif tar<arr[mid]:
#         return bs(arr,start,mid-1,tar)
#     else:
#         return bs(arr,mid+1,end,tar)
    
# arr=[-1,0,3,4,5,9,12]
# print(bs(arr,0,len(arr)-1,4))


#CLASS VARIABLES

# class Student:

#     class_year = 2024
#     num_students =0 
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Student.num_students+=1
# # use loops

# student1 = Student("Kavya", 20)
# student2 = Student("Diya", 21)

# print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
# print(student1.name)
# print(student2.name)

# -------------------------------------------------------
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def display(self):
#         print("Name: ",self.name)
#         print("Age: ",self.age)
#         print()

# students=[]
# n=int(input("Enter the number of students;"))
# for i in range(n):
#     name=input("Enter the students name: ")
#     age = int(input("Enter the age:"))
#     s=Student(name,age)
#     students.append(s)

# print("\nStudents details\n")
# print("-------------------")

# for student in students:
#     student.display()


'''
# ---------------------------------------------
# INHERITANCE
# --------------------------------------------
class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def bark(self):
        print(f"{dog.name} is barking")

class Cat(Animal):
    pass

class Mouse(Animal):
    pass

dog=Dog("scooby")
dog.bark()
cat=Cat("meow")
cat.eat()
cat.sleep()
dog.sleep()
# ------------------------------------------------------------------------
# Abstract method
# ----------------------------
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod            # these start() amd stop() functions are there in the abstarct method and the parent class,so this will be 
    def start(self):           # followed in the inherited class too, so every vhild class will have stop() and start() function.
        pass                   # if the functions are not present, it will create an error

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    # def __init__(self, name, colour):
    #     self.name=name
    #     self.colour=colour

    def start(self):
        print("You start the car")

    def stop(self):
        print("You stop the car")

class Bike(Vehicle):
    def __init__(self, name, colour):
        self.name=name
        self.colour=colour

    def start(self):
        print(f"You start the {self.name}")

    def stop(self):
        print(f"You stop the {self.name}")

class Scooty(Vehicle):
    def start(self):
        print("You start the scooty")

    def stop(self):
        print("You stop the scooty")


car = Car()
car.start()
car.stop()

bike1 = Bike("Yamaha","Red")
bike1.start()
bike1.stop()
# ------------------------------------------------------------
# SUPER()
# ------------------------------------------------------------
class Shape:
    def __init__(self, colour, is_filled):
        self.colour = colour
        self.name = is_filled 

class Circle(Shape):
    def __init__(self, colour, is_filled, radius):
        super().__init__(colour, is_filled)
        self.radius = radius

class Square(Shape):
    def __init__(self, colour, is_filled, side):
        super().__init__(colour, is_filled)
        self.side = side

class Triangle(Shape):
    def __init__(self, colour, is_filled, side,height):
        super().__init__(colour, is_filled)
        self.side = side
        self.height = height

circle = Circle(colour = "red", is_filled = True, radius = 5)
print(circle.colour)
print(circle.is_filled)
print(f"{circle.radius} cm")

# ---------------------------------------------------------------------------------------
#POLYMORPHISM
# ----------------------------------------------------------------------------------------
from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14* self.radius **2
    
class Square(Shape):
    def __init__(self,side):
        self.side = side
    
    def area(self):
        return self.side **2
    
   
class Triangle(Shape):
    def __init__(self,side,height):
        self.side = side
        self.height = height
    
    def area(self):
        return self.side * self.height * 0.5
    
shapes =[Circle(4), Square(5), Triangle(6,7)]

for i in shapes:
    print(i.area())

#===========================================================================  
#LIBRARY MANAGEMENT SYSTEM:
#==========================================================================
    def __init__(self):
        self.books = []

    # Add book
    def add_book(self):

        book = input("\nEnter book name: ")

        self.books.append(book)

        print(f"\n'{book}' added successfully!")

    # Remove book
    def remove_book(self):

        book = input("\nEnter book name to remove: ")

        if book in self.books:

            self.books.remove(book)

            print(f"\n'{book}' removed successfully!")

        else:

            print("\nBook not found!")

    # Display books
    def display_books(self):

        if len(self.books) == 0:

            print("\nLibrary is empty!")

        else:

            print("\n========== AVAILABLE BOOKS ==========")

            for i, book in enumerate(self.books, start=1):

                print(f"{i}. {book}")

    # Search book
    def search_book(self):

        book = input("\nEnter book name to search: ")

        if book in self.books:

            print(f"\n'{book}' is available in library!")

        else:

            print(f"\n'{book}' is not available!")

    # Total books
    def total_books(self):

        print(f"\nTotal books in library: {len(self.books)}")


# Object Creation
library = Library()

# Main Program
while True:

    print("\n")
    print("=" * 50)
    print("         LIBRARY MANAGEMENT SYSTEM")
    print("=" * 50)

    print("\n1. Add Book")
    print("2. Remove Book")
    print("3. Display Books")
    print("4. Search Book")
    print("5. Total Books")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    # Add
    if choice == "1":

        library.add_book()

    # Remove
    elif choice == "2":

        library.remove_book()

    # Display
    elif choice == "3":

        library.display_books()

    # Search
    elif choice == "4":

        library.search_book()

    # Total
    elif choice == "5":

        library.total_books()

    # Exit
    elif choice == "6":

        print("\nThank you for using Library Management System!")

        break

    else:

        print("\nInvalid choice! Please try again.")

'''
# ------------------------------------------------------------
#PATTERN CODES
# ------------------------------------------------------------
#01.Right-Angled Triangle (Half Pyramid)

n = 5
for i in range(1, n + 1):
    print("* " * i)

#02. Inverted Right-Angled Triangle

n = 5
for i in range(n, 0, -1):
    print("* " * i)

#03. Floyd's Triangle

n, num = 4, 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()



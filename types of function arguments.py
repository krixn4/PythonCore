#keyword arguments
# def fun(n,a):
#     print("name:",n)
#     print("age:",a)
# fun(n='arun',a=23)
# fun(a=23,n='arun')

#default argument
# def fun(n,a=25):
#     print("name:",n)
#     print("age:",a)
# fun(n='arun',a=23)
# fun(n='arun')

#variable length/ arbitary arguments

#arbitary postional
# def fun(*args):
#     print(args)
# fun(10,20,30)

#arbitary keyword
# def fun(**kwargs):
#     print(kwargs)
# fun(a=10,b=20,c=30)

#define a fun to find the sum of numbers using arbitary argument type
# def add(*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     print(sum)
#
# def addd(**kwargs):
#     sum=0
#     for i in kwargs.values():
#         sum=sum+i
#     print(sum)
#
# add(10,20,30)
# add(1,2,3,4,5)
# addd(a=10,b=20,c=30)

#write a program to create a list of 5 random 3 digit numbers
# import random
# new=[]
# for i in range(1,6):
#     new.append(random.randint(100,999))
# print(new)

#write a program to create a  5digit random otp number
# otp=random.randint(10000,99999)
# print('otp:',otp)

#write a program to find the position of a character in a string
# str=input("enter the string:")
# chr=input("enter the character:")
# print(str.find(chr))

#define a function that takes a string as arguments and returns a new dictionary where keys are character and values are count of each character
# def strfun(s):
#     new={}
#     for i in s:
#         new[i]=s.count(i)
#     print(new)
# s=input("enter the string")
# # print(strfun(s))
# #define a function that takes string as argument and print the count of digits,spaces,letters in that string
# def csl(s):
#     count=0
#     space=0
#     letter=0
#     for i in s:
#         if i.isdigit():
#             count+=1
#         elif i.isspace():
#             space+=1
#         elif i.isalpha():
#             letter+=1
#     print('digits=',count)
#     print('space=',space)
#     print('letter=',letter)
# s=input("enter the string:")
# print(csl(s))


# #list comprehension
#
# #l=[1,2,3,4]
# # new=[i**2 for i in l]
# # print(new)
# # new=[i**3 for i in l]
# # print(new)
# # new=[5 for i in l]
# # print(new)
#
# # l=[23,56,34,12,89,90,24]
# # new=[i for i in l if(i%2==0)]
# # print(new)
# # new=[i for i in l if i>50]
# # print(new)
# #Given a list
# l=[12,45,34,67,90]
# # create a new list with even values
#
# new=[i for i in l if i%2==0]
# print(new)
#
# #create a new list with values greater than 50
# new=[i for i in l if i>50]
# print(new)
# #Given  a list
# colors=['red','green','blue','orange']
# # create a new list with first letter of each color
# new=[i[0] for i in colors]
# print(new)
# # create a new list with length of each color
# new=[len(i) for i in colors]
# print(new)
# #create a new list of cubes
# l=[1,2,3,4]
# new=[i**3 for i in l]
# print(new)
#
# #create a new list of square roots
# import math
# l=[25,36,81,100]
# new=[math.sqrt(i) for i in l]
# print(new)
#
# #create a new list of lengths
# colors=['red','green','blue','yellow','black']
# #create a new list of first characters
# new=[i[0] for i in colors]
# print(new)
# #create a new list of last characters
# new=[i[-1] for i in colors]
# print(new)
# #create a new list of reverse of each element
# new=[i[::-1] for i in colors]
# print(new)
# #Given a list
# l=[23,78,12,56]
# #Add 10 to each element in the given sequence
# new=[i+10 for i in l]
# print(new)
# ##given a list of dictionaries
# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
#     {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
#     {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
#
# # # create a new list of emails
# new=[i['email'] for i in l]
# print(new)
#
# # # #create a new list with square root of each element
# #l=[25,16,9,36]
#
#
# # #Given a dictionary
# d={'arun':25,'amal':34,'akhil':26,'anu':21}
# # # create a list of names
# new=[i for i in d.keys()]
# print(new)
# # # create a list of marks
# new=[i for i in d.values()]
# print(new)
# # #Given a list
# l=[23,56,12,89,-34,-23,-67,-43,9.7,4.5,'hello','world']
#
# # #create a list of string values
# new=[i for i in l if(type(i)==str)]
# print(new)
# # #create a list of floats
# new=[i for i in l if(type(i)==float)]
# print(new)
# # #create a list of positive numbers
# new=[i for i in l if type(i)!=str and i>0]
# print(new)
# #
# #
# # #Given a list
# fruits=['apple','orange','pineapple','avocado','grapes']
# # #create a new list with elements whose length is greater than 6
# new=[i for i in fruits if len(i)>6]
# print(new)
# # #create a new list with elements whose value is divisible by 3 in range(1,101)
# new=[i for i in range(1,101) if i%3==0]
# print(new)
# # Given
# s="python coding  is easy and fun"
# # # create a new list with only vowels
# new=[i for i in s if i in 'aeiouAEIOU']
# # print(new)
#

#dictionary comprehension
# l=[1,2,3,4]
# new={i:i**2 for i in l}
# print(new)
#
# l=[10,20,30,40]
# new={i:l[i] for i in range(0,len(l))}
# print(new)

# s='python is a programming language'
# for i in s.split():
#     print(i)
#
# s='python coding is easy and fun'
# new={i:len(i) for i in s.split()}
#print(new)


#functions

# def add():
#     n1=int(input("enter a no:"))
#     n2=int(input("enter a no:"))
#     sum=n1+n2
#     print("sum=",sum)
#     return
# add()

##define a fucn to display "hello your name"

# def name():
#     n=input("enter your name:")
#     print("hello "+n)
# name()
#define a funct to find the factorial of a number

# def fact():
#     n=int(input("enter the no:"))
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)
# fact()
#define a function to find the count of a specific character in a giver string
# def count():
#     s=input("enter a string:")
#     chr=input("enter the char to count:")
#     count=0
#     for i in s:
#         if i==chr:
#             count+=1
#     print(count)
# count()

#prime or not
# def prime():
#     n=int(input("enter the no:"))
#     for i in range(2,n):
#         if n%i==0:
#             print("not prime")
#             break
#     else:
#         print("prime")
# prime()
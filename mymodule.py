# from calculator.operations import *
# a=int(input("enter no:"))
# b=int(input("enter no:"))
# op=input("enter operation:")
# if op=='+':
#     add(a,b)
# elif op=='-':
#     diff(a,b)
# elif op=='*':
#     mul(a,b)
# elif op=='/':
#     div(a,b)
# else:
#     print("invalid operation")

from shapes import circle,rectangle

r=int(input("enter radius:"))
circle.area(r)
circle.perimeter(r)
l=int(input("enter lenght:"))
b=int(input("enter breadth:"))
rectangle.area(l,b)
rectangle.perimeter(l,b)


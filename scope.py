#accessibility of a variable
#area of a program code where variable/name can be accessed

#global
#   scope of a variable declared inside the main part of a program code

#local
#   sxope of variable declared inside a block/functiom

#global
# x=10
# print("outside:",x)
# def f():
#     print("inside:",x)
# f()

#local
# def f():
#     x = 10
#     print("inside:",x)
# f()
# print("outside:",x)

# def f():
#     global x
#     x=10
#     print("inside:",x)
# def g():
#     y=20
#     print(x)
# f()
# g()

#nonlocal/enclosing
# def outer():
#     x=10
#     print(x)
#     def inner():
#         print(x)
#     inner()
# outer()

#write a pgm to interchange two variables
from tempfile import tempdir

a=2
b=3
# temp=a
# a=b
# b=temp
# print("a=",a)
# print("b=",b)

#without using temp var

a,b=b,a
print("a=",a)
print("b=",b)
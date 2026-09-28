#100,200,300...1000
#
# for i in range(100,1001,100):
#     print(i)

#1,8,27
# for i in range(1,6):
#     print(i**3)

#3 digit no divisible by 3
# for i in range(100,1000):
#     if i%3==0:
#         print(i)

# colors=['red','green','blue','yellow','black']
# for i in colors:
#     print(i[::-1])

# #print each digit in a number
# n=1234
# for i in str(n):
#     print(i)

# #sum of digit
# n=1234
# sum=0
# for i in str(n):
#     sum+=int(i)
# print(sum)

# l=[1,2,3,4]
# new=[]
# for i in l:
#     new.append(i**2)
# print(new)

# s="hello world"
# new=""
# for i in s:
#     if i in "aeiouAEIOU":
#         new+=i
# print(new)

# l=[1,2,3,4]
# d={}
# for i in l:
#     d[i]=i**2
# print(d)

# #reverse of a string
# s="hello"
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)

#rev of a no

n=1234
rev=""
for i in str(n):
    rev=i+rev
print(rev)
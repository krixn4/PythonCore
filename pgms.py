#write a pgm to check whether a no is armstrong
# num=int(input("enter the no:"))
# s=str(num)
# l=len(s)
# sum=0
# for i in s:
#     sum+=int(i)**l
# if num==sum:
#     print("armstrong")

#factors of a no
# n=int(input("enter the no:"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

# for i in range(1,6):
#     if i==3:
#         break
#     print(i)
# else:   #it works only after the normal execution of loop
#     print("hello")

#check whether a no prime or not
# num=int(input("enter no:"))
# if num>1:
#     for i in range(2,num):
#         if num%i==0:
#             print("not prime")
#             break
#     else:
#         print("prime")
# else:
#     print("no is neither prime nor composite")

#nested loop

# l=[1,2,3,4]
# for i in l:
#     for j in range(1,5):
#         print(i,end=" ")
#     print()
#
# for i in range(1,4):
#     for j in range(1,5):
#         print('*',end=' ')
#     print()

# l=[['lion','tiger'],['cat','dog']]
# for i in l:
#     for j in i:
#         print(j,end=' ')
#     print()

#1. names=['kelly','alan','jeny']
# for i in names:
#     for j in range(1,4):
#         print(i,end=' ')
#     print()

#2. given 2 lists
# n=[1,2,3]
# q=['what','when','why']
#
# for i in n:
#     print(i)
#     for j in q:
#         print(j,end=' ')
# #     print()
#
# ##3.given a list
# d=[{'id':101,'name':'arun','age':23},
#    {'id':102,'name':'amal','age':24},
#    {'id':103,'name':'anu','age':25}]
# for i in d:
#     for j in i.values():
#         print(j,end=' ')
#     print()

# for i in range(1,5):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()

# for i in range(1,8,2):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(i,end=' ')
#     print()

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()

# for i in range(5,1,-1):
#     for j in range(1,i):
#         print('*',end=' ')
#     print()

# l=[23,45,78,90,12,13,91]
# for i in l:
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)

# for i in range(1,100):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)
#
# for i in range(1,5):
#     for j in range(1,6):
#         print(j,end=' ')
#     print()

# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()
# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end=' ')
#         k+=1
#     print()

# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end=' ')
#         k+=1
#     print()

# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end=' ')
#     k+=1
#     print()

# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end=' ')
#         k+=1
#     k=ord('A')
#     print()

# for i in range(1,5):
#     for j in range(1,5):
#         if i==j:
#             print(i,end=' ')
#         else:
#             print('0',end=' ')
#     print()

# for i in range(1,5):
#     for j in range(1,i+1):
#         if j%2!=0:
#             print('1',end=' ')
#         else:
#             print('0',end=' ')
#     print()

# k=0
# for i in range(1,6):
#     for j in range(0,i):
#         print(j,end=' ')
#     print()

# h='hello'
# for i in range(1,6):
#     for j in range(0,i):
#         print(h[j],end=' ')
#     print()
# #
# k=6
# for i in range(1,5):
#     for p in range(1,k+1):
#         print(end=' ')
#     for j in range(1,i+1):
#         print(j,end='   ')
#     k=k-2
#     print()
# k=2
# for i in range(3,0,-1):
#     for p in range(1,k+1):
#         print(end=' ')
#     for j in range(1,i+1):
#         print(j,end='   ')
#     k=k+2
#     print()

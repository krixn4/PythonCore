#define a function that takes a string as argument and return a new dict where keys are words and values are lenght of each word
# def stringfun(s):
#     new={}
#     for i in s.split():
#         new[i]=len(i)
#     return new
# s='python coding is easy and fun'
# print(stringfun(s))

#define a function that takes a number as argument and check whether that number is spy number of not
def spy(n):
    s=str(n)
    sum=0
    product=1
    for i in s:
        sum=sum+int(i)
        product=product*int(i)
    if sum==product:
        return 'spy number'
    else:
        return 'not a spy number'
n=int(input("enter a number:"))
print(spy(n))

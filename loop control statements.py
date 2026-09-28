#break
    #exit from the loop
#continue
    #to skip an iteration
#pass
    #no operation code/null statement

# s="hello"
# for i in s:
#     if i=='l':
#         break
#     print(i)

# s="hello"
# for i in s:
#     if i=='l':
#         continue
#     print(i)

l=[25,67,34,78,17,44,82]
#print all the numbers
for i in l:
    print(i)
print(('\n'))

#stops the loop when i>50
for i in l:
    if i>50:
        break
    print(i)
print('\n')

#skip all even no
for i in l:
    if i%2==0:
        continue
    print(i)

colors=['red','green','yellow','blue','orange','black']
#print all colors
for i in colors:
    print(i)
print('\n')

#print those colors starting with 'b' #blue black
for i in colors:
    if i[0]=='b':
        print(i)
print('\n')

#print the first color starting with 'b' #blue
for i in colors:
    if i[0]=='b':
        print(i)
        break
print('\n')

#skips all colors starting with 'b'
for i in colors:
    if i[0]=='b':
        continue
    print(i)
print('\n')

3.
s="python coding is easy and fun"
#print all charcters upto a specific character(including that character)
ch=input("enter character:")
for i in s:
    print(i)
    if i==ch:
        break

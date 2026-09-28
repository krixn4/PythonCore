l=[23,45,67,12,89,70]
#filter even no greater than 50
print(list(filter(lambda x:x%2==0 and x>50,l)))

#given a list
colors=['red','green','blue','yellow','orange']
#filter colors whose lenght is greater than 5
print(list(filter(lambda x:len(x)>5,colors)))
#filter the color containing letter 'n'
print(list(filter(lambda x:'n' in x,colors)))
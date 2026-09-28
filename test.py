#declare a list of five colours
#add a new colour yellow to the list
#change the second colour to black
#print the list in reverse order
#print the second last colour
#print the no of colours
#print the updated list

colors=['violet','indigo','blue','green','orange']
print(colors)
colors.append('yellow')
print(colors)
colors[1]='black'
print(colors)
print(colors[::-1])
print(colors[-2])
print(len(colors))
print(colors)
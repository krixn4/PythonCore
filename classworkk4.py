#write a pgm to check whether the entered num is positive even/posiive odd ,negative even/negative odd

num=int(input("enter the number"))
if num>0:
    if num%2==0:
        print("postive even")
    else:
        print("positive odd")
else:
    if num%2==0:
        print("negative even")
    else:
        print("negative odd")

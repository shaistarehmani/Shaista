s=int(input("Enter the start index:" ))
e=int(input("Enter the ending index")) 
for i in range(s,e+1):
    if i>1: 
        for n in range(2,i):
            if i%n==0:
              break
        else:
            print(i)   

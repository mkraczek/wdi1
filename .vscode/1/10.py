import random
x,y=input("wprowadz 2 liczby").split()
print ("wprowadz wybrane dzialanie matematyczne")
d=input("+,-,*,/,^,#,x")
x=float(x)
y=float(y)
if d=="+":
    print(x+y)
elif d=="-":
    print (x-y)
elif d=="*":
    print (x*y)
elif d=="/":
    if y==0:
        print ("error")
        quit
    else:
        print(x/y)
elif d=="^":
    print(x**y)
elif d=="#":
    if x<0 and y%2==0:
        print("error")
        quit()
    else:
        print (x**(1/y))
elif d=="x":
    if x<y:
        print (random.randint(x,y))
    else:
        print (random.randint(y,x))
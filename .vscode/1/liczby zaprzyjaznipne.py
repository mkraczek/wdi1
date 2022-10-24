for x in range (1,1000_001):
    suma=1
    for i in range (2,int(x**(1/2)+1)):
        if x%i==0:
            suma=suma+i+(x//i)
    y=suma
    sumay=1
    for i in range (2,int(y**(1/2)+1)):
        if y%i==0:
            sumay=sumay+i+(y//i)
    if sumay==x and x!=y and x<y:
        print (x,y)

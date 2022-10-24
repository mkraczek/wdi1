a=int(input("choinka"))
for i in range (0,a):
    if i==0:
        print(" "*(a)+"X")
    else:
        print(" "*(a-i) + "*"*(2*i+1))
print(" "*(a)+"U")
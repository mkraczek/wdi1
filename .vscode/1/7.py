a=int(input("dolna granica zakresu"))
b=int(input("górna granica zakresu"))
if b<a:
    print("error")
    quit()
if b-a<=19:
    for i in range (a,b+1):
        print (i,end=" ")
else:
    srednia=(a+b)/2
    if (a+b)%2==0:
        srednia=int(srednia)
        print(srednia-3, srednia -2, srednia-1, srednia+1, srednia+2, srednia+3)
    else:
        srednia=int(srednia)
        print (srednia-2, srednia-1, srednia, srednia +1, srednia+2, srednia+3)


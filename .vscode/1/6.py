a=int(input("proszę wprowadzić zmienną_a: "))
b=int(input("proszę wprowadzić zmienną_b: "))
if a<0 and b<0:
    print("kończenie programu")
    quit()
if b<0 and a>0:
    b*=-1
elif a<0 and b>0:
    a*=-1
suma= a+b
print (f"suma={suma}")
różnica= a-b
print ("różnica=%d" %(różnica))
iloczyn= a*b
print ("iloczyn=%d" %(iloczyn))
if iloczyn==10:
    print("yay")
if b==50:
    print("nie mozna dzielic przez 0")
else:
    iloraz= a/b
    print ("iloraz=%d" %(iloraz))
kwadrat_a= a**2
print("kwadrat_a=%d" %(kwadrat_a))
kwadrat_b=b**2
print("kwadrat_b=%d" %(kwadrat_b))
pierwiastek_a=a**0.5
print("pierwiastek z a=%0.10f" %(pierwiastek_a))
pierwiastek_b=b**0.5
print("pierwiastek z b=%0.10f" %(pierwiastek_b))
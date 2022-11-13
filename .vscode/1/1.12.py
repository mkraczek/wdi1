n=int(input("Proszę wprowadzic pierwsza lizbę większą niż zero i mniejszczą od 10^10 "))
m=int(input("Proszę wprowadzic druga lizbę większą niż zero i mniejszczą od 10^10 "))
print("Proszę wprowadzić działanie matematyczen (Tylko dodawanie i odejmowanie)")
d=input()
if d=="+":
    wynik=int(m+n)
elif d=="-":
    wynik=int(n-m)

if n>10**10 or m>10**10:
    print('za duze liczby')
    quit()
if d== '*' or d=="/":
    print('kalkulator nie obsluguje mnozenie i dzielenia')
    quit()
def rozdziel(x):
    cyfry=[]
    while x>0 and x<10**10:
        cyfry.append(x%10)
        x//=10
    return cyfry[::-1]


spacjen=12-len(rozdziel(n))
spacjem=11-len(rozdziel(m))
spacjew=12-len(rozdziel(abs(wynik)))


if d== "+":
    print(' '*spacjen + str(n))
    print('+'+ spacjem*' ' + str(m))
    print("-----------")
    print(' '*spacjew + str(wynik))
if d=="-" and wynik>0:
    print(' '*spacjen + str(n))
    print('-'+ spacjem*' ' + str(m))
    print("------------")
    print(' '*spacjew + str(wynik))
if d=="-" and wynik<0:
    print(' '*spacjen + str(n))
    print('-'+ spacjem*' ' + str(m))
    print("-----------")
    print(' '*(spacjew-1) + str(wynik))
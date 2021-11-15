import random
import datetime
a=datetime.datetime.now()
print("\n\n\t \t welcome to casino",end=' at Date: ')
print(a.strftime("%d %m %y Time: %H:%M"),end='\n\n')
print("\t \t start with no. between 30")
i=int(input(" \t\t "))
d=random.randrange(1,30)
if (i==d):
    print("\t \t Right guess you win",end='')
    print("generated number is",d,end='\n\n\t\t\yThanku for playing')
else:
    print("\n\t\t opps you lost",end=' ')
    print("generated number is",d)
    print("\n\t\t but no worry lets try with fruits")
    j=['mango','banana','papaya','berries']
    k=input("\t\t enter the fruit name \n \t\t ")
    l=random.choice(j)
    if (k==l):
        print("\t\t you won",end=' ')
        print(" generated fruit is",l,end='\n\n\t\t\tThanku for playing')
    else:
        print("\n\t\t opps you lost again")
        print("\t\t generated fruit is",l,end='\n\n\t\t\tThanku for playing')
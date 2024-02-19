import math

def fivepercent(n):
    n+=((n*5)/100)
    n+=(n*5)/100
    return n

p,v=map(int,(input("Enter p and v: ").split()))

c=input("With taxes? y or n ")

if(c=='n'):
    p=fivepercent(p)
    v=fivepercent(v)
    
m=(35*p+7*v)/6
r=(23*p+10*v)/6
a=(38*p+7*v)/6


print(f"M: {int(m)}\nR: {int(r)}\nA: {int(a)}")
print(f"Total: {int(m+r+a)}")    

c=input("Discount? y or n ")

if(c=='y'):
    md=(m*100)/int(m+r+a)
    rd=(r*100)/int(m+r+a)
    ad=(a*100)/int(m+r+a)

    disc=int(input("Enter the discount amount: "))
    m-=(disc*md)/100
    r-=(disc*rd)/100
    a-=(disc*ad)/100

    print(f"M: {int(m)}\nR: {int(r)}\nA: {int(a)}")
    print(f"Total: {int(m+r+a)}")  
    

    
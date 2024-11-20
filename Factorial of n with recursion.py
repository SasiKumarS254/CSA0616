n=int(input("Enter the number"))
res=1 if n==0 or n==1 else n
while n>1:
    n-=1
    res*=n
print(res)

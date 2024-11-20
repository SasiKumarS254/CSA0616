n=int(input("Enter the string= "))
sign= -1 if n<0 else 1
n=abs(n)
rev=int(str(n)[::-1])*sign
print(rev if -2**31<=rev<=2**31-1 else 0)

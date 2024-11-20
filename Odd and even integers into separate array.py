arr=list(map(int,input("ENTER THE NUMBER ").split()))
even=[x for x in arr if x%2==0]
odd=[x for x in arr if x%2!=0]
print(f"THE EVEN ARE {even}")
print(f"THE ODD ARE {odd}")

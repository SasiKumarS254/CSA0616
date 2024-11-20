arr=list(map(int,input("Enter the number").split()))
dup=list({x for x in arr if arr.count(x)>1})
print("Duplicate elements are ",dup if dup else "No elements")

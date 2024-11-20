num1=[2,3,2]
num2=[1,2]
set1=set(num1)
set2=set(num2)
ans1=sum(1 for num in num1 if num in set2)
ans2=sum(1 for num in num2 if num in set1)
print(f"[",ans1,ans2,"]")

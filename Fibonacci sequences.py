terms=int(input(f"ENTER THE NUMBER+ "))
a,b,fib_sum=0,1,0
for i in range(terms):
    fib_sum+=a
    a,b=b,b+a
print(f"THE SUM OF THE FIBANOCCI SEQUENCES IS {fib_sum}")

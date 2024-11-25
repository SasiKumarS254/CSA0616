n = int(input("Enter the number to check prime: "))
m = n // 2
flag = 0

for i in range(2, m + 1):
    if n % i == 0:
        print("Number is not prime")
        flag = 1
        break

if flag == 0:
    print("Number is prime")

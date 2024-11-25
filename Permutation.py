string = "ABC"
n = len(string)

for i in range(1 << n):  # Iterate through all possible combinations
    subset = ""
    for j in range(n):
        if i & (1 << j):  # Check if the j-th bit is set in i
            subset += string[j]
    print(subset)

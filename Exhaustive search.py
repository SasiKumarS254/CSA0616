numbers = [3, 34, 4, 12, 5, 2]
target_sum = 9
n = len(numbers)

found = False
for i in range(1 << n):  # 2^n subsets
    subset = [numbers[j] for j in range(n) if i & (1 << j)]
    if sum(subset) == target_sum:
        print(f"Found subset: {subset}")
        found = True
        break

if not found:
    print("No subset found.")

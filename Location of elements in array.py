arr = list(map(int,input("Enter the array elements separated by spaces: ").split()))
target = int(input("Enter the element to find: "))
if target in arr:
    print(f"Element {target} is found at index {arr.index(target)}")
else:
    print(f"Element {target} is not in the array")

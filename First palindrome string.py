strings=input("Enter the strings= ").split()
palin=next((s for s in strings if s==s[::-1]),None)
if palin:
    print(f"First Palindrome is {palin}")
else:
    print(f"Not Palindrome")

def find_max(lst):
    if not lst:
        return "List is empty"
    return max(sorted(lst))

print(find_max([]))           
print(find_max([5]))          
print(find_max([3, 3, 3, 3])) 

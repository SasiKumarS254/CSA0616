def countPairs(nums, k):
    from collections import defaultdict
    count = 0
    indices = defaultdict(list)
    
    for i, num in enumerate(nums):
        for j in indices[num]:
            if (i * j) % k == 0:
                count += 1
        indices[num].append(i)
    
    return count

nums = [3, 1, 2, 2, 2, 1, 3]
k = 2
print(countPairs(nums, k)) 

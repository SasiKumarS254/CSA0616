weights, values, capacity = [1, 2, 3, 4], [10, 20, 30, 40], 5
n = len(weights)
dp = [[0] * (capacity + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(1, capacity + 1):
        dp[i][w] = dp[i - 1][w]
        if weights[i - 1] <= w:
            dp[i][w] = max(dp[i][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])

print(dp[n][capacity])

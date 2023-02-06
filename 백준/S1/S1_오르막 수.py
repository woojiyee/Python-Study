# DP 다이나믹 프로그래밍

# 규칙 못 찾겠음...
# 블로그

n = int(input())

dp = [1] * 10

for i in range(n-1):
    for j in range(1,10):
        dp[j] += dp[j-1]

print(sum(dp) % 10007)
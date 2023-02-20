# DP 다이나믹 프로그래밍

# 10 -4 3 1 5 6 -35 12 21 -1
# 10 / 6 / 9 / 10 / 15 /21/ -14 / 12 / 33 / 32
# dp[i] = max(이전 항들의 합= dp[i-1],현재 항 a[i])

# 1st

n = int(input())
a = list(map(int,input().split()))
dp = [0] * n

for i in range(n):
    # 전 항까지의 최대 합 + 현재 항(연속된 항의 합), 현재 항 중 큰 값이 dp[i](a[i-1]을 더하지 않을거면 현재항부터 새로 덧셈을 시작해야함)
    dp[i] = max(dp[i-1]+a[i],a[i])

print(max(dp))
        

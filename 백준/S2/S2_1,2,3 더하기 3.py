# DP 다이나믹 프로그래밍

# 1,2,3의 합으로 나타내는 방법 수
# 점화식..
# 수 n
# 1 2 3 4 5 6 7 8 9 10 11 12 13
# 방법 수
# 1 2 4(1+1+1,1+2,2+1,3) 7 
# 5
'''
1+1+1+1+1 + 1(앞뒤 똑같음)
1+1+1+2   + 2(압뒤 다름)
1+1+2+1
1+2+1+1   + 1(앞뒤 다르나 위에 뒤랑 같음)
2+1+1+1   + 1(앞뒤 다르나 위에 뒤랑 같음)
1+2+2     + 3
2+1+2
2+2+1
1+1+3
1+3+1
3+1+1
'''

# 블로그
# 점화식 : A(n) = A(n-1)+ A(n-2)+A(n-3)
# 테스트 케이스 수
t = int(input())
# 입력받은 수
a = [0] * t
# dp[i] = i를 1,2,3의 합으로 나타내는 방법의 수
dp = [0] * 1000001

for i in range(t):
    a[i] = int(input())

dp[1] = 1
dp[2] = 2
dp[3] = 4

for n in range(4,1000001):
    # 저장할 때 1,000,000,009로 안 나누고 print할 때 나눠서 출력하면 "메모리 초과" 뜸
    dp[n] = (dp[n-1]+dp[n-2]+dp[n-3])%1000000009

for i in a:
    print(dp[i])
# 위 for문 두 줄을
'''
[print(dp[i]) for i in a]
'''
# 이렇게 써도 잘 돌아감
# 대신
# [print(dp[i] for i in a)] => 틀렸습니다
# print(dp[i]) for i in a => 컴파일 에러
# 로 됨

# 위 코드는 다 입력을 받고 원하는 알고리즘 동작하게 하고 출력하는 순서였지만
# 아래 코드처럼 알고리즘 코드를 짜놓고 입력 받으면서 출력도 가능

'''
dp = [0 for i in range(1000001)]
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, 1000001):
    dp[i] = ( dp[i - 1] + dp[i - 2] + dp[i - 3] ) % 1000000009

t = int(input())
for i in range(t):
    n = int(input())
    print(dp[n])
'''

# Q. 이전 문제는 n에 대한 dp가 궁금했을 때 반복문도 n까지 돌렸는데
# 지금은 n을 여러(t)개 받으니 그 때 그 때 n이 바뀌니까 그냥 처음부터 n에 들어올 수 있는 n 범위만큼 반복문 돌려서 dp를 만들어 놓는건가?
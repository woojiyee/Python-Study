# 문제
'''
ps 카드에 있는 정보
- 사람들의 아이디
- 얼굴
- 각 카드에는 등급을 나타내는 8종류의 색이 칠해져있다

카드는 카드팩의 형태로만 구매 가능
카드팩의 종류: 
    카드 1개가 포함된 카드팩, 카드 2개가 포함된 카드팩,...,카드 n개가 포함된 카드팩 - n가지가 존재

민규는 카드의 개수가 적은 팩이더라도 가격이 비싸면 높은 등급의 카드가 많이 들어있을 거라는 미신을 믿고 있다.
돈을 최대한 많이 지불해서 카드 n개를 구매하려고 한다.
카드가 i개 포함된 카드팩의 가격은 Pi원이다

문제: 카드 팩의 가격이 주어졌을 때, n개의 카드를 구매하기 위해 민규가 지불해야하는 금액의 최대값을 구하는 프로그램을 작성
( n개보다 많은 수의 카드를 산 다음 일부를 버려서 카드를 n개로 만드는 것은 불가능)

ex)
카드팩 종류 4가지 : P1 = 1, P2 = 5, P3 = 6, P4 = 7
-> 민규가 카드 4개를 갖기 위해 지불해야하는 금액의 최대값은 10원 , 2개 들어있는 카드팩을 2번 구매

P1 = 5, P2= 2, P3 = 8, P4 = 10 -> P1 * 4번 구매 : 민규가 지불해야하는 금액의 최대값 20원

P1 = 3, P2= 5, P3 = 15, P4 = 16 
  -> P1 * 1 + P3 * 1번 구매 : 민규가 지불해야하는 금액의 최대값 18원 
'''

# 아이디어
'''
각 팩당 카드 1개의 가격이 큰 것을 우선시 산다.
Q. P1 = 1, P2= 9, P3 = 15 P4 = 4
    P3 을 사고 p1 *1를 사면 4개를 16원에 사는거니까 1개가 4원
    P2 *2 사면 4개를 18원에 사는거고 한개당 4.5원
    p3이 개당 5원이라 개당 최고가 팩이지만 최종적으로 최대 구매액은 아님
'''

# 1st
'''
# 구매해야하는 카드 n = 팩의 종류 수
n = int(input())

p = [int(input()) for _ in range(n)]

# p[0:0] = [0] # 인덱스 0에 0이 들어감
p.insert(0,0)


# 각 카드팩에서의 카드 1개의 가격
one = [[p[i]//i,i] for i in range(1,n)]

one.insert(0,[0,0])

# 카드 하나의 가격이 가장 비싼 카드팩 먼저 구매
one.sort()

maxPay = []

for i in range(1,n+1):
    for onePay,cnt in one[i]:
        if n % cnt == 0:
            maxPay.append(onePay*n)
        else:
            pack = n // cnt
            spare = n % cnt
            for j in range(i+1,n+1):
                print("계속 빙빙 돔")
            maxPay.append(onePay*pack*cnt + one[spare])
'''
# 코드도 마무리 못 지음

# 2nd
'''
# 구매해야하는 카드 n = 팩의 종류 수
n = int(input())

p = [int(input()) for _ in range(n)]

# p[0:0] = [0] # 인덱스 0에 0이 들어감
p.insert(0,0)

dp = [0] * (n+1)

for i in range(1,n+1):
    dp[i] = max(dp[i-1])
'''
# dp[i]에 i개의 최대값을 저장해야하는건 알겠는데 규칙을 모르겠음

# 3rd ( 블로그 )
# 아이디어
'''
d[1] = p[1]
d[2] = d[1] + p[1] or d[0] + p[2]
d[3] = d[2] + p[1] or d[1] + p[2] or d[0] + p[3]
d[4] = d[3] + p[1] or d[2] + p[2] or d[1] + p[3] or d[0] + p[4]
'''
# 구매해야하는 카드 n = 팩의 종류 수
n = int(input())

p = list(map(int, input().split()))

'''
p = [map(int, input().split())] 
print(p) # [<map object at 0x104b5e680>]
print(type(p)) # <class 'list'>
# [()] 이런거 마냥 리스트 안에 하나의 맵이 있는 형식으로 된 듯
# 문제에서는 map형식을 리스트형식으로 형변환해야하는데 []로는 형변환 된게 아니라 리스트로 감싸지기만 한듯
'''
p.insert(0,0)
# p[0:0] = [0] # 인덱스 0에 0이 들어감
# 한 줄로도 가능 p = [0] + list(map(int, input().split()))

dp = [0] * (n+1)

dp[1] = p[1]

for i in range(2, n + 1):
    for j in range(1, i + 1):
        if dp[i] < dp[i - j] + p[j]:
            dp[i] = dp[i - j] + p[j]
        # dp[i] = max(dp[i], dp[i-k] + p[k])
        # if 문을 한줄로도 표현 가능

print(dp[n])
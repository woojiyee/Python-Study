# 문제
'''
포도주 잔이 일렬로 나열, 포도주 시식할 거다
1. 포도주 잔을 선택하면 그 잔에 들어있는 포도주는
   모두 마셔야하고, 마신 후에는 원래 위치에 다시 놓아야한다.
2. 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.
가능한 많은 양의 포도주를 맛보려고 한다.
6개의 포도주 잔
놓여있는 잔 순서대로의 포도주 양
: 6,10,13,9,8,1
각 잔을 선택할 수도 있고 안 할 수도 있지만 연이어 3번쨰 잔이라면 무조건 선택 할 수 없음
'''

# 1st
'''
# 포도주 잔 개수
n = int(input())

# 각 잔의 포도 양
amount = [int(input()) for _ in range(n)] 

dp = []


def sum(start,s,check):
    # 와인잔을 다 돌았을 때
    if start == n:
        dp.append(s)
        return
    # 이미 연속으로 두번 와인잔이 선택된 상황
    # -> 3번째는 무조건 선택될 수 없음
    if check == 2:
        # 연속으로 더한 횟수를 0으로 초기화
        sum(start+1,s,0)
    else:
        sum(start+1,s+amount[start],check+1)
        sum(start+1,s,0)


sum(0,0,0)

print(max(dp))
'''
# x가 세번째에 오는 경우
# xxx,oxx,...,oox 중 oox가 최대값이므로 oox만 구하면 되는데 위 코드는 하나 하나 다 선택한 경우 = 최대값이 아닌 경우도 다 돌림
# len(dp) = 44


# 2nd
'''
import sys
sys.setrecursionlimit(10000)

# 포도주 잔 개수
n = int(input())

# 각 잔의 포도 양
amount = [int(input()) for _ in range(n)] 

dp = []


def sum(start,s,check,x):
    # 와인잔을 다 돌았을 때
    if start == n :
        if x == n//3:
            dp.append(s)
        return
    # 이미 연속으로 두번 와인잔이 선택된 상황
    # -> 3번째는 무조건 선택될 수 없음
    if check == 2:
        # 연속으로 더한 횟수를 0으로 초기화
        sum(start+1,s,0,x+1)
    else:
        sum(start+1,s+amount[start],check+1,x)
        sum(start+1,s,0,x+1)


sum(0,0,0,0)

print(max(dp))
'''
# vscode서 돌리면 예제는 정답이 나오는데
# 백준 런타임 에러(RecursionError) 뜸
# 그래서 setrecursionlimit 코드 추가해줘도 똑같이 recursionerror 뜸

# 3rd
'''
import sys
sys.setrecursionlimit(10000)

# 포도주 잔 개수
n = int(input())

# 각 잔의 포도 양
amount = [int(input()) for _ in range(n)] 

dp = []


def sum(start,s,check,x):
    # 와인잔을 다 돌았을 때
    if start == n :
        if x == n//3:
            dp.append(s)
        return
    # 이미 연속으로 두번 와인잔이 선택된 상황
    # -> 3번째는 무조건 선택될 수 없음
    if check == 2:
        # 연속으로 더한 횟수를 0으로 초기화
        sum(start+1,s,0,x+1)
    # 3개 덩어리엔 x가 한 개 있을 때가 최대값
    # 3개 덩어리 안에 이미 x가 있다면 나머지 두갠 무조건 선택하기
    # start가 인덱스라 개수보다 1 작으니 +1해주기
    elif (start+1)//3 + 1 == x:
        sum(start+1,s+amount[start],check+1,x)
    else:
        sum(start+1,s+amount[start],check+1,x)
        sum(start+1,s,0,x+1)


sum(0,0,0,0)

print(max(dp))
'''
# vscode서 돌리면 예제는 정답이 나오는데
# 백준 런타임 에러(RecursionError) 뜸

#4th (블로그)
'''
가장 많이 마실 수 있는 상황을 고르면 됨
현재 포도주를 마실지 말지를 결정 할 때
1. 현재 포도주와 이전 포도주를 마시고 전전 포도주는 마시지 않는다 (wine[i]+wine[i-1]+d[i-3])
2. 현재 포도주 o, 이전 포도주 x, 전전 포도주 o (wine[i]+d[i-2])
3. 현재 포도주 x (d[i-1]) (+ d[i-2]+wine[i-1]을 포함한 최댓값이 d[i-1]에 저장돼있기에 d[i-1] 이용)

포도잔이 3잔 이하인 경우에는 인덱스에러 방지를 위해 예외처리 하기
'''

n = int(input())

wine = [int(input()) for _ in range(n)] 

# 각 i번째 와인에서의 와인양 최대값
d = [0]*n

d[0] = wine[0]

# 1<=n이라 n이 1이 될수도 있음 그럼 wine[0]만 존재하고 wine[1]은 없으니 if 안 해주면 index error 뜸
if n > 1:
    d[1] = wine[0] + wine[1]

if n > 2:
    d[2] = max(d[1],wine[0]+wine[2],wine[1]+wine[2])

for i in range(3,n):
    d[i] = max(d[i-1],d[i-3]+wine[i-1]+wine[i],d[i-2]+wine[i])

print(d[n-1])

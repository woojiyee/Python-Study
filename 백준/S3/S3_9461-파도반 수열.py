# 1st
'''
t = int(input())
n= [int(input()) for _ in range(t)]

p = [0] * max(n)

# 문제는 1번째부터 시작하지만 걍 인덱스 0부터 받겠음.
p[0:4] = [1,1,1,2,2]
# 위 코드의 잘못된 점:
# 슬라이싱도 i번째부터 j번째까지 대입하고 싶으면 list[i:j+1] = [...] 해줘야하나봐
# 슬라이싱으로 대입전까진 인덱스 0~11까지 있었는데 대입하니 0~12가 되버림..왠진 몰라

# 앞에서부터 시작
i = 0

for j in range(5,max(n)):
    p[j] = p[i] + p[j-1]
    i += 1

# 잘못된 점:
# 차피 n 리스트에 원하는 수의 번호가 다 있기에 t는 for 돌릴필요 없이 n만 돌리면 됨
for i in range(t):
    for j in n:
        print(p[j-1])
'''

# 2nd
'''
t = int(input())
n= [int(input()) for _ in range(t)]

p = [0] * max(n)

# n이 4 미만일 수도 있음 -> 그럴시 인덱스 에러가 뜰거임
# p[0:5] = [1,1,1,2,2]


if n >= 1:
    p[0] = 1

if n >= 2:
    p[1] = 1

if n >= 3:
    p[2] = 1

if n >= 4:
    p[3] = 2

if n >= 5:
    p[4] = 2




# 앞에서부터 시작
i = 0

for j in range(5,max(n)):
    p[j] = p[i] + p[j-1]
    i += 1


for j in n:
    print(p[j-1])
'''
# 현재 n은 리스트임-> 정수를 담은 변수가 아님
# if n >= 정수 부분에서 런타임에러(TypeError) 발생

# 아이디어
'''
인덱스
수열
0  1  2  3  4   5   6    7   8   9  10
1, 1, 1, 2, 2,  3,  4,   5,  7,  9, 12 ...
=            / 1+2 1+3  1+4 2+5 2+9 3+9 
인덱스 5부터의 각 수열의 값 = 인덱스 0부터 시작해서 수열 + 해당 수열 앞에 수( 수열[인덱스 -1] ) '''
# 3rd

t = int(input())
n= [int(input()) for _ in range(t)]

p = [0] * max(n)

# n이 4 미만일 수도 있음 -> 그럴시 인덱스 에러가 뜰거임
# p[0:5] = [1,1,1,2,2]


if max(n) >= 1:
    p[0] = 1

if max(n) >= 2:
    p[1] = 1

if max(n) >= 3:
    p[2] = 1

if max(n) >= 4:
    p[3] = 2

if max(n) >= 5:
    p[4] = 2

# 앞에서부터 시작
i = 0

for j in range(5,max(n)):
    p[j] = p[i] + p[j-1]
    i += 1

for j in n:
    print(p[j-1])

# 백준 맞았습니다.
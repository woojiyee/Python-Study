# 문제
'''
- i: n+1개, O: n개 -> i와 o가 교대로 나오는 문자열: Pn
- p1:ioi
- p2: ioioi
- p3: ioioioi
- pn ioioi...oi (o가 n개)

i,o로만 이루어진 문자열 s와 정수 n이 주어졌을 때,
s안에 Pn이 몇 군데 포함되어있는지 구하라
'''

# 1st
'''
# Pn 중 o의 개수
n = int(input())

p = "io" * n +"i"

# s 길이
m = int(input())

s = input()

cnt = 0

for i in range(0,m-n):
    if s[i] == "i":
        if s[i:n] == p:
            cnt +=1

print(cnt)'''

# 2nd
'''
# Pn 중 o의 개수
n = int(input())

p = "IO" * n +"I"

# s 길이
m = int(input())

s = input()

cnt = 0

for i in range(0,m-n):
    if s[i] == "I":
        # Pn의 길이는 2n+1 <- n은 O의 개수고 Pn은 IO쌍에 I가 하나 더 추가된 수열
        # 슬라이싱 할 때 리스트[n:m]은 리스트의 인덱스 n~m-1까지 데이터
        isP = s[i:i+2*n+1]
        if isP == p:
            cnt +=1

print(cnt)
'''
# 백준 50점
# 서브태스크
# 1.N ≤ 100, M ≤ 10 000.: 맞았습니다.
# 2.추가적인 제약 조건이 없다.: 시간 초과

# 3rd

'''
# Pn 중 o의 개수
n = int(input())

p = "IO" * n +"I"

# s 길이
m = int(input())

s = input()

cnt = 0

for i in range(0,m-n):
    cnt += s[i:i+2*n+1].count(p)

print(cnt)
'''
# 백준 50점
# 서브태스크
# 1.N ≤ 100, M ≤ 10 000.: 맞았습니다.
# 2.추가적인 제약 조건이 없다.: 시간 초과
# 파이썬에서 arr[a:b]의 시간 복잡도는 O(b-a)다
# -> 슬라이스를 최대한 덜 쓰고 반복을 최소화하는 방법을 찾아야한다.

# 4th (블로그)

# Pn 중 o의 개수
n = int(input())

# s 길이
m = int(input())

s = input()

# s를 돌 때 체킹할 인덱스 위치, ioi rotn, 정답
cursor, count, result = 0,0,0

# while cursor < (m-n) 하면 백준 틀렸습니다 뜸
# 첨엔 차피 p의 길이가 5면 s에서 4개 남았을 때 차피 5글자가 될 수 없는 거 아닌가? 생각했는데
# 현재 코드는 p(io쌍 + i)로 돌리는 게 아니라 한개의 ioi랑 비교하는 거니까 남은게 ioi가 될 수 없는 2개일 땐 확인 할 필요 없음
# -> < m-1은 m-2개까지 하겠다는 거니까 위에 줄을 성립하는 것
while cursor < m-1:
    if s[cursor:cursor + 3] == "IOI":
        count += 1
        cursor += 2
        if count == n:
            result +=1
            count -= 1

    else:
        cursor += 1
        count = 0

print(result)


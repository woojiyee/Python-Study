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
        # i에서부터 Pn인지를 확인하는 거니까 s문자열의 i부터 i+2n+1까지의 데이터를 확인해야함
        # 슬라이싱 할 때 리스트[n:m]은 리스트의 인덱스 n~m-1까지 데이터
        isP = s[i:i+2*n+2]
        if isP == p:
            cnt +=1

print(cnt)
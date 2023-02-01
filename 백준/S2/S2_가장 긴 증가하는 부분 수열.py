# 10 20 10 30 20 50
# array 10 / 10 20 / 10 or 10 20 중 10 20 /10 20 30 / 10 20 or 10 20 30 중 10 20 30 / 10 20 30 50 -> 길이 4

# 10 20 50 30 40
# array 10 / 10 20 / 10 20 50 / 10 20 30 or 10 20 50 둘 다 됨 / 10 20 30 40 or 10 20 50 중 10 20 30 40 -> 4
# 해당 인덱스의 값이 array의 마즈막 항보다 큰가? 
# y->array에 추가
# n -> 해당 인덱스보다 작은 인덱스이면서 값도 작은 항들을 갖는 array를 추가

# 20 10 50 30 20 40
# 20 / [[10] or [20]] / 

# 1st
'''
# 수열의 크기
n = int(input())
# 수열
a = map(int,input().split())

# 증가 수열을 저장할 리스트
array = [[a[0]]]
print(array)

for i in range(1,n):
    if a[i] > a[i-1]:
        array.append(a[i])
    # array의 그 전항과 같으면 무시
    elif a[i] == a[i-1]:
'''

# 2ND
'''
from collections import deque
# 수열의 크기
n = int(input())
# 수열
a = list(map(int,input().split()))

# 증가 수열을 저장할 리스트
array = [[a[0]]]
print(array)

for i in range(1,n):
    for j in range(len(array)):
        if array[j][-1] < a[i]:
            array[j].append(a[i])
        elif array[j][-1] > a[i]:
            queue = deque()
            queue.append(a[i])
            k = i
            l = k - 1
            while l >= 0:
                if a[l] < a[k]:
                    queue.appendleft(a[l])
                    k -= 1
                l -= 1

                
            if len(array[j]) == len(queue):
                array.append(list(queue))
            elif len(array[j]) < len(queue):
                array = [list(queue)]

answer = 0

for i in array:
    answer = max(len(i),answer)

print(answer)
'''
    
# 3rd
'''
# 입력받은 수열 a
# 가장 긴 증가 수열(1차원 리스트)들을 저장하는 (2차원) 리스트 array
# array에 a[0] 대입
# a[1]부터 현재 a 항이 array 리스트 수열들의 마즈막 항보다 큰가?
# 크면 수열들의 마즈막에 추가

# 수열 항 갯수
n = int(input())

# 수열
a = list(map(int,input().split()))

# 증가하는 수열을 받을 리스트
array = [[a[0]]]

for i in range(1,n):
    for j in range(len(array)):
        if array[j][-1] < a[i]:
            array.append(array[j]+[a[i]])

length = 0
for i in array:
    length = max(length,len(i))

print(length)
'''

# 블로그
# 현재 항까지의 증가 수열의 길이를 저장!
# 나는 배열을 저장하려고 했었음!! 배열이 아니라 길이를 저장!

n = int(input())
a = list(map(int,input().split()))

dp = [0] * n

for i in range(n):
    for j in range(i):
        # 현재 원소(a[i])가 이전에 있는 원소(a[j]) 크고 i고정 j 바뀔 때 이전 dp[j] 원수 길이 중 가장 긴 길이를 dp[i]에 저장
        if a[i]> a[j] and dp[i] <dp[j]:
            dp[i] = dp[j]
        # a[i]를 포함해서 +1
    dp[i] += 1

print(max(dp))



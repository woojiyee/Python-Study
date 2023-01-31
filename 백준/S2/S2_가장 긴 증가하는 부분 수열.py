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
            while k >= 0:
                if a[k-1] < a[k]:
                    queue.appendleft(a[k-1])
                k -= 1
            if len(array[j]) == len(queue):
                array.append(list(queue))
            elif len(array[j]) < len(queue):
                array = list(queue)

answer = 0

for i in array:
    answer = max(len(i),answer)

print(answer)

    



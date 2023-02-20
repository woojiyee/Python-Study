# 문제
# 수첩 1 : 실제로 연종이가 하루 동안 본 정수
# 동규 -> 연종 질문: x라는 정수를 본 적 있는가? -> 연종이 대답함
# 수첩 2 : 연종이 봤다고 말한 수

# 1st
'''
#테스트 케이스 수
t = int(input())
# 수첩1 : 실제로 본 수 개수
n = int(input())
real = list(map(int,input().split()))
# 수첩2 : 연종이가 봤다고 한 수 개수
m = int(input())
talk = list(map(int,input().split()))

# 이진 탐색을 위해 정렬하기
real.sort()

def binary_search(start,end,target):
    if start > end:
        print(0)
        return
    mid = (start+end)//2
    if real[mid] == target:
        print(1)
        return
    if real[mid] < target:
        binary_search(mid+1,end,target)
    if target < real[mid]:
        binary_search(start,mid-1,target)

for i in talk:
    binary_search(0,m-1,i)
'''
# 2nd
'''
#테스트 케이스 수
t = int(input())
# 수첩1 : 실제로 본 수 개수

n = [0] * t
real = [[0]* t]
# 수첩2 : 연종이가 봤다고 한 수 개수
m = [0] * t
talk = [[0]* t]

for i in range(t):
    n[i] = int(input())
    real[i] = list(map(int,input().split()))
    # 수첩2 : 연종이가 봤다고 한 수 개수
    m[i] = int(input())
    talk[i] = list(map(int,input().split()))

# 이진 탐색을 위해 정렬하기
real.sort()

def binary_search(t,start,end,target):
    if start > end:
        print(0)
        return
    mid = (start+end)//2
    if real[t][mid] == target:
        print(1)
        return
    if real[t][mid] < target:
        binary_search(t,mid+1,end,target)
    if target < real[t][mid]:
        binary_search(t,start,mid-1,target)

for t in talk:
    for j in t:
        binary_search(t,0,m-1,j)
'''
# 3rd
#테스트 케이스 수
t = int(input())
# 수첩1 : 실제로 본 수 개수

n = [0] * t
real = [0]* t
# 수첩2 : 연종이가 봤다고 한 수 개수
m = [0] * t
talk = [0]* t

for i in range(t):
    n[i] = int(input())
    real[i] = list(map(int,input().split()))
    # 수첩2 : 연종이가 봤다고 한 수 개수
    m[i] = int(input())
    talk[i] = list(map(int,input().split()))

print("real",real)
print("talk",talk)
# 이진 탐색을 위해 정렬하기
for i in range(t):
    real[i].sort()

print("sort 후 real",real)
def binary_search(t,start,end,target):
    if start > end:
        print(0)
        return
    mid = (start+end)//2
    if real[t][mid] == target:
        print(1)
        return
    if real[t][mid] < target:
        binary_search(t,mid+1,end,target)
    if target < real[t][mid]:
        binary_search(t,start,mid-1,target)

for i in range(t):
    for j in talk[i]:
        binary_search(i,0,m[i]-1,j)
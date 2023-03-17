# 1st
'''
# 듣도 못한 사람의 수, 보도 못한 사람의 수
n , m = map(int,input().split())

noListen = []
noSee = []

for i in range(n):
    noListen.append(input())

for i in range(m):
    noSee.append(input())

noListen.sort(key=len)
noSee.sort(key=len)

def binary(list,start,end,target):
    mid = (start+end)//2
    if len(list[mid]) == len(target):
        # 길이가 같을 때 리턴으로 돌릴 수 가 없음
    if len(list[mid]) < len(target):
        return binary(list,start,len(list[mid]),target)
    if len(list[mid]) > len(target):
        return binary(list,len(list[mid]),end,target)
'''

# 2nd

import sys
sys.setrecursionlimit(10000)
# 듣도 못한 사람의 수, 보도 못한 사람의 수
n , m = map(int,input().split())

noListen = []
noSee = []

for i in range(n):
    noListen.append(input())

for i in range(m):
    noSee.append(input())

noListen.sort()
noSee.sort()

answer = []

def binary(start,end,target):
    # start,end = index
    mid = (start+end)//2
    if start > end:
        return
    if noListen[mid] == target:
        answer.append(target)
        return
    elif noListen[mid] > target:
        return binary(start,mid-1,target)
    elif noListen[mid] < target:
        return binary(mid+1,end,target)

for i in noSee:
    binary(0,n-1,i)

answer.sort()

print(len(answer))
for i in answer:
    print(i)
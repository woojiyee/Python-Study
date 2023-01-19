# 이진 탐색

# 문제
# 숫자 카드 두 그룹
# 하나는 탐색 대상 그룹 , 하나는 타겟 그룹
# 타겟 숫자가 탐색 대상 그룹에 몇개가 있는가

# 1st
'''
import sys

# 상근이가 가지고 있는 카드 개수 ( 탐색 대상 그룹 )
n = int(input())
# 상근이가 갖고 있는 카드 ( 탐색 대상 그룹 )
array = list(map(int,sys.stdin.readline().rstrip().split()))

# 타겟 카드 수
m = int(input())
targets = list(map(int,sys.stdin.readline().rstrip().split()))

array.sort()

def binary_search(array,target,start,end):
    if start > end:
        print(0,end=' ')
        return
    mid = (start+end)//2
    if array[mid] == target:
        print(array.count(target),end = ' ')
        return
    elif target < array[mid]:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)

for i in targets:
    binary_search(array,i,0,n-1)
'''
# 시간 초과 뜸
# 리스트에서 count 매서드는 시간 복잡도가 O(n)이래... 그래서 그런가

# 2nd
'''
import sys

# 상근이가 가지고 있는 카드 개수 ( 탐색 대상 그룹 )
n = int(input())
# 상근이가 갖고 있는 카드 ( 탐색 대상 그룹 )
array = list(map(int,sys.stdin.readline().rstrip().split()))

# 타겟 카드 수
m = int(input())
targets = list(map(int,sys.stdin.readline().rstrip().split()))

array.sort()

def binary_search(array,target,start,end):
    if start > end:
        print(0,end=' ')
        return
    mid = (start+end)//2
    if array[mid] == target:
        count = 1
        before = mid
        after = mid
        # 타겟이 여러개라면 대상 그룹을 정렬했으니 타겟이 있는 인덱스 앞 뒤로 타겟과 같은 숫자가 있을 거임
        # 타겟값과 같은 탐색 대상의 중앙값 앞의 대상이 타겟값과 같다면 계속 실행
        while array[before -1] == target:
            count += 1
            before -= 1
            if before < 0:
                break
        while array[after + 1] == target:
            count += 1
            after += 1 
            if after >= n-1:
                break 
        print(count,end=' ')
        return
    elif target < array[mid]:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)

for i in targets:
    binary_search(array,i,0,n-1)

'''
# 이것도 시간 초과 뜸
# 50분 정도 시도하다가 블로그 참고

# 3rd
# 외장 함수  Counter 이용해서 풀기!

import sys
from collections import Counter

# 상근이가 가지고 있는 카드 개수 ( 탐색 대상 그룹 )
n = int(input())
# 상근이가 갖고 있는 카드 ( 탐색 대상 그룹 )
array = list(map(int,sys.stdin.readline().rstrip().split()))

# 타겟 카드 수
m = int(input())
targets = list(map(int,sys.stdin.readline().rstrip().split()))

array_dict = Counter(array)
# Counter(리스트) = 리스트의 요소를 키로 가지고, 리스트에 키의 갯수를 벨루로 가지는 딕셔너리
# Counter(리스트) = {리스트요소 1: 리스트에서 1의 개수,리스트요소 2: 리스트에서 2의 개수,...}

print("딕셔너리",array_dict)

for i in targets:
    print(array_dict.get(i,0),end=' ')

# 4th
# 직접 딕셔너리 만들어서 푸는 방법
N = int(input())
arrN = list(map(int, input().split(' ')))  # 상근이가 가진 숫자 카드

M = int(input())
arrM = list(map(int, input().split(' ')))  # 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 정수

cnt = {} # cnt = dict()

for i in arrN:
    # 이미 cnt 딕셔너리에 있는 키라면 벨루 +1
    # arrN 요소가 첨 들어간 이후면 이미 cnt에 키로 있을 거니까 있을 땐 벨루값 +1, arrN의 i 갯수만큼 i를 키로 가지는 벨루가 됨
    if i in cnt:
        cnt[i] += 1
    # arrN의 요소가 처음 들어갈 때 cnt에 i가 없을 거니까 벨로값 1로 딕셔너리에 추가됨
    else:
        cnt[i] = 1
    #cnt[arrN의 요소] = arrN의 요소가 arrN에 몇개 있는지

for i in arrM:
    # arrM의 요소 i가 cnt에 있다면 arrN에 i의 개수인 cnt[i] 벨루값 출력
    if i in cnt:
        print(cnt[i], end=' ')
    else:
        print(0, end=' ')
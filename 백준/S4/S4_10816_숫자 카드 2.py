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

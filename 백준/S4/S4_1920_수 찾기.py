# 이진 탐색
# 주어진 수열 중에 특정 수가 존재하는 가?
# 탐색 문제
# 탐색 대상 수열의 범위가 100000이하 -> 대상 사이즈가 큼 -> 이진 탐색

#1st
'''
import sys

# 탐색 대상 수열의 갯수
n = int(input())
# 탐색 대상 수열
array = list(map(int,sys.stdin.readline().rstrip().split()))

# 탐색 대상에서 유무를 확인할 타겟 수열의 갯수
m = int(input())
# 타겟 수열
targets = list(map(int,sys.stdin.readline().rstrip().split()))

# 이진 탐색을 위해 탐색 대상 그룹 정렬하기
array.sort()

def binary_search(array,target,start,end):
    if start > end:
        return
    # 타겟과 비교할 중간 인덱스
    mid = (start+end)//2
    if array[mid] == target:
        print(1)
        return
    # target이 중간 데이터보다 작다면 중간값보다 작은 수열의 원소들만 확인하면 됨
    # 끝값을 중간값 앞으로 수정하여 중간값 뒤는 버리기(탐색 대상에서 제외, 타겟과 같은지 비교 체킹 안하기)
    elif target < array[mid]:
        return binary_search(array,target,start,mid-1)
    # target이 중간값보다 크다면 시작 인덱스 바꾸기
    else:
        return binary_search(array,target,mid+1,end)
    print(0)

for i in targets:
    binary_search(array,i,0,n-1)
'''
# 0이 출력안됨

# 2nd
import sys

# 탐색 대상 수열의 갯수
n = int(input())
# 탐색 대상 수열
array = list(map(int,sys.stdin.readline().rstrip().split()))

# 탐색 대상에서 유무를 확인할 타겟 수열의 갯수
m = int(input())
# 타겟 수열
targets = list(map(int,sys.stdin.readline().rstrip().split()))

# 이진 탐색을 위해 탐색 대상 그룹 정렬하기
array.sort()

def binary_search(array,target,start,end):
    # 시작 인덱스가 끝 인덱스보다 작은 경우엔 타겟이 있었을 시 1을 출력하고 함수가 종료됐을 거임.
    # 시작 인덱스가 끝 인덱스보다 큰 경우까지 왔단 거는 오는 와중에 타겟이 대상 수열에 없어서
    # 함수가 종료되지 않았단 거임 -> 수열을 다 돌았는데도 타겟이 발견되지 않았다 -> 대상 수열엔 타겟이 없다
    # 범위가 벗어났을 때 타겟이 없단 의미인 0을 출력
    if start > end:
        print(0)
        return
    # 타겟과 비교할 중간 인덱스
    mid = (start+end)//2
    if array[mid] == target:
        print(1)
        return
    # target이 중간 데이터보다 작다면 중간값보다 작은 수열의 원소들만 확인하면 됨
    # 끝값을 중간값 앞으로 수정하여 중간값 뒤는 버리기(탐색 대상에서 제외, 타겟과 같은지 비교 체킹 안하기)
    elif target < array[mid]:
        return binary_search(array,target,start,mid-1)
    # target이 중간값보다 크다면 시작 인덱스 바꾸기
    else:
        return binary_search(array,target,mid+1,end)
    

for i in targets:
    binary_search(array,i,0,n-1)

# print(1/0)을 탐색 함수 안에 넣을 수도 있고 아님 return부분에 True나 False를 넣고
# 맨 아래 target 돌리는 for문에 함수의 리턴값이 True면 1 출력 이런식으로도 가능

# 푸는데 25분가량 걸림
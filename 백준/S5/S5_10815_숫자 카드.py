# 1st
'''import sys

#상근이가 소유한 카드 개수
n = int(input())
cards = list(map(int,sys.stdin.readline().rstrip().split()))
#for _ in range(n):
#    cards.append(sys.stdin.readline().rstrip())

# 찾을 카드 개수
m = int(input())
targets = list(map(int,sys.stdin.readline().rstrip().split()))

# 이진 탐색을 위해 탐색 전 데이터 정렬하기
cards.sort()
# target은 정렬하면 안 됨 -> 문제에서 타겟 순으로 카드에 타겟의 유무를 1,0으로 출력하라 했으니 순서 바꾸면 안 됨!

def binary_search(array,target,start,end):
    if start <= end:
        # 중간점
        mid = (start+end) // 2
        # 탐색 대상 리스트의 중간점에 있는 데이터가 찾고자하는 타겟과 같을 때
        # 1 출력
        if target == array[mid]:
            return True
        # 타겟이 중간점의 데이터보다 작을 때
        # 중간점 데이터보다 작은 데이터들만 확인 함 (= 끝점을 중간점 앞에 데이터로 변경)
        elif target < array[mid]:
            binary_search(array,target,start,mid-1)
        # 타겟이 중간점의 데이터보다 클 때
        # 중간점 데이터보다 큰 데이터들만 탐색 돌림 (= 시작점을 중간점 뒤 지점으로 변경)
        else:
            binary_search(array,target,mid+1,end)
    # (젤 바깥 binary_search에 포함된 하위 binary_search들이 다 돌고
    # 젤 밖에 있는 binary_search가 다 실행됨 
    # 중간에 타겟이 있었다면 return을 만나서 종료됐을거임
    # return되지 않고 이 부분이 실행됬단 말은 다 돌고도 타겟이 없단 의미
    


for i in targets:
    if binary_search(cards,i,0,n-1) == True:
        print(1,end=' ')
    else:
        print(0,end=' ')
'''
# 함수 안에서 재귀할 때 return안 쓰고 재귀하니 원하는 결과가 출력 안 됨!

#2nd
'''
import sys

#상근이가 소유한 카드 개수
n = int(input())
cards = list(map(int,sys.stdin.readline().rstrip().split()))
#for _ in range(n):
#    cards.append(sys.stdin.readline().rstrip())

# 찾을 카드 개수
m = int(input())
targets = list(map(int,sys.stdin.readline().rstrip().split()))

# 이진 탐색을 위해 탐색 전 데이터 정렬하기
cards.sort()
# target은 정렬하면 안 됨 -> 문제에서 타겟 순으로 카드에 타겟의 유무를 1,0으로 출력하라 했으니 순서 바꾸면 안 됨!

def binary_search(array,target,start,end):
    if start <= end:
        # 중간점
        mid = (start+end) // 2
        # 탐색 대상 리스트의 중간점에 있는 데이터가 찾고자하는 타겟과 같을 때
        # 1 출력
        if target == array[mid]:
            return True
        # 타겟이 중간점의 데이터보다 작을 때
        # 중간점 데이터보다 작은 데이터들만 확인 함 (= 끝점을 중간점 앞에 데이터로 변경)
        elif target < array[mid]:
            return binary_search(array,target,start,mid-1)
        # 타겟이 중간점의 데이터보다 클 때
        # 중간점 데이터보다 큰 데이터들만 탐색 돌림 (= 시작점을 중간점 뒤 지점으로 변경)
        else:
            return binary_search(array,target,mid+1,end)
    # (젤 바깥 binary_search에 포함된 하위 binary_search들이 다 돌고
    # 젤 밖에 있는 binary_search가 다 실행됨 
    # 중간에 타겟이 있었다면 return을 만나서 종료됐을거임
    # return되지 않고 이 부분이 실행됬단 말은 다 돌고도 타겟이 없단 의미
    


for i in targets:
    if binary_search(cards,i,0,n-1) == True:
        print(1,end=' ')
    else:
        print(0,end=' ')
'''


import sys

#상근이가 소유한 카드 개수
n = int(input())
cards = list(map(int,sys.stdin.readline().rstrip().split()))
'''for _ in range(n):
    cards.append(sys.stdin.readline().rstrip())'''

# 찾을 카드 개수
m = int(input())
targets = list(map(int,sys.stdin.readline().rstrip().split()))

# 이진 탐색을 위해 탐색 전 데이터 정렬하기
cards.sort()

def binary_search(array,target,start,end):
    if start <= end:
        # 중간점
        mid = (start+end) // 2
        # 탐색 대상 리스트의 중간점에 있는 데이터가 찾고자하는 타겟과 같을 때
        # 1 출력
        if target == array[mid]:
            print(1,end=' ')
            return 
        # 타겟이 중간점의 데이터보다 작을 때
        # 중간점 데이터보다 작은 데이터들만 확인 함 (= 끝점을 중간점 앞에 데이터로 변경)
        elif target < array[mid]:
            return binary_search(array,target,start,mid-1)
        # 타겟이 중간점의 데이터보다 클 때
        # 중간점 데이터보다 큰 데이터들만 탐색 돌림 (= 시작점을 중간점 뒤 지점으로 변경)
        else:
            return binary_search(array,target,mid+1,end)
    # (젤 바깥 binary_search에 포함된 하위 binary_search들이 다 돌고
    # 젤 밖에 있는 binary_search가 다 실행됨 
    # 중간에 타겟이 있었다면 return을 만나서 종료됐을거임
    # return되지 않고 이 부분이 실행됬단 말은 다 돌고도 타겟이 없단 의미
    print(0,end=' ')


for i in targets:
    binary_search(cards,i,0,n-1)

# 2,3rd 둘 다 맞음! 
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
# 아이디어
'''
문자열도 첫글자 a,b,c 또는 ㄱ,ㄴ,ㄷ으로 크기 비교 가능 -> 이걸 이용
중간값 계산은 (시작값 + 끝값)//2라 숫자여야 함 -> 인덱스 이용
타겟이 인덱스가 mid인 문자열보다 크다 = 사전순으로 뒤에있다를 의미
리스트도 정렬해놨으니 사전순으로 되어있음 시작값을 미드 뒤로 옮기기 
'''

# 듣도 못한 사람의 수, 보도 못한 사람의 수
n , m = map(int,input().split())

noListen = []
noSee = []

for i in range(n):
    noListen.append(input())

for i in range(m):
    noSee.append(input())

# 문자열이 있는 리스트를 sort하면 ㄱ,ㄴ,ㄷ순으로 정렬됨
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
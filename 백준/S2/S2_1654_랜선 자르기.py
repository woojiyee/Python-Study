# 문제
'''
만들어야하는 같은 길이의 랜선 n개
갖고있는 제각각 길이의 랜선 k개 (k <= n)
k개를 잘라서 n개의 랜선을 만든다 
n개보다 많이 만드는 것도 n개를 만드는 것에 포함됨
만들 수 있는 최대 랜선의 길이를 구하라
'''

# 1st
'''
# 랜선의 개수, 필요한 개수
k, n = map(int,input().split())

graph = []

for i in range(k):
    graph.append(int(input()))

graph.sort()

#length = [i for i in range(1,graph[0])]

def binary(start,end):
    if start <= end:
        mid = (start+end)//2
        cnt = 0
        for i in graph:
            # mid는 랜선 길이
            # cnt는 해당 길이로 만들 수 있는 랜선 개수
            cnt += i//mid
        # cnt가 필요한 랜선 개수보다 작다
        # 하나의 랜선 길이가 커서 나눴을 때 몫이 랜선 수보다 작은 것
        # 현재 랜선 길이보다 작은 랜선길이들을 체크해야함
        if cnt < n:
            binary(start,mid)
        elif cnt == n:
            return mid
        elif cnt > n:
            binary(mid+1,end)
        
print(binary(1,graph[0]))
'''
# 1st 백준 컴파일 에러 뜸
# vscode서 돌려도 None 출력

# 2nd
'''
# 랜선의 개수, 필요한 개수
k, n = map(int,input().split())

graph = []

for i in range(k):
    graph.append(int(input()))

graph.sort()

#length = [i for i in range(1,graph[0])]

def binary(start,end):
    if start > end:
        return end
    mid = (start+end)//2
    cnt = 0
    for i in graph:
        # mid는 랜선 길이
        # cnt는 해당 길이로 만들 수 있는 랜선 개수
        cnt += i//mid
    # cnt가 필요한 랜선 개수보다 작다
    # 하나의 랜선 길이가 커서 나눴을 때 몫이 랜선 수보다 작은 것
    # 현재 랜선 길이보다 작은 랜선길이들을 체크해야함
    if cnt < n:
        binary(start,mid-1)
    else:
        binary(mid+1,end)
    
    #elif cnt == n:
    #    return mid
    
    # cnt > n:
    
        
print(binary(1,graph[-1]))
'''
# 2nd 백준 컴파일 에러 뜸
# vscode서 돌려도 None 출력


# 3rd

# 랜선의 개수, 필요한 개수
k, n = map(int,input().split())

graph = []

for i in range(k):
    graph.append(int(input()))

graph.sort()

#length = [i for i in range(1,graph[0])]

def binary(start,end):
    if start > end:
        return end
    mid = (start+end)//2
    cnt = 0
    for i in graph:
        # mid는 랜선 길이
        # cnt는 해당 길이로 만들 수 있는 랜선 개수
        cnt += i//mid
    # cnt가 필요한 랜선 개수보다 작다
    # 하나의 랜선 길이가 커서 나눴을 때 몫이 랜선 수보다 작은 것
    # 현재 랜선 길이보다 작은 랜선길이들을 체크해야함
    if cnt < n:
        return binary(start,mid-1)
    else:
        return binary(mid+1,end)
    '''
    elif cnt == n:
        return mid
    '''
    # cnt > n:
    
        
print(binary(1,graph[-1]))

# 백준 맞았습니다 뜸
# + elif주석 풀고 위치에 맞게 수정해도 백준 틀렸습니다 뜸
# + binary(1,graph[0])하면 문제 예제는 정답 뜨지만 백준 틀렸습니다 뜸
# 예를 들어 10,100, 200, 400 이고 n이 7일 때 정답인 랜선 길이가 100임 -> 그러므로 입력받는 k개의 랜선 중 최소 길이가 end가 되면 안 되고 최대 길이가 end가 되야함
# 문제
'''
A[i][j] = i*j (요소가 행 * 열)인 n*n 배열을 
일차원 배열 B로 바꾼 후(a의 2행 1열이 b의 4번째 요소인 셈) 
오름차순 했을 때 b[k]

입력
배열 크기 n,배열 b에서 원하는 값의 인덱스 k
'''

# 1st

n = int(input())
k = int(input())

graph = [[i*j] for i in range(n+1) for j in range(n+1)]

def binary(start,end):
    cnt = 0
    if start > end:
        return end
    # mid는 요소 값
    mid = (start + end) //2
    for i in range(1,n+1):
        for j in range (1,n+1):
            if mid > graph[i][j]:
                cnt += 1
    # mid 요소 값보다 작은 graph[i][j] 요소들이 k개보다 많다
    # = mid가 k번째 요소가 아닌 것

# 어떻게 코드를 짜야할지 모르겠음

# 2nd( 블로그 )
n, k = int(input()), int(input())

start, end = 1, k

while start <= end:
    mid = (start + end) // 2

    cnt = 0
    for i in range(1,n+1):
        cnt += min(mid // i, n)
        # cnt += mid // i
        # min 안 해주면 백준 틀렸습니다 뜸
        # 한 행에 mid보다 작은 수의 개수는 열의 개수를 넘을 수 없음 -> min으로 열의 개수 n 처리

    if cnt >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)

# 백준 맞았습니다
# 수 A를 입력받고  수열 D를 구해서 리스트에 저장
# 중복 체킹 ( 계산된 항이 이전에 있던 항과 같은 값인가? -> in 이용 )

# 1st
# 수열 첫 항 a1, 지수 p
'''
a , p = map(int,input().split())
# 수열 d
d = list()
'''
# 코드를 어케 짜야할지 가늠도 안 감
# 블로그 참고

def next(a,p):
    a = str(a)
    answer = 0
    for i in a:
        answer += pow(int(i),p)
    return answer

def dfs(a,p,count,check):
    if check[a]!=0:
        return check[a]-1
    check[a]=count
    b = next(a,p)
    count += 1
    return dfs(b,p,count,check)

# 항의 최대 값은 9^5 + 9^5 + 9^5 + 9^5 = 250000
# 중복 체크를 항으로 나올 수 있는 값만큼의 크기를 가지는 리스트 생성
# -> 인덱스와 같은 값의 항이 나오면 체킹 -> 중복 체크하는데 이용?
# 초기화를 0으로 -> 항이 체킹 되면 값을 대입 -> 0이 아닌 값이 들어있으면 이미 나온 적 있는 값 -> 중복으로 인식
check = [0] * 250000
a, p = map(int,input().split())
# 중복되지 않은 항들 갯수 세는 변수
# 전항을 계산해서 수열 규칙으로 현재 항을 구했을 때 이전에 나왔던 값이 아니면 카운팅
count = 1
# 첫 항의 dfs만 돌려도 dfs 함수 안에서 그 다음 항의 dfs가 실행되기에 따로 for문이 필요 없음
print(dfs(a,p,count,check))

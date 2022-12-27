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

check = [0] * 250000
a, p = map(int,input().split())
count = 1
print(dfs(a,p,count,check))

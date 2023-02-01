# 18kg
# 5*3 + 3*1 / 5 *1,2 + 3* x / 5*0 + 3*6
# 봉지 갯수 : 4 / x / 6

# 4kg
# 5*0 3의 배수도 x -> -1 출력

# 6kg
# 5*1 + 3 배수 x / 3*2

'''알고리즘
1. 5로 나눈 자연수 몫(k)으로 입력받은 무게로 나눴을때 나머지가 3의 배수인가?
-> 5로 나눈 몫과 나머지를 3으로 나눈 몫이 봉지수 -> 저장
2. 5로 나눈 자연수 몫(k)으로 입력받은 무게로 나눴을때 나머지가 3의 배수가 아니라면 따로 저장 없이 다음 k-1 진행
1-2. 입력받은 수를 k-1로 나눈 나머지가 3의 배수인가? 맞다면 1번 진행
최소 봉지 수는 5가 우선시'''

#1st

n = int(input())

# 5로 나누었을 때 몫
m = n // 5

# 5로 나눈 몫이 0일 때 포함 봉지개수를 담는 리스트
count = []

while m >=0:
    # 5의 배수인가?
    if n == 5*m :
        count.append(m)
        # 다음 케이스? 5킬로그램 봉지 수를 줄여가며 구하기
        m -= 1
    # 5로 나눈 나머지가 3의 배수인가?
    elif (n - 5*m) % 3 == 0:
        count.append(m+((n - 5*m)//3))
        m -= 1
    # 5의 배수도 3의 배수도 아닐 때
    else:
        # 따로 저장하지 않음
        m -= 1

# 빈 배열일 때
if not count: # 비어있는 리스트를 확인할 수 있는 코드
    print(-1)
else:
    print(min(count))


 
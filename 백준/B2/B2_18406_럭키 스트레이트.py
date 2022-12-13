# 수도 코드
'''
1. 점수 N을 문자열로 입력받기
2. 문자열 길이 저장
3. 0~ 문자 길이 반까지의 문자열을 for문 돌리고 int형으로 변환하여 더하기
4. 문자 길이 반+1 ~ 끝까지의 문자열을 for문 돌리고 int형으로 변환하여 더하기
5. 3번과 4번이 같은지 확인 -> 그에 맞게 출력
'''

# 점수 
N = input("점수 :")

len = len(N)

# 오른쪽 합
Rsum = 0
# 왼쪽 합
Lsum = 0

for i in range(len//2):
    Rsum += int(N[i])

for i in range(len//2,len):
    Lsum += int(N[i])

if Rsum == Lsum :
    print("LUCKY")
else:
    print("READY")

# 소요 시간 약20분
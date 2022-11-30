"""
+ 테스트 케이스 수 입력받기
+ 테스트 케이스 리스트/배열에 입력받기
+ 테스트 케이스 리스트 요소 반복문 돌려서 각 테스트케이스마다 총점 구하기
1. ox 문제 정답,오답을 담는 배열/리스트로 입력받기
    -> 테스트 케이스 리스트의 원소인 ox가 문자열이라 바로 인덱싱 가능
2. 현재 요소가 x이면 0 , o이면 아래 조건에 따라 +1 => 각 문제의 점수를 담고있는 배열 선언
3. 전값이 0 o이면 0+1, 전값이 0이 아니면 전값+1
    -> 현재 값이 x 이면 0, o 이면 전값 +1( 전값이 0인지 아닌지는 상관 없고 현재가 o인지에 따라 결과가 달라지기에 2,3번을 합쳐서 변경)
    + 현재 답이 o이면 전값에 +1 하므로 첫번째 답은 전값이 필요 -> 각 문제의 점수를 담고있는 배열을 ox 문자열의 길이보다 하나 크게 선언하고 0으로 초기화
    + ox문자열의 길이를 알아야하기에 len()활용하여 문자열 길이를 담은 변수도 정의
+ 총점 변수 선언
+ 점수 변수 원소들을 반복문 이용하여 총점 변수에 더하기
4. 총점 출력

"""

#1st
'''ox = list(input("ox 입력:").split())
print(ox)'''

#2nd
'''ox = input("ox 입력:")
print(ox[0])
print(ox[1])
print(ox[2])

문자열은 인덱싱 가능, 인덱스는 0부터 시작'''

#3rd
'''    ox = input("ox 입력:")
    받은 문자열 길이
    length = len(ox)
    시작 하는 ox 전 점수를 넣기 위해 받은 문자열 길이보다 1 큰 배열
    score[length+1] = 0'''


#4th
"""ox = input("ox 입력:")
length = len(ox)
score = [0 for i in range(length+1)]
total = 0

for i in range(length) :
    if ox[i] == "x" :
        score[i+1] = 0
    else:
        score[i+1] = score[i]+1

for i in score:
    total += i

print("ox 총점:",total)


한 테스트케이스 점수 구하는 코드
문제는 테스트케이스가 여러개"""

#5ft

count = int(input("테스트 케이스 갯수 입력:"))
osList = []

for i in range(count):
    osList.append(input("테스트 케이스 입력:"))

#테스트 케이스 돌리는 반복문
for i in osList:
    length = len(i)
    #print("테스트케이스 문자열 길이:",length)
    score = [0 for i in range(length+1)]
    ''' print("점수 배열:",score,"배열 크기:",len(score))
    print("i[0]:",i[0])
    print("i[1]:",i[1])
    print("i[2]:",i[2])
    문자열은 따로 리스트 선언한 변수에 안 담아도 인덱싱 가능'''
    for j in range(length):
        if i[j] == "x":
            score[j+1] = 0
        else:
            score[j+1] = score[j]+1

    #총 점수
    total = 0
    
    for k in score:
        total += k

    print(total)

#백준 문제에서 주어지는 ox는 대문자 ox라서 백준서 맞추려면 if부분 X로 바꾸면 됨
# 검색 및 푸는데 걸린 시간 : 대량 1시간
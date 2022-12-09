# 수도 코드
'''
1. 지도 값 2차원 리스트로 입력받기
2. 단지명 = 1
3. 지도의 현 위치에 집 여부가 1?
   -> 0열 (왼쪽이 없음) -> 위만 확인  
      : j=0 ? 위 집 여부가 0이 아닌가? 현재 집 값을 위 집 단지명으로 변경
   -> 0 행 (위가 없음) -> 왼쪽만 확인
      : i = 0 ? 왼쪽집 여부가 0이 아닌가? 현재 집 값을 위 집 단지명으로 변경
   -> 0열, 0행이 아닌 나머지 -> 왼쪽,위 확인
        i,j != 0? 왼쪽 집 여부가 0이 아닌가? 현재 집 값을 왼쪽 집 단지명으로 변경
                위 집 여부가 0이 아닌가? 현재 집 값을 위 집 단지명으로 변경

     집 여부가 0이 아닌가? -다음 조건문-> 0인가? 단지명 +=1, 현재 집 값에 변경된 단지명으로 변경
4. 만들어진 단지명 리스트 만들기 list = [i for i in range(단지명)]
5. 총 단지수 출력 print(len(단지명))
6. 단지별 집 수를 담는 리스트 count
7. 단지명(요인) 반복해서 지도에서 단지명 요소들이 각각 몇개있는지 세서 count에 넣기
8. 단지수 리스트 오름차순 정렬
9. count 출력
'''

#1st
'''
# 지도의 크기 
n = int(input(" 지도의 크기 "))

# 지도: 집 여부 리스트
map = [[0 for i in range(n)] for i in range(n)]
#map = list(())

# 단지 번호
group = 1

print(map)

for i in range(n):
    # 지도 한 줄 받을 임시 변수
    line = input('집의 여부 입력:')
    # 띄어쓰기 없이 입력되는 집 여부값 문자열을 집 단위로 리스트에 담기
    for j in range(n):
        #print(line)
        #print(line[j])
        #print("i,j 자료형:",type(i),type(j))
        #print(map[i][j])
        map[i][j] = line[j]

# 2중 배열이 잘 들어갔는지 확인
#print(map)

for i in range(n):
    for j in range(n):
        # 지도 속 위치에 집이 있을 때
        if map[i][j] == '1':
            #0행 0열에 위치 -> 위와 왼쪽에 집이 없음
            if i == '0' & j =='0':
                # 해당 위치에 집이 있을 때
                if map[i][j] == '1':
                    # 위치에 단지번호/ 그룹번호로 재할당
                    map[i][j]= group
            # 0행에 있는 집인가? -> 위에 집이 없음, 왼쪽 집 여부만 확인
            elif i =='0':
                # 왼쪽에 집이 있으면
                if map[i][j-1] == '1':
                    # 왼쪽 집에 그룹번호가 들어가있을 거임
                    # 같은 그룹 번호로 재할당
                    map[i][j] = map[i][j-1]
                # 왼쪽에 집이 없으면
                else:
                    # 새로운 그룹이기에 그룹 번호를 1증가 시켜줌
                    group += 1
                    # 새로운 그룹(그 전 그룹번호의 다음 그룹 번호)로 재할당
                    map[i][j] = group
            # 0열에 있는 집인가? -> 왼쪽에 집이 없음, 위쪽 집 여부만 확인
            elif j == '0':
                if map[i-1][j] == '1':
                    map[i][j] = map[i-1][j]
                else:

#1st 잘못 된 점
왼쪽,위 집의 여부만 확인할 시, 현재 위치에 집이 있는데 위에는 없고 오른쪽에 집이 있을시 오른쪽 집과 같은 단지여야하는데 오른쪽 체킹이 안 됨....
'''

# 2nd
'''
# 지도의 크기
n = int(input("지도의 크기 :"))

# 집 여부를 받는 지도 리스트
map = [[0 for _ in range(n)] for _ in range(n)]

# 단지/ 그룹 번호
group = 0

# 단지별 집 수 받을 리스트
cnt= list()

for i in range(n):
    # 지도 한 줄 받을 임시 변수
    line = input('집의 여부 입력:')
    # 띄어쓰기 없이 입력되는 집 여부값 문자열을 집 단위로 리스트에 담기
    for j in range(n):
        #print(line)
        #print(line[j])
        #print("i,j 자료형:",type(i),type(j))
        #print(map[i][j])
        map[i][j] = line[j]

print(map)
# map의 요소 타입확인
#print(type(map[2][3]))

for i in range(n):
    for j in range(n):
        print("for문 잘 돌아감")
        # 현재 집이 그룹 번호를 가지고 있는 경우
        if type(map[i][j]) == int :
            # 마즈막행이 아닌 경우
            if i != n-1:
                # 현재 집의 아래 위치에도 집이 있는가?
                if map[i+1][j] == '1':
                    # 현재 집과 같은 그룹 번호를 줌
                    map[i+1][j] = map[i][j]
        # 현재 집이 그룹 번호를 가지고 있지 않는 경우 중 현재 집 여부가 1인 경우
        elif map[i][j] == '1':
            # 첫번째 열인 경우 - 왼쪽 집이 없음 -> 오른쪽 집만 그룹 여부 체크
            if j == 0:
                # 오른쪽 집이 그룹 번호가 있는 경우
                if type(map[i][j+1]) == int :
                    map[i][j] = map[i][j+1]
                    # 마즈막행이 아닌 경우
                    if i != n-1:
                        # 현재 집의 아래 위치에도 집이 있는가?
                        if map[i+1][j] == '1':
                            # 현재 집과 같은 그룹 번호를 줌
                            map[i+1][j] = map[i][j]
                # 오른쪽 집이 그룹 번호가 없는 경우
                else:
                    group += 1
                    print("새 그룹 번호:",group)
                    # 새 그룹 번호를 넣어줌
                    map[i][j] = group

                    print("map[",i,"][",j,"] =", group)
                    print("map[i][j] type:", type(map[i][j]))
                    # 마즈막행이 아닌 경우
                    if i != n-1:
                        # 현재 집의 아래 위치에도 집이 있는가?
                        if map[i+1][j] == '1':
                            # 현재 집과 같은 그룹 번호를 줌
                            map[i+1][j] = map[i][j]
            # 젤 오른쪽 열인 경우 - 오른쪽 집이 없음 -> 왼쪽 집만 그룹 여부 체크
            elif j == n-1 :
                # 왼쪽 집이 그룹 번호가 있는 경우
                if type(map[i][j-1]) == int :
                    map[i][j] = map[i][j-1]
                    # 마즈막행이 아닌 경우
                    if i != n-1:
                        # 현재 집의 아래 위치에도 집이 있는가?
                        if map[i+1][j] == '1':
                            # 현재 집과 같은 그룹 번호를 줌
                            map[i+1][j] = map[i][j]
                # 왼쪽 집이 그룹 번호가 없는 경우
                else:
                    group += 1
                    print("새 그룹 번호:",group)
                    # 새 그룹 번호를 넣어줌
                    map[i][j] = group

                    print("map[",i,"][",j,"] =", group)
                    print("map[i][j] type:", type(map[i][j]))
                    # 마즈막행이 아닌 경우
                    if i != n-1:
                        # 현재 집의 아래 위치에도 집이 있는가?
                        if map[i+1][j] == '1':
                            # 현재 집과 같은 그룹 번호를 줌
                            map[i+1][j] = map[i][j]
            # 젤 왼쪽 열도 오른쪽 열도 아닌 경우
            # 현재 집의 좌우 집에 그룹 변호가 있는 경우
            elif type(map[i][j+1]) == int and type(map[i][j-1]) == int :
                # 현재 집을 기준으로 좌우집의 그룹 번호가 다른 경우
                if map[i][j-1] != map[i][j+1] :
                    # 그룹 번호 하나로 통일
                    # 왼쪽 집 그룹번호로 통일하겠음
                    map[i][j] = map[i][j-1]
                    # 지도 리스트에서 우측 집 그룹번호가 담겨있는 위치의 요소를 좌측집에 담겨있는 그룹번호로 바꿈
                    # map.replace(map[i][j+1],map[i][j-1])
                    # list엔 replace못 씀
                    for k in range(i+1):
                        for l in range(j+2):
                            if map[k][l] == map[i][j+1]:
                                map[k][l] = map[i][j-1]
                    # 마즈막행이 아닌 경우
                    if i != n-1:
                        # 현재 집의 아래 위치에도 집이 있는가?
                        if map[i+1][j] == '1':
                            # 현재 집과 같은 그룹 번호를 줌
                            map[i+1][j] = map[i][j]
            # 나머지 경우
            # 왼쪽 집이 그룹 번호가 있는 경우
            elif type(map[i][j-1]) == int :
                map[i][j] = map[i][j-1]
                # 마즈막행이 아닌 경우
                if i != n-1:
                    # 현재 집의 아래 위치에도 집이 있는가?
                    if map[i+1][j] == '1':
                        # 현재 집과 같은 그룹 번호를 줌
                        map[i+1][j] = map[i][j]
            # 오른쪽 집이 그룹 번호가 있는 경우
            elif type(map[i][j+1]) == int :
                map[i][j] = map[i][j+1]
                # 마즈막행이 아닌 경우
                if i != n-1:
                    # 현재 집의 아래 위치에도 집이 있는가?
                    if map[i+1][j] == '1':
                        # 현재 집과 같은 그룹 번호를 줌
                        map[i+1][j] = map[i][j]
            # 좌우집 다 그룹 번호가 없는 경우
            else:
                group += 1
                print("새 그룹 번호:",group)
                # 새 그룹 번호를 넣어줌
                map[i][j] = group

                print("map[",i,"][",j,"] =", group)
                print("map[i][j] type:", type(map[i][j]))
                # 마즈막행이 아닌 경우
                if i != n-1:
                    # 현재 집의 아래 위치에도 집이 있는가?
                    if map[i+1][j] == '1':
                        # 현재 집과 같은 그룹 번호를 줌
                        map[i+1][j] = map[i][j]
print("i am map",map)
# 그룹 번호별 갯수를 리스트에 담기

print("map에서 1의 갯수:", map.count(1))

for i in range(group):
    print('i의 타입',type(i))
    print('추가되는 요소의 타입', type(map.count(i)))
    cnt.append(map.count(i))

# 그룹당 수를 오름차순으로 정렬
cnt.sort()

print("오름 차순 정렬 후 그룹 리스트 :",cnt)

# 총 단지수 : 집의 수가 0개가 아닌 그룹의 수
print("단지 수:",len(cnt)-cnt.count(0))


# 집 갯수가 0 초과인 그룹 중 오름차순으로 출력
for i in cnt:
    print("단지별 집 수 오름차순 출력 for문")
    if i > 0:
        print(i)
'''        

#3rd
'''
# 지도의 크기
n = int(input("지도의 크기 :"))

# 집 여부를 받는 지도 리스트
map = [[0 for _ in range(n)] for _ in range(n)]

# 단지/ 그룹 번호
group = 0


for i in range(n):
    # 지도 한 줄 받을 임시 변수
    line = input('집의 여부 입력:')
    # 띄어쓰기 없이 입력되는 집 여부값 문자열을 집 단위로 리스트에 담기
    for j in range(n):
        #print(line)
        #print(line[j])
        #print("i,j 자료형:",type(i),type(j))
        #print(map[i][j])
        map[i][j] = line[j]

print(map)
# map의 요소 타입확인
#print(type(map[2][3]))

for i in range(n):
    for j in range(n):
        print("for문 잘 돌아감")
        # 현재 집이 그룹 번호를 가지고 있는 경우
        if type(map[i][j]) == int :
            # 마즈막행이 아닌 경우
            if i != n-1:
                # 현재 집의 아래 위치에도 집이 있는가?
                if map[i+1][j] == '1':
                    # 현재 집과 같은 그룹 번호를 줌
                    map[i+1][j] = map[i][j]
        # 현재 집이 그룹 번호를 가지고 있지 않는 경우 중 현재 집 여부가 1인 경우
        elif map[i][j] == '1':
            # 첫번째 열인 경우 - 왼쪽 집이 없음 -> 오른쪽 집만 그룹 여부 체크
            if j == 0:
                # 오른쪽 집이 그룹 번호가 있는 경우
                if type(map[i][j+1]) == int :
                    map[i][j] = map[i][j+1]
                    # 마즈막행이 아닌 경우
                    if i != n-1:
                        # 현재 집의 아래 위치에도 집이 있는가?
                        if map[i+1][j] == '1':
                            # 현재 집과 같은 그룹 번호를 줌
                            map[i+1][j] = map[i][j]
                # 오른쪽 집이 그룹 번호가 없는 경우
                else:
                    group += 1
                    print("새 그룹 번호:",group)
                    # 새 그룹 번호를 넣어줌
                    map[i][j] = group

                    print("map[",i,"][",j,"] =", group)
                    print("map[i][j] type:", type(map[i][j]))
                    # 마즈막행이 아닌 경우
                    if i != n-1:
                        # 현재 집의 아래 위치에도 집이 있는가?
                        if map[i+1][j] == '1':
                            # 현재 집과 같은 그룹 번호를 줌
                            map[i+1][j] = map[i][j]
            # 젤 오른쪽 열인 경우 - 오른쪽 집이 없음 -> 왼쪽 집만 그룹 여부 체크
            elif j == n-1 :
                # 왼쪽 집이 그룹 번호가 있는 경우
                if type(map[i][j-1]) == int :
                    map[i][j] = map[i][j-1]
                    # 마즈막행이 아닌 경우
                    if i != n-1:
                        # 현재 집의 아래 위치에도 집이 있는가?
                        if map[i+1][j] == '1':
                            # 현재 집과 같은 그룹 번호를 줌
                            map[i+1][j] = map[i][j]
                # 왼쪽 집이 그룹 번호가 없는 경우
                else:
                    group += 1
                    print("새 그룹 번호:",group)
                    # 새 그룹 번호를 넣어줌
                    map[i][j] = group

                    print("map[",i,"][",j,"] =", group)
                    print("map[i][j] type:", type(map[i][j]))
                    # 마즈막행이 아닌 경우
                    if i != n-1:
                        # 현재 집의 아래 위치에도 집이 있는가?
                        if map[i+1][j] == '1':
                            # 현재 집과 같은 그룹 번호를 줌
                            map[i+1][j] = map[i][j]
            # 젤 왼쪽 열도 오른쪽 열도 아닌 경우
            # 현재 집의 좌우 집에 그룹 변호가 있는 경우
            elif type(map[i][j+1]) == int and type(map[i][j-1]) == int :
                # 현재 집을 기준으로 좌우집의 그룹 번호가 다른 경우
                if map[i][j-1] != map[i][j+1] :
                    # 그룹 번호 하나로 통일
                    # 왼쪽 집 그룹번호로 통일하겠음
                    map[i][j] = map[i][j-1]
                    # 지도 리스트에서 우측 집 그룹번호가 담겨있는 위치의 요소를 좌측집에 담겨있는 그룹번호로 바꿈
                    # map.replace(map[i][j+1],map[i][j-1])
                    # list엔 replace못 씀
                    for k in range(i+1):
                        for l in range(j+2):
                            if map[k][l] == map[i][j+1]:
                                map[k][l] = map[i][j-1]
                    # 마즈막행이 아닌 경우
                    if i != n-1:
                        # 현재 집의 아래 위치에도 집이 있는가?
                        if map[i+1][j] == '1':
                            # 현재 집과 같은 그룹 번호를 줌
                            map[i+1][j] = map[i][j]
                else:
                    map[i][j] = map[i][j-1]
            # 나머지 경우
            # 왼쪽 집이 그룹 번호가 있는 경우
            elif type(map[i][j-1]) == int :
                map[i][j] = map[i][j-1]
                # 마즈막행이 아닌 경우
                if i != n-1:
                    # 현재 집의 아래 위치에도 집이 있는가?
                    if map[i+1][j] == '1':
                        # 현재 집과 같은 그룹 번호를 줌
                        map[i+1][j] = map[i][j]
            # 오른쪽 집이 그룹 번호가 있는 경우
            elif type(map[i][j+1]) == int :
                map[i][j] = map[i][j+1]
                # 마즈막행이 아닌 경우
                if i != n-1:
                    # 현재 집의 아래 위치에도 집이 있는가?
                    if map[i+1][j] == '1':
                        # 현재 집과 같은 그룹 번호를 줌
                        map[i+1][j] = map[i][j]
            # 좌우집 다 그룹 번호가 없는 경우
            else:
                group += 1
                print("새 그룹 번호:",group)
                # 새 그룹 번호를 넣어줌
                map[i][j] = group

                print("map[",i,"][",j,"] =", group)
                print("map[i][j] type:", type(map[i][j]))
                # 마즈막행이 아닌 경우
                if i != n-1:
                    # 현재 집의 아래 위치에도 집이 있는가?
                    if map[i+1][j] == '1':
                        # 현재 집과 같은 그룹 번호를 줌
                        map[i+1][j] = map[i][j]
print("i am map",map)
# 그룹 번호별 갯수를 리스트에 담기

print("map에서 1의 갯수:", map.count(1))

#3rd
# 그룹 수 리스트
cnt = [ 0 for i in range(group+1)]
# 그룹 당 지도에서의 집 개수
NumberPerGroup = 0

# map이 이차원 배열인 관계로 행단위로 1차원 배열을 count해줌
for j in range(1,group+1):
    # 같은 j안에서만 누적 다음 j로 바뀌면 초기화되어야함
    NumberPerGroup = 0
    # cnt[1]에는 맵에서 1이 있는 개수
    for i in range(n):
        print("map[",i,"].count(",j,")",map[i].count(j))
        #cnt[j] += map[i].count(j)
        #if map[i].count(j) == 0:
        #    break
        #위에 몰려있고 아래가 0인 경우는 제대로 계산 되지만 그룹 번호가 윗줄에선 0개이다가 아래 행에서 나오는 경우는 아래 행을 가지못하고 위에서 포문을 나가게 됨
        NumberPerGroup += map[i].count(j)

    cnt[j] = NumberPerGroup

print("그룹 리스트 :",cnt)

# 그룹당 수를 오름차순으로 정렬
cnt.sort()

print("오름 차순 정렬 후 그룹 리스트 :",cnt)

# 총 단지수 : 집의 수가 0개가 아닌 그룹의 수
print("단지 수:",len(cnt)-cnt.count(0))

# 집 갯수가 0 초과인 그룹 중 오름차순으로 출력
for i in cnt:
    print("단지별 집 수 오름차순 출력 for문")
    if i > 0:
        print(i)
''' 

 #4th

# 지도의 크기
n = int(input())

# 집 여부를 받는 지도 리스트
# 지도의 위치에 집이 없으면 '0' 집이 있으면 '1'이 들어가고 단지 번호를 받게 되면 정수형의 group 값을 받는다.
# 젤 처음 입력받을 떄는 문자열 형식의 요소 -> 그룹 번호를 받게 되면 정수형 형식의 요소로 바뀐다.
# 단지 번호를 받았는지의 여부는 지도의 값이 문자형인지 정수형인지로 구분
map = [[0 for _ in range(n)] for _ in range(n)]

# 단지/ 그룹 번호
group = 0


for i in range(n):
    # 지도 한 줄 받을 임시 변수
    line = input()
    # 띄어쓰기 없이 입력되는 집 여부값 문자열을 집 단위로 리스트에 담기
    for j in range(n):
        map[i][j] = line[j]

for i in range(n):
    for j in range(n):
        # 현재 집이 그룹 번호를 가지고 있는 경우
        if type(map[i][j]) == int :
            # 마즈막행이 아닌 경우
            if i != n-1:
                # 현재 집의 아래 위치에도 집이 있는가?
                if map[i+1][j] == '1':
                    # 현재 집과 같은 그룹 번호를 줌
                    map[i+1][j] = map[i][j]
        # 현재 집이 그룹 번호를 가지고 있지 않는 경우 중 현재 집 여부가 1인 경우
        elif map[i][j] == '1':
            # 첫번째 열인 경우 - 왼쪽 집이 없음 -> 오른쪽 집만 그룹 여부 체크
            if j == 0:
                # 오른쪽 집이 그룹 번호가 있는 경우
                if type(map[i][j+1]) == int :
                    map[i][j] = map[i][j+1]
                    
                # 오른쪽 집이 그룹 번호가 없는 경우
                else:
                    group += 1
                    # 새 그룹 번호를 넣어줌
                    map[i][j] = group

            # 젤 오른쪽 열인 경우 - 오른쪽 집이 없음 -> 왼쪽 집만 그룹 여부 체크
            elif j == n-1 :
                # 왼쪽 집이 그룹 번호가 있는 경우
                if type(map[i][j-1]) == int :
                    map[i][j] = map[i][j-1]
                    
                # 왼쪽 집이 그룹 번호가 없는 경우
                else:
                    group += 1
                    # 새 그룹 번호를 넣어줌
                    map[i][j] = group

            # 젤 왼쪽 열도 오른쪽 열도 아닌 경우
            # 현재 집의 좌우 집에 그룹 변호가 있는 경우
            elif type(map[i][j+1]) == int and type(map[i][j-1]) == int :
                # 현재 집을 기준으로 좌우집의 그룹 번호가 다른 경우
                if map[i][j-1] != map[i][j+1] :
                    # 그룹 번호 하나로 통일
                    # 왼쪽 집 그룹번호로 통일하겠음
                    map[i][j] = map[i][j-1]
                    # 지도 리스트에서 우측 집 그룹번호가 담겨있는 위치의 요소를 좌측집에 담겨있는 그룹번호로 바꿈
                    # map.replace(map[i][j+1],map[i][j-1])
                    # list엔 replace못 씀
                    for k in range(i+1):
                        for l in range(j+2):
                            if map[k][l] == map[i][j+1]:
                                map[k][l] = map[i][j-1]
                else:
                    map[i][j] = map[i][j-1]    
            # 나머지 경우
            # 왼쪽 집이 그룹 번호가 있는 경우
            elif type(map[i][j-1]) == int :
                map[i][j] = map[i][j-1]
                # 마즈막행이 아닌 경우
                
            # 오른쪽 집이 그룹 번호가 있는 경우
            elif type(map[i][j+1]) == int :
                map[i][j] = map[i][j+1]
                
            # 좌우집 다 그룹 번호가 없는 경우
            else:
                group += 1
                # 새 그룹 번호를 넣어줌
                map[i][j] = group

            # 마즈막행이 아닌 경우
            if i != n-1:
                # 현재 집의 아래 위치에도 집이 있는가?
                if map[i+1][j] == '1':
                    # 현재 집과 같은 그룹 번호를 줌
                    map[i+1][j] = map[i][j]

print("map",map)
# 그룹 수 리스트
cnt = [ 0 for i in range(group+1)]
# 그룹 당 지도에서의 집 개수
NumberPerGroup = 0

# map이 이차원 배열인 관계로 행단위로 1차원 배열을 count해줌
for j in range(1,group+1):
    # 같은 j안에서만 누적 다음 j로 바뀌면 초기화되어야함
    NumberPerGroup = 0
    # cnt[1]에는 맵에서 1이 있는 개수
    for i in range(n):
        NumberPerGroup += map[i].count(j)
        # cnt[j] += map[i].count(j) #IndexError: string index out of range 왜?

    cnt[j] = NumberPerGroup

# 그룹당 수를 오름차순으로 정렬
cnt.sort()

# 총 단지수 : 집의 수가 0개가 아닌 그룹의 수
print(len(cnt)-cnt.count(0))

# 집 갯수가 0 초과인 그룹 중 오름차순으로 출력
for i in cnt:
    if i > 0:
        print(i)


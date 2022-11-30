#1st

n, x = map(int,input("수열의 항 개수와 비교할 정수 입력").split())

# 수를 여러개 받으니까 리스트 사용 + 수끼리 비교해야하니까 정수 자료형으로 변환
"""arr = [map(int,input("수열 입력:").split())]
[]로 싸도 리스트 형식이 되는 게 아님
출력해보면 map 객체라고 뜸"""

arr = list(map(int,input("수열 입력:").split()))

# 배열 원소 수만큼 반복문 돌려서 각 원소와 비교할 정수 x 비교
for i in range(n):
    if arr[i] < x :
        print(arr[i],end=' ')
        # 조건(x보다 작은 수)에 해당하는 수들이 한줄로 나열되야 함
        # 그냥 print는 자동 개행(기본값으로 end = "\n") -> 출력 내용 마즈막에 붙일 문자를 end 매개변수를 이용해 띄워쓰기로 변경


        
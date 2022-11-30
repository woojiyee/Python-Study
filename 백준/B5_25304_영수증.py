#1st
"""totalReceipt = int(input("영수증의 총 금액을 입력하시오"))
totalTypeCount = int(input("구매한 물품의 종류의 수를 입력하시오"))
totalPrice


for i in totalTypeCount :
    price, count = map(int, input("각 구매한 상품별 가격과 갯수 입력").split())
    totalPrice += price*count
    
if totalReceipt == totalPrice:
    print("Yes")
else:
    print("No")

1st 코드의 잘못된 점
1. 파이썬은 JS와 달리 변수 선언문 앞에 붙이는 var,const같은 타입 추론이 가능한 변수 선언용 예약어가 없다.
    -> 초기값 명시 없는 변수 선언이 불가능
    -> totalPrice만 쓰면 에러 -> 초기화시켜줘야함
2. for문의 in 뒤에는 iterable(반복 가능한) 변수가 와야함
    -> totalTypeCount는 int이기에 iterable하지 않아 에러 뜸
    -> range()를 사용해서 정수를 iterable로 만들어 줌"""
    
#2nd
#금액과 종류 수는 다른 줄로 받음 -> input 2개
totalReceipt = int(input("영수증의 총 금액을 입력하시오"))
totalTypeCount = int(input("구매한 물품의 종류의 수를 입력하시오"))
#영수증의 총금액과 상세 물품의 금액 합을 비교하기 위해 낱개의 금액 합 변수 선언 및 초기화
totalPrice = 0

#물품의 종류만큼 물품 한개의 금액과 갯수를 입력받아야함
for i in range(totalTypeCount) :
    price, count = map(int, input("각 구매한 상품별 가격과 갯수 입력").split())
    # 물품 종류마다 가격과 금액은 저장할 필요없이 상세 물품의 금액 합을 구하면 되니까 totalPrice에 각 종류별 총 금액 더하기
    totalPrice += price*count
    
if totalReceipt == totalPrice:
    print("Yes")
else:
    print("No")

# 2nd 코드 처럼 백준 제출하면 출력 초과 뜸, 백준에서는 yes,no만 출력하길 원하는데
# 내 코드는 input에 값 입력받을 때 뜨는 문자열도 출력 됨 => 출력 초과
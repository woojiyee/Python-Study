'''king, queen, rook, bishop, knight, pawn = input("킹, 퀸, 룩, 비숍, 나이트, 폰 순서로 개수 입력").split()

king = int(king)
queen = int(queen)
bishop = int(bishop)
rook = int(rook)
knight = int(knight)
pawn = int(pawn)


print(1-king," ",1-queen," ",2-rook," ",2-bishop," ",2-knight," ",8-pawn)'''

#2nd
'''
king, queen, rook, bishop, knight, pawn = map(int,input("킹, 퀸, 룩, 비숍, 나이트, 폰 순서로 개수 입력").split())

print(1-king,1-queen,2-rook,2-bishop,2-knight,8-pawn)
'''

# 12.22 다시 풀어봄
#1st
'''
chess = list(map(int,input().split()))
print(chess)
original = [1,1,2,2,2,8]

for i in range(6):
    print(original[i]-chess[i],end = ' ')
'''
# 입력값이 한 줄에 있음 -> 한번의 input으로 입력받을 수 있음 -> input을 for 안 돌려도 됨
# 입력값이 한 줄에 띄워쓰기로 데이터를 구분해서 받음 -> split()이용 -> 띄워쓰기로 데이터를 구분하여 list()함수를 통해 list형식으로 입력됨
# + 사칙연산이 필요하니 숫자형으로 형변환 시켜야 함 -> int() 함수 이용
# 리스트 형식을 input() 매개변수로 받을 수 없음( int()가 그럼 ) => map 함수 이용해서 리스트에 int() 함수 적용시키기


# 23.4.29 복습

# 1st

k,q,l,b,kn,p = map(int,input().split())


print(1-k,end = ' ')
print(1-q,end = ' ')
print(2-l,end = ' ')
print(2-b,end = ' ')
print(2-kn,end = ' ')
print(8-p,end = ' ')
    
# 백준 맞았습니다.
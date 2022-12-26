# 로또는 순서가 달라도 구성요소?가 같으면 같은 데이터로 침 -> 순서 의미 x -> 조합
# 조합 : nCr (서로 다른 n개에서 r 개를 택하는 조합의 수 ) = nPr / r! = n * (n-1) * (n-2) * ... * (n-r+1) / r * (r-1) * (r-2) * ... * 1 ( 단, 0 <= r <= n)

# 목적 : 한 개의 리스트에서 r개의 조합 구하기
# 입력 : nCr에서 n과 r

# itertools 사용하는 방법

import itertools

# 테스트 케이스
t = 1

while t:
    l = list(map(int,input().split()))
    t = l[0]
    if t == 0:
        break
    s = l[1:]
    #print("t:",t)
    #print("s:",s)
    #print(list(itertools.combinations(s,6))) #[(1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 5, 7), (1, 2, 3, 4, 6, 7), (1, 2, 3, 5, 6, 7), (1, 2, 4, 5, 6, 7), (1, 3, 4, 5, 6, 7), (2, 3, 4, 5, 6, 7)]
    #print(map(list,itertools.combinations(s,6))) # <map object at 0x1051ea680>
    #print(list(map(list,itertools.combinations(s,6)))) # [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 7], [1, 2, 3, 4, 6, 7], [1, 2, 3, 5, 6, 7], [1, 2, 4, 5, 6, 7], [1, 3, 4, 5, 6, 7], [2, 3, 4, 5, 6, 7]]
    combination = list(map(list,itertools.combinations(s,6)))

    for i in combination:
        for j in range(6):
            print(i[j], end = " ")
        print("")
    print("")    

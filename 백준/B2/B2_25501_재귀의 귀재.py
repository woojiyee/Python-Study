# 1st
'''# 테스트 케이스 개수
T = int(input())

# 문자열
S = ''

# 반환값과 함수 호출 횟수 리스트
answer = [[0,0]]

# 테스트 케이스 수만큼 문자열 입력받아 리스트에 넣기
for i in range(T):
    S = input()
    
    def recursion(s,l,r):
        # recursion 함수 호출될 때마다 호출 횟수 증가
        answer[i,1]+=1
        if l>=r: return answer[i,0] = 1
        elif s[i] != s[r]: return answer[i,0] = 0
        else: return recursion(s, l+1, r-1)
 '''       
    

#2nd
# 테스트 케이스 개수
'''T = int(input("테스트 케이스 수 입력:"))

# 문자열
S = ''


# 테스트 케이스 수만큼 문자열 입력받아 리스트에 넣기
for i in range(T):
    s = input(" 문자열 입력:")
    
    # recursion 함수 호출 횟수
    n = 0

    def recursion(s,l,r):
        # recursion 함수 호출될 때마다 호출 횟수 증가
        n += 1

        if l>=r: return 1 
        elif s[i] != s[r]: return 0 
        else: return recursion(s, l+1, r-1)

    def isPalindrome(s):
        return recursion(s, 0, len(s)-1)

    print(isPalindrome(s),' ',n)'''

#3rd
# 테스트 케이스 개수
T = int(input("테스트 케이스 수 입력:"))

# 문자열 리스트
S = []


def recursion(s,l,r):
    global n
    n +=1
    # recursion 함수 호출될 때마다 호출 횟수 증가
    if l>=r: return 1
    elif s[l] != s[r]: return 0 
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)


# 테스트 케이스 수만큼 문자열 입력받아 리스트에 넣기
for i in range(T):
    S.append(input(" 문자열 입력:"))
    
for str in S:
    # recursion 함수 호출 횟수
    n = 0
    print(isPalindrome(str),n)
    
# 전역 변수관련
'''n의 특징
1. recursion 호출 횟수를 세야함 -> recursion 안에서 증가 코드가 있어야함
2. 문자열이 바뀔 때마다 n(recursion 호출 횟수)가 초기화 돼야함 -> 'for str in S'에서 n 초기화
3. -> n은 'for str in S'에서 초기화 되고 함수 'recursion'에서 또 쓰임 = 쓰이는 곳과 초기화한 곳이 다름 = namespace?가 다름 => n을 쓰는 함수 'recursion'에서 n을 전역변수 선언!( global n )
   -> 전역 변수로 썼기에 'recursion'의 return으로 넘기지 않아도 'for str in S'에서 그냥 바로 'recursion'에서 바뀐 n 값을 받을 수 있음
'recursion'의 반환값(return) 0,1 특징
1. 'recursion' 함수를 호출하면 나오는 값 -> 반환값으로 주면 됨
2. 얘도 전역변수로 써도 되긴함 -> 근데 n처럼 계속 바뀌는 값이 아니고 'recursion'가 아닌 다른 곳에서 초기화하거나 값을 변경하지 않고 'recursion' 함수를 돌리면 나오는 값이기에 반환값으로만 줘도 충분'''
    



    
    
 
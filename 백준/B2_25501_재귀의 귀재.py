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
    

    



    
    
 
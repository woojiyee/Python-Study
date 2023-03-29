'''a = list()
print("a",a) # []

a.append(3) # [3]
print(a)

# b = list(2,3) 
# print("b",b) # TypeError: list expected at most 1 argument, got 2

c = list((2,3,4))
print("C",c) # [2, 3, 4]

d = (5,6)
print("d",d) # (5, 6)

e = list(d)
print("e",e) # [5, 6]'''

'''q = [[1,2,3],[4,5,6]]

for i in q:
    print("i[1]",i[1])'''

'''
list1 = []

def what1():
    list1 = [0] * 3

what1()

print("list1",list1) # []


list2 = [0] * 3

def what2():
    list2[1] = 2
what2()

print("list2",list2) # [0, 2, 0]

list3 = [0] * 3

def what3():
    list3 = []
what3()

print("list3",list3) # [0,0,0]

list4 = [0] * 3
list4 = []
print("list4",list4) # []

list5 = []

def what5():
    list5.append(2)

what5()

print("list5",list5) # [2]
'''

'''list6 = []

def what6():
    list6.append(3)
    list6 = []

what6()

print("list6",list6) # UnboundLocalError: local variable 'list6' referenced before assignment
'''

'''
list5 = []


list7 = [1,2]
def what7():
    list7 = []
    list7.append(2)
    

what7()

print("list7",list7) # [1,2]

var = 0

def fun():
    a = var +2
    print("a",a) # 2
    return a+2

print("fun return",fun()) # 4
print("var",var) # 0

var10 = 10

def fun10():
    var10 = 7 + 2
    # var10 = var10 + 2  # UnboundLocalError: local variable 'var10' referenced before assignment
    print("var10",var10) # 9
    return var10+2

print("fun10 return",fun10()) # 11

print("var10",var10) # 10

var20 = 20

def fun20():
    global var20
    var20 = var20 + 2  
    print("var20",var20) # 22
    return var20+ 1

print("fun20 return",fun20()) # 23

print("var20",var20) # 22
'''
# c = c +1 # NameError: name 'c' is not defined

'''def check():
    cc = cc +1 # UnboundLocalError: local variable 'cc' referenced before assignment (따로 print안 해도 해당 코드서 에러 뜸 )

check()'''
'''
ll = [1,2,3]
print("ll",ll,id(ll))
ll[1] = 0
print("ll 인덱싱을 통한 값 변경",ll,id(ll))
ll = [10,20,30]
print("ll 통으로 값 변경",ll,id(ll))

a = 10
print("a",a,id(a))
a = a + 1
print("a를 이용한 값 변경",a,id(a))
a = 20
print("a 재할당",a,id(a))

def change():
    val = 20
    print("값 변경 전 list2",list2)
    # print("재선언 전 list1",list1) # UnboundLocalError: local variable 'list1' referenced before assignment
    list1 = [1,2,3]
    list1[1] = 0
    list2[1] = 100
    global list3
    list3 = [0,0,0]
    list3[1] = 1000
    print("함수 안 val",val)
    print("함수 안 list1",list1)
    print("함수 안 list2",list2)
    print("함수 안 list3",list3)

val = 10
list1 = [10,20,30]
list2 = [11,22,33]
list3 = [100,200,300]
change()
print("함수 밖 val",val)
print("함수 밖 list1",list1)
print("함수 밖 list2",list2)
print("함수 밖 list3",list3)
'''
'''
amount = [int(input()) for _ in range(3)] 
print(amount) # [1, 2, 3]
'''

a = [1,2,3]
print(a)

# 1
'''
a[0:0] = 0
print(a) # TypeError: can only assign an iterable
'''
#2
'''
a[0:0] = [0] 
print(a) # [0, 1, 2, 3]
'''

#3
'''
a[0:1] = [0] 
print(a) # [0, 2, 3]
'''

a.insert(0,0)
print(a) # [0, 1, 2, 3]
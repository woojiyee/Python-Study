a = list()
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
print("e",e) # [5, 6]

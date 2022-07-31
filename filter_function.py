#Funzioni Filter

def add7(x):
    return x+7

def minus7(x):
    return x-7

def isOdd(x):
    return x%2 == 0

def addLetter(x):
    
    return(f'lettera {x}')


a = [1,2,3,4,5,6,7,8,9,10]

liste = ['a','b','c']

e = list(map(addLetter, filter( addLetter, liste)))

b = list(filter(isOdd, a))

c = list(map(add7, filter(isOdd, a)))

d = list(map(minus7, filter(isOdd, a)))
# 
# print(a)
# 
# print(b)
# 
# print(c)
# 
# print(d)

print (e)
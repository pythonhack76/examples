#map function 

lista = [1,2,3,4,5,6,7,8,9,10]

def func(x):
    return x**x

newList = []
for x in lista:
    newList.append(func(x))

print(newList)
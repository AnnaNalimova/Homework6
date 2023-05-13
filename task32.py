# 32 Определить индексы элементов массива (списка),
# значения которого 
# принадлежат заданному диапазону
# (т.е.не меньше заданного минимума и не больше заданного максимума)
def  filllist(n):
    list1 = []
    for i in range(n):
        numm = int(input())
        list1.append(numm)
    return(list1)


def index1(minnn: int,maxxx: int,list_r: list):
    indexx = []
    for i in range(len(list_r)):
        if list_r[i] > minnn and list_r[i] < maxxx :
            indexx.append(i)
    return(indexx)


N = int(input('Введите длину списка:'))
minn = int(input('Введите число минимума:'))
maxx = int(input('Введите  число максимума:'))
print(index1(minn,maxx,(filllist(N))))
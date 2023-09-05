first = int(input("Введите первый жлемент прогрессии: "))
step = int(input("Введите разность прогрессии: "))
num = int(input("Введите количество элементов прогрессии: "))
l = []
for i in range(first, first + step * num -1, step):
    l.append(i)

print(l)    

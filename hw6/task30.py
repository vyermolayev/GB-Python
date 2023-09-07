first = int(input("Введите первый жлемент прогрессии: "))
step = int(input("Введите разность прогрессии: "))
num = int(input("Введите количество элементов прогрессии: "))
l = []
for i in range(num):
    l.append(first + step * i)

print(l)    
print([first + step * i for i in range(num)])
print(list(range(first, first + step * num, step)))

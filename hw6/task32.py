inList = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

rangeMin = int(input("Введите минимальное значение: "))
rangeMax = int(input("Введите максимальное значение: "))

resList = []

if rangeMax < rangeMin:
    rangeMin, rangeMax = rangeMax, rangeMin
    
for idx in range(len(inList)):
    if inList[idx] >= rangeMin and inList[idx] <= rangeMax:
        resList.append(idx)

print(resList)        
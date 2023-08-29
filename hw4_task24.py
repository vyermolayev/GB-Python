n = int(input("Введите количество кустов: "))
berries = []
i = 0
while i in range(n):
    berries.append(int(input("Введите количество ягод на кусте №{num}: ".format(num = i + 1))))
    i += 1
maxBerries = 0
maxBerriesPos = 0
curRes = 0
i = 0
while i in range(n):
    if i == 0:
        prevIdx = len(berries) - 1
    else:
        prevIdx = i - 1    
    if i == len(berries)  - 1:
        nextIdx = 0
    else:
        nextIdx = i + 1
 
    curRes = berries[prevIdx] + berries[i] + berries[nextIdx]

    if curRes > maxBerries:
        maxBerries = curRes
        maxBerriesPos = i + 1
    i += 1 

print(maxBerries)


        
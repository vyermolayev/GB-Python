n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))
input1 = []
input2 = []
i = 0
while i in range(n):
    input1.append(int(input("Введите элемент №{num} первого множества: ".format(num = i + 1))))
    i += 1

i = 0
while i in range(m):
    input2.append(int(input("Введите элемент №{num} второго множества: ".format(num = i + 1))))
    i += 1

input1 = set(input1)
input2 = set(input2)

result = list(input1.intersection(input2))
result.sort()
print(result)
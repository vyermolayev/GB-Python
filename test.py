def revList(n):
    if n == 0:
        return
    uData = input("Введите элемент {num}: ".format(num=num - n + 1))

    revList(n -1)
    print (uData, end =" ")


num = int(input("Введите кол-во элементов:"))
revList(num)    
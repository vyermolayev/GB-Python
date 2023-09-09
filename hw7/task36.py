def print_operation_table(operation, num_rows, num_columns):

    return [[str(operation(i + 1, j + 1)) for j in range(num_columns)] for i in range(num_rows)]

def calcMaxLength(inList):
    curMax = 0
    maxLength = 0
    for row in inList:
         curMax = max(list(map(len, row)))
         if curMax > maxLength:
             maxLength = curMax
    return maxLength

def formatter(el):
    return f"{el:>{maxLength + 1}}"

res = print_operation_table(lambda x, y: x * y,10, 10)
maxLength = calcMaxLength(res)

for el in res:
    print("".join(map(formatter,el)))
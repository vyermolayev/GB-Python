def cntVowLet(inStr):
    cnt=0
    for let in inStr:
        if let in vowLet:
            cnt += 1
    return cnt

vowLet = "а,е,ё,и,о,у,ы,э,ю,я".split(",")

inStr=input("Введите стихотворение Винни-Пуха: ")
res = set(map(cntVowLet, inStr.split()))

if len(res) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")

phoneDb =[]
def loadPhoneDirectory():
    
    with open("phoneBook.db", "r", encoding="utf-8") as reader:  
        fData = reader.readlines()
        for ln in fData:
            if ln != "\n":
                rec = {}
                rec['name'],rec['surname'],rec['phone'],rec['addr'] = (ln.replace("\n","")).split("|")
                phoneDb.append(rec)

def storePhoneBook():
    with open("phoneBook.db", "w+", encoding="utf-8") as writer:
        for rec in phoneDb:
            writer.write(f"{rec['name']}|{rec['surname']}|{rec['phone']}|{rec['addr']}\n\n")

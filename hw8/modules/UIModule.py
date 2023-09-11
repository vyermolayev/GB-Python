from modules import fileModule as FM

def inputName():
    return input("Введите имя: ")

def inputSurName():
    return input("Введите фамилию: ")


def inputPhoneNumber():
    return input("Введите номер телефона: ")

def inputAddr():
    return input("Введите адресс: ")

def createNewRecord():
    ret = {
    "name": inputName(),
    "surname": inputSurName(),
    "phone":inputPhoneNumber(),
    "addr": inputAddr()
    }

    FM.phoneDb.append(ret)

    return ret

def searchRecords():
    searchParam = input("Введите текст для поиска: ")

    for idx, rec in enumerate(FM.phoneDb):
        for fld in rec.values():
            if fld.find(searchParam) != -1:
                displayRecord(rec, idx)
                break


def displayRecord(rec, idx):
    print(f"{idx} - {rec['name']} {rec['surname']}: {rec['phone']} {rec['addr']}")


def editRecord():
    inVal = input("Введите ИД записи для редактирования")

    if not inVal.isnumeric() or int(inVal) > len(FM.phoneDb):
        print("Неверный ИД")
        return
    inVal = int(inVal)
    displayRecord(FM.phoneDb[inVal - 1], inVal)
    
    newRec = {
    "name": inputName(),
    "surname": inputSurName(),
    "phone":inputPhoneNumber(),
    "addr": inputAddr()
    }

    FM.phoneDb[inVal - 1] = newRec

    print("Изменения сохранены")

def deleteRecord():
    inVal = input("Введите ИД записи для удаления")

    if not inVal.isnumeric() or int(inVal) > len(FM.phoneDb):
        print("Неверный ИД")
        return
    inVal = int(inVal)
    displayRecord(FM.phoneDb[inVal - 1], inVal)
    FM.phoneDb.remove(FM.phoneDb[inVal - 1])
    print("Запись удалена")

def showMenu():

    while True:
        print("\n\n\n")
        print("************************************************")
        print("***        Телефонный справочник             ***")
        print("***                Меню:                     ***")
        print("***     1 - добавить новую запись            ***")
        print("***     2 - поиск записи                     ***")
        print("***     3 - Изменить запись                  ***")
        print("***     4 - Удалить запись                   ***")
        print("***     любое другое значение - выход        ***")
        print("************************************************")
        menuOpt = input("Выберите действие: ")

        if menuOpt.isnumeric():
            menuOpt = int(menuOpt)
        else:
            menuOpt = 0    
        if menuOpt == 1:
            createNewRecord()
        elif menuOpt == 2:
            searchRecords()
        elif menuOpt == 3:
            editRecord()    
        elif menuOpt == 4:
            deleteRecord()
        else:
            break


class Human:
    def __init__(self, type):
        self.type = type

class Man(Human):
    def __init__(self):
        super().__init__("m")

class Women(Human):
    def __init__(self):
        super().__init__("m")

def funct_1(str):
    n = 2
    newList = [str[i:i + n] for i in range(0, len(str), n)]
    lastInList = newList[len(newList) - 1]
    if(len(lastInList) % 2 != 0):
        newList[len(newList) - 1] = newList[len(newList) - 1] + "_"
    return newList

def funct_2(str):
    list = str.split(r'(\s+)')
    newList = ""
    for i in range(len(list)):
        reversedString = list[i][::-1]
        newList = newList + " " + reversedString
    return newList

def funct_3():
    newArray = []
    newArray.append(Man())
    newArray.append(Women())
    return newArray


print(funct_1("abcdefg"))
print(funct_2("This is an example!"))
print(funct_3())


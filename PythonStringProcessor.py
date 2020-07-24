class PythonStringProcessor:
    def __init__(self):
        self.myList = []

    def AddToList(self, newitem):
        if(type(newitem) == str and self.__is_ascii(newitem)):
            self.myList.append(newitem)
        elif(type(newitem) == list and self.CheckIfListContainsStrings(newitem)):
            for item in newitem:
                self.myList.append(item)
        
    def CheckIfListContainsStrings(self, listToCheck):
        for item in listToCheck:
            if(type(item) != str or not self.__is_ascii(item)):
                print("Not all items in the provided list are ascii strings.")
                return False
        return True
    
    def outputList(self):
        f = open('./output.txt', 'w')
        f.write("\n".join(self.myList))

    def __is_ascii(self, s):
        return all(ord(c) < 128 for c in s)
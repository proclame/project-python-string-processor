class PythonStringProcessor:
    def __init__(self):
        self.myList = []

    def AddToList(self, newitem):
        if(type(newitem) == str):
            self.myList.append(newitem)
        elif(type(newitem) == list and self.CheckIfListContainsStrings(newitem)):
            for item in newitem:
                self.myList.append(item)
        
    def CheckIfListContainsStrings(self, listToCheck):
        for item in listToCheck:
            if(type(item) != str):
                print("Not all items in the provided list are strings.")
                return False
        return True
    
    def outputList(self):
        f = open('./output.txt', 'w')
        f.write("\n".join(self.myList))
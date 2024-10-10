class Person:

    def __init__(self, name, age, id):
        self._name = name
        self._age = age
        self._id = id

    def getName(self):
        return self._name

    def getAge(self):
        return self._age

    def getId(self):
        return self._id

    def setName(self, name):
        self._name = name

    def setId(self, id):
        self._id = id

    def setAge(self, age):
        self._age = age

    def strforPerson(self):
        return "Im " + self.getName() + " And Im " + str(self.getAge()) + " My Id Is : " + str(self.getId())

    def printMySelf(self):
        print(self.strforPerson())

    def informationToDic(self, information_details):
        return {information_details["name"]: self.getName(),
                information_details["id"]: self.getId(),
                information_details["age"]: self.getAge()}

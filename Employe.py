from Person import Person


class Employe(Person):
    def __init__(self, name, age, id, field_of_work="", salary=0):
        super().__init__(name, age, id)
        self._field_of_work = field_of_work
        self._salary = salary

    def getFieldOdWork(self):
        return self._field_of_work

    def getSalary(self):
        return self._salary

    def setSalary(self, salary):
        self._salary = salary

    def setFieldOfWork(self, field_of_work):
        self._field_of_work = field_of_work

    def strforEmploye(self):
        return self.StrtoPerson() + " Working at: " + self.getFieldOdWork() + "My Salary: " + str(self.getSalary())

    def printMySelf(self):
        print(self.strforEmploye())

    def informationToDic(self, information_details):
        return {information_details["name"]: self.getName(),
                information_details["id"]: self.getId(),
                information_details["age"]: self.getAge(),
                information_details["field of work"]: self._field_of_work,
                information_details["salary"]: self._salary}

    def inputFromUser(self):
        self._field_of_work = input("what is your work: ")
        self._salary = input("what is your salary : ")

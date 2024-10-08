from Person import Person


class Employe(Person):
    def __init__(self, name, age, ids, field_of_work, salary):
        super().__init__(name, age, ids)
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

    def printEmploye(self):
        return self.StrtoPerson() + " Working at: " + self.getFieldOdWork() + "My Salary: " + str(self.getSalary())

    def printMySelf(self):
        print(self.printEmploye())



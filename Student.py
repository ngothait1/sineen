from Person import Person


class Student(Person):
    def __init__(self, name, age, id, year_of_study=0, score_avg=0):
        super().__init__(name, age, id)
        self._year_of_study = year_of_study
        self._score_avg = score_avg

    def getYearOfStudy(self):
        return self._year_of_study

    def getScoreAvg(self):
        return self._score_avg

    def setYearOfStudy(self, year_of_study):
        self._year_of_study = year_of_study

    def setscoreAvg(self, score_avg):
        self._score_avg = score_avg

    def strforStudent(self):
        return self.StrtoPerson() + " Year: " + str(self.getYearOfStudy()) + " with Avg: " + str(self.getScoreAvg())

    def printMySelf(self):
        print(self.strforStudent())

    def informationToDic(self, information_details):
        return {information_details["name"]: self.getName(),
                information_details["id"]: self.getId(),
                information_details["age"]: self.getAge(),
                information_details["year"]: self._year_of_study,
                information_details["score average"]: self._score_avg}

    def inputFromUser(self):
        self._year_of_study = input("what year you are: ")
        self._score_avg = input("what is your average : ")
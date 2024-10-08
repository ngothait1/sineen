from Person import Person


class Student(Person):
    def __init__(self, name, age, ids, year_of_study, score_avg):
        super().__init__(name, age, ids)
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

    def printStudent(self):
        return self.StrtoPerson() + " Year: " + str(self.getYearOfStudy()) + " with Avg: " + str(self.getScoreAvg())

    def printMySelf(self):
        print(self.printStudent())

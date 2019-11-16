class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []

    def add_grade(self, grade):
        if type(grade) == Grade:
            self.grades.append(grade)

    def get_average(self):
        sum_grade = 0
        for grade in self.grades:
            sum_grade += grade.score
        return sum_grade / len(self.grades)


class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score

    def is_passing(self):
        if self.score > self.minimum_passing:
            return 'Pass'
        else:
            return 'Fail'


roger = Student('Roger van der Weyden', 10)
sandro = Student('Sandro Botticelli', 12)
pieter = Student('Pieter Bruegel the Elder', 8)
grade1 = Grade(100)
grade2 = Grade(87)
pieter.add_grade(grade1)
pieter.add_grade(grade2)
avg = pieter.get_average()
print(avg)
print(grade2.is_passing())

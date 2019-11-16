class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

    def add_fractions(self, other):
        num_no = str((other.get_den() * self.num)+ (other.get_num() * self.den))
        den_no = str(other.get_den() * self.den)
        return Fraction(num_no, den_no)


f1 = Fraction(3,4)
f2 = Fraction(7,10)
print(f1)
print(f1.get_num())
print(f1.get_den())
print('Sum of two fractions are:', f1.add_fractions(f2))

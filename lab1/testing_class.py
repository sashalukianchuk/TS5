class Testing:
    @classmethod
    def NumInRange(cls, x):
        try:
            float(x)
        except ValueError:
            raise ValueError
        if x > 120.829:
            raise ValueError
        elif x < 0.606:
            raise ValueError
        else:
            return True

    @staticmethod
    def output(result):
        return result

    def pattern1(self, x):
        self.NumInRange(x)
        y = (x ** 4) * 3.75 + (x ** 3) * 2.272 - (x ** 2) * 5.351 + x * 4.653
        return self.output(y)

    def pattern2(self, x):
        self.NumInRange(x)
        y = (x ** 3) * 3.37 - (x ** 2) * 3.336 + x * 5.42
        return self.output(y)

    def pattern3(self, x):
        self.NumInRange(x)
        y = (x ** 2) * 1.441 + x * 2.465
        return self.output(y)

    def pattern4(self, x):
        self.NumInRange(x)
        y = x * 6.364
        return self.output(y)




if __name__ == '__main__':
    test = Testing()
    print(test.pattern1(1))
    print(test.pattern2(1))
    print(test.pattern3(1))
    print(test.pattern4("ajsfwfial"))
    print(test.pattern1(120.829 - 0.606))
    print(test.pattern1(0.1))
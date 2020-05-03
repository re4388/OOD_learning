class Salary_Rate:
    def __init__(self, currency='TWD', base_rate=0):
        self.currency = currency
        self.base_rate = base_rate
        self.class_name = self.__class__.__name__

    def __str__(self):
        return self.class_name

    def get_base_rate(self):
        return self.base_rate

class Monthy_Rate(Salary_Rate):
    def __init__(self, currency='TWD', base_rate=29000):
        super().__init__(currency, base_rate)


class Daily_Rate(Salary_Rate):
    def __init__(self, currency='TWD', base_rate=120):
        super().__init__(currency, base_rate)



class Comminsion_Rate(Salary_Rate):
    def __init__(self, currency='TWD', base_rate=100):
        super().__init__(currency, base_rate)

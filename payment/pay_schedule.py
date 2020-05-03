

class PaymentSchedule:
    def __init__(self, id):
        self.id = id


class Monthy_Pay(PaymentSchedule):
    def __init__(self, id):
        super().__init__(id)

    def __str__(self):
        return 'Monthy_Pay'

class Weekly_Pay(PaymentSchedule):
    def __init__(self, id, ):
        super().__init__(id, )

    def __str__(self):
        return 'Weekly_Pay'

class Biweekly_Pay(PaymentSchedule):
    def __init__(self, id, ):
        super().__init__(id, )

    def __str__(self):
        return 'Biweekly_Pay'
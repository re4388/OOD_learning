
from payment import payment_method, pay_schedule, salary_rate
from error import custom_error
from datetime import datetime as dt
datetime_dt = dt.today() 
today_formated = datetime_dt.strftime("%Y/%m/%d")

class Employer:
    def __init__(self,id: int, name :str):

        self.id = id
        self.name = name
        self.type = None

        self.payment_method = None
        self.payment_schedule = None
        self.salary_rate = None


    def get_type(self) -> str:
        return self.type


    def add_payment_schedule(self, payment_schedule_option:str):
        if payment_schedule_option is not None:
            if payment_schedule_option == 'Monthy_Pay':
                self.payment_method = pay_schedule.Monthy_Pay(1)
            elif payment_schedule_option == 'Weekly_Pay':
                self.payment_method = pay_schedule.Weekly_Pay(1)
            elif payment_schedule_option == 'Biweekly_Pay':
                self.payment_method = pay_schedule.Biweekly_Pay(1)
            else:
                return 'payment_schedule_option is not exist'
        else:
            raise custom_error.InputError('payment_schedule already exist, you could use update_payment_schedule')

    def update_payment_schedule(self, payment_schedule_option: str):
        pass

    def delete_payment_schedule(self, payment_schedule_option: str):
        pass

    def get_payment_schedule(self):
        if self.payment_schedule is None:
            return 'No payment_schedule in record'
        else:
            return self.payment_schedule



    def add_payment_method(self, payment_method_option:str):
        if payment_method_option is not None:
            if payment_method_option == 'Payment_to_Post':
                self.payment_method = payment_method.Payment_to_Post(1)
            elif payment_method_option == 'Payment_in_Company':
                self.payment_method = payment_method.Payment_in_Company(1)
            elif payment_method_option == 'Payment_to_PerosnalAccount':
                self.payment_method = payment_method.Payment_to_PerosnalAccount(1)
            else:
                return 'payment_method_option is not exist'
        else:
            raise custom_error.InputError('payment_method already exist, you could use update_payment_method')

    def get_payment_method(self, ):
        if self.payment_method is None:
            return 'No payment method in record'
        else:
            return self.payment_method

    def update_payment_method(self, ):
        pass

    def delete_payment_method(self, ):
        pass


class Rd(Employer):
    def __init__(self, id, name,type='RD'):
        super().__init__(id, name)
        self.type = type


class Pt(Employer):
    def __init__(self, id, name, type='Part_time', timecard=None):
        super().__init__(id, name)
        self.type = type
        self.receipt = None
        self.timecard = None

        # self.timecard = [{'20200309':8},
        #                  {'20200310':14}]

class Sales(Employer):
    def __init__(self, id, name, type='Sales', receipt=None):
        super().__init__(id, name)
        self.type = type
        # TODO could put in db to make it persistent
        self.receipt = []
        self.payment_schedule = pay_schedule.Biweekly_Pay(1)
        self.salary_rate = salary_rate.Comminsion_Rate()

    def salary_dispatch_record(self, date):
        receipt = self.get_receipt()

        total_qty = 0
        for i in receipt:
            if i['date'][:7] == date:
                total_qty += i['qty']

        base_rate= self.salary_rate.get_base_rate()
        wage = total_qty * base_rate

        record = {
            date:wage
        }
        return record

    def get_salary_rate(self):
        if self.salary_rate is not None:
            return self.salary_rate
        else:
            raise custom_error.InputError('no payment_schedule, system error')

    def get_payment_schedule(self):
        if self.payment_schedule is not None:
            return self.payment_schedule
        else:
            raise custom_error.InputError('no payment_schedule, system error')


    # --------------
    # receipt operation

    def get_receipt(self):
        if len(self.receipt) == 0:
            return 'The receipt is empty'
        else:
            return self.receipt

    def add_record_to_receipt(self, sell_qty=0):
        if len(self.receipt) == 0:
            new_item = {'date': today_formated,
                        'qty': sell_qty}
            self.receipt.append(new_item)
        else:
            all_date = [x['date'] for x in self.receipt]
            if today_formated in all_date:
                for item in self.receipt:
                    if item['date'] == today_formated:
                        item['qty'] += sell_qty

            else:
                new_item= {'date':today_formated,
                           'qty':sell_qty}
                self.receipt.append(new_item)

    def delete_last_record_in_receipt(self):
        self.receipt.pop()

    def update_record_in_receipt(self, date, qty):
        if len(self.receipt) == 0:
            raise custom_error.InputError('no item to update')
        else:
            all_date = [x['date'] for x in self.receipt]
            if date in all_date:
                for item in self.receipt:
                    if item['date'] == date:
                        item['qty'] = qty
            else:
                raise custom_error.InputError('can not find matching date to update')



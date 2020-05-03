import logging
from error import custom_error


class PaymentMethod:
    def __init__(self, id: int):
        self.id = id


class Payment_to_Post(PaymentMethod):
    def __init__(self, id, post_address='defualt_input: please update the post address'):
        super().__init__(id, )
        self.post_address = post_address


    def get_post_address(self):
        if self.post_address is not None:
            return self.post_address
        else:
            return 'address is not exis, please add first'

    def add_post_address(self, address:str):
        if self.post_address is not None:
            raise custom_error.InputError('address already exist, you could use update_post_address')
        else:
            self.post_address = address

    def update_post_address(self, address:str):
        if self.post_address is not None:
            self.post_address = address
        else:
            raise custom_error.InputError('address is not exist for update, please add address first')

    def delete_post_address(self, address: str):
        if self.post_address is not None:
            self.post_address = None
            logging.info('post_address is deleted')
        else:
            raise custom_error.InputError('address is not exist for delete, please add address first')



    def __str__(self):
        return 'Payment_to_Post'


class Payment_in_Company(PaymentMethod):
    def __init__(self, id, hold_day=5):
        super().__init__(id)
        self.hold_days = hold_day

    # TODO CRUD for hold_day, just like post_address
    # def get_hold_day(self):
    #     if self.post_address is not None:
    #         return self.post_address
    #     else:
    #         return 'address is not exis, please add first'
    #
    # def add_hold_day(self, address:str):
    #     if self.post_address is not None:
    #         return 'already exist, you could use update_post_address if this is what you want'
    #     else:
    #         self.post_address = address
    #
    # def update_hold_day(self, hold_day:int):
    #     if self.hold_day is not None:
    #         self.hold_day = hold_day
    #     else:
    #         return 'hold_day is not exist for update, please add first'
    #
    # def delete_hold_day(self, address: str):
    #     self.post_address = None
    #     return 'post_address is deleted'

    def __str__(self):
        return 'Payment_in_Company'



class Payment_to_PerosnalAccount(PaymentMethod):
    def __init__(self, id, bank_account):
        super().__init__(id)
        self.bank_account = bank_account

    def __str__(self):
        return 'Payment_to_PerosnalAccount'

    # TODO CRUD for bank_account, just like post_address
    # def get_bank_account(self):
    #     return self.bank_account
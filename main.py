

from employer import Rd, Pt, Sales


if __name__ == '__main__':

    # ---------------
    # init employer

    ben = Sales(1, 'Ben', )
    print(ben.get_type())

    # sabrina = Rd(2, 'Sabrina', )
    # print(sabrina.get_type())

    # --------------
    # payment schedule
    print(ben.get_payment_schedule())


    #--------------
    # salary_rate
    print(ben.get_salary_rate())




    # # --------------
    # # payment method
    ben.add_payment_method('Payment_to_Post')
    ben_payment_method = ben.get_payment_method()
    print(ben_payment_method)

    print(ben_payment_method.get_post_address())

    # ben_payment_method.add_post_address('Lemon Street, No.13')
    # print(ben_payment_method.get_post_address())
    #
    ben_payment_method.update_post_address('Lemon Street, No.66')
    print(ben_payment_method.get_post_address())


    ben_payment_method.delete_post_address('Lemon Street, No.66')
    print(ben_payment_method.get_post_address())
    #
    ben_payment_method.add_post_address('Lemon Street, No.66')
    print(ben_payment_method.get_post_address())


    print('===================')

    ben_receipt = ben.get_receipt()
    print(ben_receipt)

    ben.add_record_to_receipt(23)
    # print(ben.get_receipt())

    ben.add_record_to_receipt(23)
    # print(ben.get_receipt())

    # ben.add_record_to_receipt(10)
    # print(ben.get_receipt())
    #
    ben.delete_last_record_in_receipt()
    # print(ben.get_receipt())
    #
    ben.add_record_to_receipt(23)
    print(ben.get_receipt())
    #
    # ben.update_record_in_receipt('2020/05/03', 20)
    # print(ben.get_receipt())

    print('===================')

    # ------------------
    # get salary_dispatch_record
    print(ben.salary_dispatch_record(date='2020/05'))


    # `{[{'2020_Jan_1': 15000}, {'2020_Jan_2': 18000}]`
    # for sales
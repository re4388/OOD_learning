class InputError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'Input Error, {0} '.format(self.message)
        else:
            return 'Input Error has been raised'


# raise MyCustomError


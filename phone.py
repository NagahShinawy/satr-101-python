class Phone:

    MAX_LEN = 11

    def __init__(self, code, number):
        self.code = code
        self.number = number

    @property
    def get_number(self):
        return f"({self.code}) {self.number}"

    def __str__(self):
        return self.get_number

    def is_valid(self):
        return len(self.get_number) == self.MAX_LEN

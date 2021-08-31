from prettytable import PrettyTable
from phone import Phone


# contacts = [
#     {"name": "john", "phone": {"code": "+20", "number": "01289584983"}},
#     {"name": "james", "phone": {"code": "+20", "number": "01289584567"}},
#     {"name": "loen", "phone": {"code": "+20", "number": "01089599567"}},
# ]


class Contact:
    FILED_NAMES = ["name", "phone"]

    def __init__(self, name: str, phone: Phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return self.name

    def to_pretty(self):
        contacts_tbl = PrettyTable()
        contacts_tbl.field_names = self.FILED_NAMES
        contacts_tbl.add_row([self.name, self.phone])
        return contacts_tbl

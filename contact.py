from phone import Phone
from mixins import PrettyTableMixin

# contacts = [
#     {"name": "john", "phone": {"code": "+20", "number": "01289584983"}},
#     {"name": "james", "phone": {"code": "+20", "number": "01289584567"}},
#     {"name": "loen", "phone": {"code": "+20", "number": "01089599567"}},
# ]


class Contact(PrettyTableMixin):
    FILED_NAMES = ["Name", "Phone"]

    def __init__(self, name: str, phone: Phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.phone = phone

    def __str__(self):
        return self.name

    def to_pretty(self):
        self.field_names = self.FILED_NAMES
        self.add_row([self.name, self.phone])
        return self.get_string()

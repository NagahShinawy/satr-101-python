from phone import Phone
from mixin.pretty import PrettyTableMixin


class Contact(PrettyTableMixin):
    FIELDS_NAMES = ["Name", "Phone"]

    def __init__(self, name: str, phone: Phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.phone = phone
        self.rows = [(self.name, self.phone)]

    def __str__(self):
        return self.name

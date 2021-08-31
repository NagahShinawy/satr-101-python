from prettytable import PrettyTable


class PrettyTableMixin(PrettyTable):
    FIELDS_NAMES = ["Name", "Phone"]
    rows = []

    @staticmethod
    def to_row(contact):
        return contact.name, contact.phone

    def to_pretty(self):
        self.field_names = self.FIELDS_NAMES
        self.add_rows([self.to_row(contact) for contact in self.rows])
        return self.get_string()

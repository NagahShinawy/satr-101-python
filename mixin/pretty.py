from prettytable import PrettyTable


class PrettyTableMixin(PrettyTable):
    FIELDS_NAMES = ["Name", "Phone"]
    rows = []

    def to_pretty(self):
        self.field_names = self.FIELDS_NAMES
        self.add_rows(self.rows)
        return self.get_string()

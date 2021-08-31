from mixin.pretty import PrettyTableMixin
from mixin.message import MessageMixin


class User(PrettyTableMixin, MessageMixin):
    FIELDS_NAMES = ["Name", "Phone"]

    def __init__(self, username, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.username = username
        self.contacts = []
        self.rows = self.contacts

    def __str__(self):
        return self.username

    def add_contact(self, contact):
        if contact not in self.contacts:
            self.contacts.append(contact)
            print(self.CONTACT_ADDED_MESSAGE.format(contact=contact))
        else:
            print(self.ALREADY_EXISTS_MESSAGE.format(contact=contact))

    def remove_contact(self, contact):
        if contact not in self.contacts:
            print(self.NOTFOUND_MESSAGE.format(contact=contact))
        else:
            print(self.REMOVED_MESSAGE.format(contact=contact))
            self.contacts.remove(contact)

    def search_by_name(self, name):
        pass

    def search_by_number(self, number):
        pass


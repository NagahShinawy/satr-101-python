from mixin.pretty import PrettyTableMixin
from mixin.message import MessageMixin


class User(PrettyTableMixin, MessageMixin):
    FIELDS_NAMES = ["Name", "Phone"]

    def __init__(self, username, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.username = username
        self.contacts = []
        self.rows = self.contacts

    @property
    def contacts_names(self):
        return [contact.name.lower() for contact in self.contacts]

    @property
    def contacts_phones(self):
        return [contact.phone for contact in self.contacts]

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

    def is_exists(self, name_or_number: str):
        name_or_number = name_or_number.lower()
        for contact in self.contacts:
            if contact.name.lower() == name_or_number or contact.phone.number == name_or_number:
                return contact
        return None

    def search_by_name(self, name: str):
        contact = self.is_exists(name)
        if contact:
            return contact.name
        return self.NOTFOUND_MESSAGE.format(contact=name)

    def search_by_number(self, number):
        contact = self.is_exists(number)
        if contact:
            return contact.phone
        return self.NOTFOUND_MESSAGE.format(contact=number)


class Message:
    text = None
    more_info = None


class DuplicatedNameMessage(Message):
    text = 'Duplicated name "{name}"'


class DuplicatedPhoneMessage(Message):
    text = 'Duplicated Phone "{phone}"'


class ContactAddedMessage(Message):
    text = 'contact "{contact}" was added'


class AlreadyExistsMessage(Message):
    text = 'contact "{contact}" was Found'


class MessageMixin:
    DUPLICATED_NAME_MESSAGE = DuplicatedNameMessage.text
    DUPLICATED_PHONE_MESSAGE = DuplicatedPhoneMessage.text
    CONTACT_ADDED_MESSAGE = ContactAddedMessage.text
    ALREADY_EXISTS_MESSAGE = AlreadyExistsMessage.text

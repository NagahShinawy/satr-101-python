from contact import Contact
from phone import Phone
from user import User


if __name__ == "__main__":
    phone1 = Phone(code="+20", number="0102890987")
    phone2 = Phone(code="+20", number="0100000000")
    phone3 = Phone(code="+20", number="0120000000")
    phone4 = Phone(code="+20", number="0110000000")
    phone5 = Phone(code="+20", number="0150000000")

    john = Contact(name="John", phone=phone1)
    james = Contact(name="James", phone=phone2)
    loen = Contact(name="Loen", phone=phone5)
    smith = Contact(name="Smith", phone=phone3)

    # ########### ########### ########### ########### ########### ########### ##########

    print(john.to_pretty())

    # ########### ########### ########### ########### ########### ########### ##########
    print("\n# ########### ########### ########### ########### ########### ########### ##########\n")

    adam = User("Adam")

    adam.add_contact(john)
    adam.add_contact(james)
    adam.add_contact(loen)
    adam.add_contact(loen)
    adam.remove_contact(james)
    adam.remove_contact(smith)

    # ########### ########### ########### ########### ########### ########### ##########
    print("\n# ########### ########### ########### ########### ########### ########### ##########\n")

    print(adam.to_pretty())

    # ########### ########### ########### ########### ########### ########### ##########
    print("\n# ########### ########### ########### ########### ########### ########### ##########\n")
    print(adam.search_by_name("johN"))
    print(adam.search_by_number("0150000000"))


















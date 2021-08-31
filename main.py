from contact import Contact
from phone import Phone


if __name__ == "__main__":
    phone1 = Phone(code="+20", number="0102890987")
    phone2 = Phone(code="+20", number="0100000000")
    phone3 = Phone(code="+20", number="0120000000")
    phone4 = Phone(code="+20", number="0110000000")
    phone5 = Phone(code="+20", number="0150000000")

    john = Contact(name="John", phone=phone1)
    james = Contact(name="James", phone=phone2)
    loen = Contact(name="Loen", phone=phone5)

    # ########### ########### ########### ########### ########### ########### ##########

    print(john.to_pretty())

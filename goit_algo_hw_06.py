from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Номер телефону повинен містити рівно 10 цифр")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def edit_phone(self, old_phone, new_phone):
        phone_objekt = self.find_phone(old_phone)
        if not phone_objekt:
            raise ValueError(f"Телефон {old_phone} не знайдено")
        new_phone_objekt = Phone(new_phone)
        index = self.phones.index(phone_objekt)
        self.phones[index] = new_phone_objekt


    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone):
        find_objekt = self.find_phone(phone)
        if find_objekt:
            self.phones.remove(find_objekt)


    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):

    def add_record(self, record):
            self.data[record.name.value] = record

    
    def find(self, name):
        return self.data.get(name)


    def delete(self, name):
        if name in self.data: 
            del self.data[name]
        

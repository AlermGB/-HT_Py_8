import json

phone_book = []
external_db = 'db.json'

def open_db():
    global phone_book
    global external_db
    with open(external_db, 'r', encoding = 'utf-8') as external:
        phone_book = json.load(external)

def save_db():
    with open(external_db, 'w', encoding='utf-8') as external:
        external.write(json.dumps(phone_book, ensure_ascii=False))

def get_phone_book():
    global phone_book
    return phone_book

def add_new_contact(new_contact: dict):
    global phone_book
    phone_book.append(new_contact)


def find(something: str):
    global phone_book
    result_of_find =[]
    for contact in phone_book:
        for element in contact.values():
            if something.lower() in element.lower():
                result_of_find.append(contact)
    return result_of_find


def get_person(id: int):
    global phone_book
    return phone_book[id - 1].get('Person')


def delete_contact(id: int):
    global phone_book
    phone_book.pop(id  - 1)


def change_info(id: int, contact: dict):
    global phone_book
    phone_book.pop(id - 1)
    phone_book.insert(id - 1, contact)
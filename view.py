# import os
def print_menu():
    # os.system('clear')
    print()
    print('''Меню
    1. Показать список контактов
    2. Создать контакт
    3. Изменить контакт
    4. Найти контакт
    5. Удалить контакт
    6. Сохранить изменения
    7. Выйти
    ''')
    user_select = input('Выберите пункт меню: ')
    print()
    return user_select


def print_contacts(phone_book: list[dict]):
    if phone_book == []:
        print('Телефонная книга пусти или файл не загружен.')
    else:
        for i, contact in enumerate(phone_book, 1):
            person = contact.get('Person')
            phone = contact.get('Phone')
            birthday = contact.get('Birthday')  
            email = contact.get('Email')  
            address = contact.get('Address')  
            print(f'{i}. {person: <20} {phone: <20} {birthday: <20} {email: <20} {address: <20}')


def create_new_contact():
    name = input("Введите Имя и Фамилию: ")
    phone = input("Введите номер телефона: ")
    birthday = input("Введите дату рождения: ")
    email = input("Введите адрес электронной почты: ")
    address = input("Введите домашний адрес: ")
    new_contact ={
      "Person": name,
      "Phone": phone,
      "Birthday": birthday,
      "Email": email,
      "Address": address
    }
    return new_contact


def any_find():
    find_something = input('Введите запрос: ')
    return find_something

def get_id():
    id = int(input('Введите номер контакта: '))
    return id

def confirm(condition: str, name: str):
    answer = input(f'Вы действительно хотите {condition} контакт {name} ? (y/n): ').lower()
    if answer == 'y': 
        return True
    else: 
        return False
import view
import db_manager

db_manager.open_db()


while True:
    user_select = view.print_menu()
    
    if user_select == '1':
        try:
            phone_book = db_manager.get_phone_book()
            view.print_contacts(phone_book)
        except:
            print('Что-то пошло не так! Повторите ввод.')    
    elif user_select == '2':
        try:
            new_contact = view.create_new_contact()
            db_manager.add_new_contact(new_contact)
        except:
            print('Что-то пошло не так! Повторите ввод.')     
    elif user_select ==  '3':
        try:
            pb = db_manager.get_phone_book()
            view.print_contacts(pb)
            id = view.get_id()
            contact = view.create_new_contact()
            db_manager.change_info(id, contact)
        except:
            print('Что-то пошло не так! Повторите ввод.')     
    elif user_select == '4':
        try:
            find = view.any_find()
            result = db_manager.find(find)
            view.print_contacts(result)
        except:
            print('Что-то пошло не так! Повторите ввод.')     
    elif user_select == '5':
        try:
            phone_book = db_manager.get_phone_book()
            view.print_contacts(phone_book)
            id = view.get_id()
            name = db_manager.get_person(id)
            if view.confirm('удалить', name):
                db_manager.delete_contact(id)
        except:
            print('Что-то пошло не так! Повторите ввод.')         
    elif user_select == '6':
        try:
            db_manager.save_db()
        except:
            print('Что-то пошло не так! Повторите ввод.')     
    elif user_select == '7':
            quit()
    else:
        print('Неверная команда. Повторите ввод.')
   
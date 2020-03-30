class Contact:
    def __init__(self, name, surname, number, favorite_contact=False, **kwargs):
        self.name = name
        self.surname = surname
        self.number = number
        self.favorite_contact = favorite_contact
        self.something_else = kwargs

    def __str__(self):
        keys = self.something_else.keys()
        if self.favorite_contact == True:
            favorite = 'Да'
        else:
            favorite = 'Нет'

        cool_string = (
            f'Имя: {self.name}\nФамилия: {self.surname}\nТелефон:{self.number}\nИзбранный контакт: {favorite}\n     Дополнительная инфа: \n')
        for key in keys:
            add_to_cool_string = (f'     {key}: {self.something_else.get(key)}')
            cool_string = cool_string + add_to_cool_string + '\n'
        return cool_string


phonebook_list = {
    'jhon': Contact('Jhon', 'Smith', '+71234567809', favorite_contact=True, telegram='@jhony', inst='@jhony'),
    'josh': Contact('Josh', 'sdsd', '+71234567808', favorite_contact=True, telegram='@wef', inst='@wef'),
    'ivan': Contact('Ivan', 'wed', '+71234567807', favorite_contact=False, telegram='@wew', twitter='@12345')
}


class phonebook:
    def __init__(self, phonebook_name):
        self.phonebook_name = phonebook_name

    def make_contact():
        global name
        name = input('Введите имя: ')
        name_for_contact = name
        surname = input('Введите фамилию: ')
        number = input('Введите номер телефона')
        if input("Если контакт избранный, введите цифру 1: ") == 1:
            favorite_contact = True
        else:
            favorite_contact = False
        make_more_data = "1"
        params = {}
        while make_more_data == "1":
            name_for_data = input('Введите название соц.сети/заголовка для дополнительных данных: ')
            data = input('Введите аккаунт/дополнительные сведения: ')
            make_more_data = input('Если хотите продолжить ввод эллементов нажмите 1: ')
            params[name_for_data] = data

        name = Contact(name, surname, number, favorite_contact=favorite_contact, **params)
        phonebook_list[name_for_contact] = name

    def show_contact_by_name_and_surname(name, surname):
        count_contact = 0
        for i in phonebook_list.keys():
            if phonebook_list[i].name == name and phonebook_list[i].surname == surname:
                print(phonebook_list[i])
                count_contact = 1
        if count_contact == 0:
            print("Контакт не найден")

    def show_all_contact():
        for i in phonebook_list:
            print(phonebook_list[i])

    def del_contact_by_number(number):
        list_to_del = []
        for i in phonebook_list.keys():
            if phonebook_list[i].number == number:
                list_to_del.append(i)
        if len(list_to_del) > 0:
            for del_contact in list_to_del:
                del phonebook_list[del_contact]
                print(f'контакт {del_contact} удален')
        else:
            print("Контакт не найден")

    def find_favorite_contacts():
        str_favorite_contacts = ""
        count = 0
        for i in phonebook_list.keys():
            if phonebook_list[i].favorite_contact == True:
                if count == 0:
                    str_favorite_contacts = str_favorite_contacts + i
                    count = 1
                else:
                    str_favorite_contacts = str_favorite_contacts + ", " + i
        print(f'Лист избранных контактов: {str_favorite_contacts}')


def phone_book_app():
    new_phone_book = phonebook
    new_phone_book.phonebook_name = input("введите наименование телефонной книги: ")
    app_work = "1"
    while app_work == "1":
        task = input("\nЧто вы хотите сделать?\nПоказать все контакты - введите 1\nДобавить новый контакт - 2"
                     "\nУдалить контакт по номеру телефона - 3"
                     "\nПоказать все избранные контакты - 4"
                     "\nПоиск контакта по имени и фамилии -5"
                     "\nВыйти из приложения - 6\n")
        if task == "1":
            new_phone_book.show_all_contact()
        elif task == "2":
            new_phone_book.make_contact()
        elif task == "3":
            new_phone_book.del_contact_by_number(input("введите номер: "))
        elif task == "4":
            new_phone_book.find_favorite_contacts()
        elif task == "5":
            new_phone_book.show_contact_by_name_and_surname(input("Введите имя"), input('Введите фамилию: '))
        elif task == "6":
            app_work = "0"
            print("Пока")
        else:
            print("Попробуйте ввести команду еще раз")


phone_book_app()

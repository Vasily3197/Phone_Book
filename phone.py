# -*- coding: utf-8 -*import 
import os 
os.system('cls' if os.name == 'nt' else 'clear') # Что бы очищать консоль после заапуска программы


phone_book = {} 
PATH = 'Phones.txt' # Из файла 

# 1
def open_file(book: dict):                       # Открытие файла
    with open(PATH, 'r') as file:
        data = file.readlines()
    for i, contact in enumerate(data,1):
        contact = contact.strip().split(';')
        book[i] = contact

# 2
def save_file(book: dict):                       # Сохранение файла
    all_contacts = []
    for contact in book.values():
        all_contacts.append(';'.join(contact))
    with open(PATH, 'w') as file:
        file.write('\n'.join(all_contacts))

# 3
def show_contacts(book: dict, message: str):     # Показать контакты
    print('\n' + '=' * 67) # Обрамление сверху и снизу
    if book:
        for i, contact in book.items():
            print(f'{i:>3}. {contact[0]:<20} {contact[1]:<20} {contact[2]:<20}') # Отступы и равнение 
    else:
        print(message)
    print('=' * 67 + '\n')

# 4
def add_new_contact(book: dict, new: list):      # Добавить новый контакт
    cur_id = max(book.keys()) + 1
    book[cur_id] = new

# 5
def find_contact(book: dict, search: str):       # Поиск контакта
    result = {}                                  # Пустой словарь, что бы программа не искала первый подходящий контакт
    for i, contact in book.items():              # Проход по телефонной книге
        for filed in contact:                    # Отдельно берём поля телефоннок книги
            if search in filed.lower():          # Ищем совпадения
                result[i] = contact               
                break
    return result                                # Выводим словарь на печать

#6
def func_search(book: dict):                     # Функция поиска
    search = input('What are we going to look for?: ')
    result = find_contact(book, search)
    show_contacts(result, f'The contact containing the {search} was not found')

#7
def ch_contact(book: dict, cid: int ):           # Измененеие контакта
    name, phone, comment = book.get(cid)         # Разворачиваем телефонную книгу
    ch = []                                      # Создаание нового контакта
    for item in ['Enter a new name (leave it empty so as not to change): ', 
                 'Enter phone number (leave it empty so as not to change): ', 
                 'Enter comment (leave it empty so as not to change): ']:
        ch.append((input(item)))
    book[cid] = [ch[0] if ch[0] else name, ch[1] if ch[1] else phone, ch[2] if ch[2] else comment ] # Если значение 0, то остается старое значение
    return ch[0] if ch[0] else name # Вернёт новое имя, или старое, если не изменяли

#8
def delete_contact(book: dict, cid: int):        # Удаление контакта
    name = book.pop(cid)
    return name[0]

def menu():                                      # Меню
    menu_points = ['Open file',
                   'Save file',
                   'Viev all contacts',
                   'Add a contact',
                   'Find a contact',
                   'Change contact',
                   'Delete a contact',
                   'Exit']
    print('Main menu')
    [print(f'\t{i}. {item}') for i, item in enumerate (menu_points, 1)] # enemerate - Для того, что бы били порядковые номера
    choice = int(input('Select the menu item: '))
    return choice

while True:
    choice = menu()
    match choice: 
            case 1: 
                open_file(phone_book)
                print('\nPhone book opened successfully!\n')

            case 2:
                save_file(phone_book)
                print('\nPhone book saved successfully!\n')

            case 3:
                show_contacts(phone_book, 'The phone book is empty or not open')

            case 4: 
                new = []
                for item in ['Enter name: ', 'Enter phone number: ', 'Enter comment: ']:
                    new.append((input(item)))
                add_new_contact(phone_book, new)
                print(f'\nContact successfully added\n')

            case 5:
                func_search(phone_book)

            case 6:
                func_search(phone_book)
                select = int(input('Which contact will we change? '))
                name = ch_contact(phone_book, select)
                print(f'\nContact {name} has been successfully changed\n')

            case 7:
                func_search(phone_book)
                select = int(input('Which contact will we delete? '))
                name = delete_contact(phone_book, select)
                print(f'\nContact {name} has been successfully deleted\n')
                
            case 8:
                print('\nGood luck!')
                break
    

        
        
        
        
                                
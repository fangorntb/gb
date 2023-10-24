from dataclasses import dataclass
import json


@dataclass
class Contact:
    first_name: str
    last_name: str
    phone_number: str


def load_phone_book():
    try:
        with open("phone_book.json", "r") as file:
            data = json.load(file)
            return [Contact(**contact_data) for contact_data in data]
    except FileNotFoundError:
        return []


def save_phone_book(contacts):
    data = [{"first_name": contact.first_name, "last_name": contact.last_name, "phone_number": contact.phone_number} for
            contact in contacts]
    with open("phone_book.json", "w", encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def add_contact(first_name, last_name, phone_number):
    contacts = load_phone_book()
    contact = Contact(first_name, last_name, phone_number)
    contacts.append(contact)
    save_phone_book(contacts)
    print(f"Контакт {first_name} {last_name} добавлен в справочник.")


def update_contact(first_name, last_name, new_phone_number):
    contacts = load_phone_book()
    updated = False
    for contact in contacts:
        if contact.first_name == first_name and contact.last_name == last_name:
            contact.phone_number = new_phone_number
            updated = True
            break
    if updated:
        save_phone_book(contacts)
        print(f"Контакт {first_name} {last_name} обновлен.")
    else:
        print(f"Контакт {first_name} {last_name} не найден.")


def delete_contact(first_name, last_name):
    contacts = load_phone_book()
    removed = False
    for contact in contacts:
        if contact.first_name == first_name and contact.last_name == last_name:
            contacts.remove(contact)
            removed = True
            break
    if removed:
        save_phone_book(contacts)
        print(f"Контакт {first_name} {last_name} удален из справочника.")
    else:
        print(f"Контакт {first_name} {last_name} не найден.")


def main():
    while True:
        print("1. Добавить контакт")
        print("2. Обновить контакт")
        print("3. Удалить контакт")
        print("4. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            first_name = input("Введите имя: ")
            last_name = input("Введите фамилию: ")
            phone_number = input("Введите номер телефона: ")
            add_contact(first_name, last_name, phone_number)
        elif choice == "2":
            first_name = input("Введите имя: ")
            last_name = input("Введите фамилию: ")
            phone_number = input("Введите новый номер телефона: ")
            update_contact(first_name, last_name, phone_number)
        elif choice == "3":
            first_name = input("Введите имя: ")
            last_name = input("Введите фамилию: ")
            delete_contact(first_name, last_name)
        elif choice == "4":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()

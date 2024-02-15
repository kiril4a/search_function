contacts = []

def add_contact(name, phone_number):
    contacts.append({'name': name, 'phone_number': phone_number})

def search_contacts(dictionary, query): #функція пошуку контакту за ім'ям/ частиною імені, де перший аргумент це словник, а другий це ключове слово для пошуку. 
    results = []
    name = 'name' #змінна яка вказує де знаходяться імена в словнику.
    for contact in dictionary:
        if query.lower() in contact[name].lower():
            results.append(contact)
    return results

def main():
    while True:
        print("\n1. Додати контакт")
        print("2. Пошук за іменем")
        print("3. Вихід")

        choice = input("Виберіть опцію (1/2/3): ")

        if choice == '1':
            name = input("Введіть ім'я контакту: ")
            phone_number = input("Введіть номер телефону: ")
            add_contact(name, phone_number)
            print("Контакт успішно доданий!")

        elif choice == '2':
            search_query = input("Введіть ім'я або його частину для пошуку: ")
            search_results = search_contacts(contacts, search_query)
            if not search_results:
                print("Контакти не знайдені.")
            else:
                print("\nЗнайдені контакти:")
                for result in search_results:
                    print(f"Ім'я: {result['name']}, Телефон: {result['phone_number']}")

        elif choice == '3':
            print("Дякую за використання програми. До побачення!")
            break

        else:
            print("Невірний вибір. Будь ласка, виберіть правильну опцію.")

if __name__ == "__main__":
    main()

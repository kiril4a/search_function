notes = []

def add_note():
    title = input("Введіть заголовок нотатки: ")
    content = input("Введіть текст нотатки: ")
    tags = input("Введіть теги (розділіть їх комами): ").split(', ')
    
    note = {'title': title, 'content': content, 'tags': tags}
    notes.append(note)
    print("Нотатка успішно додана!")

def view_notes():
    if not notes:
        print("Немає доступних нотаток.")
        return

    for i, note in enumerate(notes):
        print(f"\nНотатка {i + 1}:")
        print(f"Заголовок: {note['title']}")
        print(f"Текст: {note['content']}")
        print(f"Теги: {', '.join(note['tags'])}")

def search_by_tag():
    tag_to_search = input("Введіть тег для пошуку: ")
    matching_notes = [note for note in notes if tag_to_search.lower() in map(str.lower, note['tags'])]
    
    if matching_notes:
        print(f"\nЗнайдені нотатки за тегом '{tag_to_search}':")
        for i, note in enumerate(matching_notes):
            print(f"\nНотатка {i + 1}:")
            print(f"Заголовок: {note['title']}")
            print(f"Текст: {note['content']}")
            print(f"Теги: {', '.join(note['tags'])}")
    else:
        print(f"Нотаток з тегом '{tag_to_search}' не знайдено.")

def main():
    while True:
        print("\n1. Додати нотатку")
        print("2. Переглянути нотатки")
        print("3. Пошук за тегом")
        print("4. Вийти")

        choice = input("\nВиберіть опцію: ")

        if choice == '1':
            add_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            search_by_tag()
        elif choice == '4':
            print("До побачення!")
            break
        else:
            print("Некоректний вибір. Спробуйте знову.")

if __name__ == "__main__":
    main()

def search_contacts(dictionary, query): #функція пошуку контакту за ім'ям/ частиною імені, де перший аргумент це словник, а другий це ключове слово для пошуку. 
    results = []
    name = 'name' #змінна яка вказує де знаходяться імена в словнику.
    for contact in dictionary:
        if query.lower() in contact[name].lower():
            results.append(contact)
    return results
import os
import json

from add import add
from edit import edit
from search import search


class Directory:
    def __init__(self, file_name: str):
        """
        Инициализация класса Directory.
        :param file_name: Имя файла, в котором хранятся записи.
        :type file_name: str
        """
        self.file_name = file_name
        self.entries = self.load_entries()
        self.next_id = max((entry['id'] for entry in self.entries), default=-1) + 1 if self.entries else 0

    def load_entries(self) -> list:
        """
        Загрузка записей из файла.
        :return: Список записей.
        :rtype: list
        """
        if not os.path.exists(self.file_name):
            return []
        with open(self.file_name, 'r', encoding='utf-8') as file:
            try:
                entries = json.load(file)
            except json.JSONDecodeError:
                entries = []
        return entries

    def add_entry(self, entry: dict):
        """
        Добавление новой записи в справочник.
        :param entry: Новая запись.
        :type entry: dict
        """
        entry['id'] = self.next_id
        self.next_id += 1
        self.entries.append(entry)
        self.save_entries()

    def edit_entry(self, id: int, new_entry: dict):
        """
        Редактирование записи в справочнике.
        :param id: Идентификатор записи для редактирования.
        :type id: int
        :param new_entry: Обновленная запись.
        :type new_entry: dict
        """
        for i, entry in enumerate(self.entries):
            if entry['id'] == id:
                self.entries[i] = new_entry
                self.entries[i]['id'] = id
                self.save_entries()
                return
        print("Запись с таким id не найдена.")
        '''
        for i, entry in enumerate(self.entries):
            if entry['id'] == id:
            self.entries[i].update(new_entry)
            self.save_entries()
            return
        print("Запись с таким id не найдена.")'''

    def search_entries(self, search_terms: dict) -> list:
        """
        Поиск записей по одной или нескольким характеристикам.
        :param search_terms: Словарь с характеристиками для поиска.
        :type search_terms: dict
        :return: Список найденных записей.
        :rtype: list
        """
        results = []
        for entry in self.entries:
            if all(term.lower() in entry[key].lower() for key, term in search_terms.items()):
                results.append(entry)
        return results

    def print_entries(self, entries: list):
        """
        Вывод записей на экран.
        :param entries: Список записей для вывода.
        :type entries: list
        """
        print()
        for i, entry in enumerate(entries):
            print(f"Запись - {i}")
            print(f"Фамилия - {entry['last_name']}")
            print(f"Имя - {entry['first_name']}")
            print(f"Отчество - {entry['patronymic']}")
            print(f"Организация - {entry['organization']}")
            print(f"Рабочий телефон - {entry['work_phone']}")
            print(f"Личный телефон - {entry['personal_phone']}")
            print("________________________________________")

    def save_entries(self):
        """
        Сохранение записей в файл.
        """
        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(self.entries, file, ensure_ascii=False, indent=4)
        self.entries = self.load_entries()  # Обновление списка записей после сохранения (while running).


def main():
    directory = Directory('directory.json')
    try:
        while True:
            print("\n1. Вывод записей из справочника постранично")
            print("2. Добавление новой записи")
            print("3. Редактирование записей")
            print("4. Поиск записей по одной или нескольким характеристикам")
            print("5. Выход")
            choice = input("Введите пункт: ")
            if choice == '1':
                page_number = int(input("Введите номер страницы: "))
                entries_per_page = 10
                start_index = (page_number - 1) * entries_per_page
                end_index = start_index + entries_per_page
                entries = directory.entries[start_index:end_index]
                directory.print_entries(entries)
            elif choice == '2':
                directory.add_entry(add(directory))
            elif choice == '3':
                id_input = input("Введите id записи для редактирования: ")
                if not id_input.isdigit():
                    print("Некорректный ввод. id должен быть числом.")
                    continue
                edit(directory, id_input)
            elif choice == '4':
                results = directory.search_entries(search(directory))
                directory.print_entries(results)
            elif choice == '5':
                print("Спасибо за использование справочника! До свидания!")
                break
    except KeyboardInterrupt:
        print("\nСпасибо за использование справочника! До свидания!")


if __name__ == "__main__":
    main()

Телефонный справочник
Описание

Этот проект представляет собой консольное приложение для управления телефонным справочником. Он позволяет добавлять, редактировать и искать записи в справочнике. Данные хранятся в текстовом файле в формате JSON.
Структура проекта:

Проект состоит из следующих файлов:

    main.py: Главный файл, который содержит основной код программы.
    add.py: Файл, содержащий функцию для добавления новой записи в справочник.
    edit.py: Файл, содержащий функцию для редактирования существующей записи в справочнике.
    search.py: Файл, содержащий функцию для поиска записей в справочнике.
    test.py: Файл, содержащий тесты для проверки корректности работы программы.

Компоненты программы

Класс Directory

Класс Directory в файле main.py представляет собой основной компонент программы. Он содержит методы для загрузки записей из файла, добавления новой записи, редактирования существующей записи, поиска записей и сохранения записей в файл.

Функции add, edit и search

Функции add, edit и search в файлах add.py, edit.py и search.py соответственно представляют собой вспомогательные функции, которые используются для добавления новой записи, редактирования существующей записи и поиска записей в справочнике.

Тесты

Файл test.py содержит тесты для проверки корректности работы программы. Он использует модуль unittest для написания и выполнения тестов.

Использование программы

При запуске программы(main.py) пользователю предлагается выбрать одну из следующих операций:

    Вывод записей из справочника постранично
    Добавление новой записи
    Редактирование записей
    Поиск записей по одной или нескольким характеристикам
    Выход

Пользователь может выбрать операцию, введя соответствующий номер. Затем программа предлагает пользователю ввести необходимые данные для выполнения выбранной операции.

Заключение

Этот проект является примером простого, но функционального консольного приложения для управления телефонным справочником. Он демонстрирует использование различных концепций программирования, таких как работа с файлами, обработка исключений, регулярные выражения и модульное тестирование. Проект хорошо структурирован и легко расширяем.

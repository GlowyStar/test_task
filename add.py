import re

simbols = "^[А-Яа-яЁёA-Za-z]{1,100}$"
def add(directory):
    entry = {}
    prompts = [
        ("Введите фамилию: ", "last_name", simbols, "Фамилия должна содержать только буквы и быть не длиннее 100 символов."),
        ("Введите имя: ", "first_name", simbols, "Имя должно содержать только буквы и быть не длиннее 100 символов."),
        ("Введите отчество: ", "patronymic", simbols, "Отчество должно содержать только буквы и быть не длиннее 100 символов."),
        ("Введите название организации: ", "organization", ".{0,255}", "Название организации должно быть не длиннее 255 символов."),
        ("Введите рабочий телефон: ", "work_phone", "^\d{11}$", "Рабочий телефон должен содержать 11 цифр без пробелов и других символов."),
        ("Введите личный телефон: ", "personal_phone", "^\d{11}$", "Личный телефон должен содержать 11 цифр без пробелов и других символов.")
    ]

    for prompt, key, pattern, error_message in prompts:
        while True:
            data = input(prompt)
            if not re.match(pattern, data):
                print(error_message)
                continue
            if key in ['work_phone', 'personal_phone']:
                data = f"{data[:1]}({data[1:4]}) {data[4:7]}-{data[7:9]}-{data[9:]}"
            entry[key] = data
            break

    print("Запись успешно добавлена!")
    return entry


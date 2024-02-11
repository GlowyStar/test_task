import re

simbols = "^[А-Яа-яЁёA-Za-z]{1,100}$"


def edit(directory, id_input):
    id = int(id_input)
    for entry in directory.entries:
        if entry['id'] == id:
            prompts = [
                ("Введите новую фамилию (оставьте пустым, чтобы оставить текущую): ", "last_name", simbols, "Фамилия должна содержать только буквы и быть не длиннее 100 символов."),
                ("Введите новое имя (оставьте пустым, чтобы оставить текущее): ", "first_name", simbols, "Имя должно содержать только буквы и быть не длиннее 100 символов."),
                ("Введите новое отчество (оставьте пустым, чтобы оставить текущее): ", "patronymic", simbols, "Отчество должно содержать только буквы и быть не длиннее 100 символов."),
                ("Введите новое название организации (оставьте пустым, чтобы оставить текущее): ", "organization", ".{0,255}", "Название организации должно быть не длиннее 255 символов."),
                ("Введите новый рабочий телефон (оставьте пустым, чтобы оставить текущий): ", "work_phone", "^\d{11}$", "Рабочий телефон должен содержать 11 цифр без пробелов и других символов."),
                ("Введите новый личный телефон (оставьте пустым, чтобы оставить текущий): ", "personal_phone", "^\d{11}$", "Личный телефон должен содержать 11 цифр без пробелов и других символов.")
            ]

            for prompt, key, pattern, error_message in prompts:
                while True:
                    new_data = input(prompt)
                    if not new_data:  # Если пользователь ничего не ввел, скип
                        break
                    if not re.match(pattern, new_data):
                        print(error_message)
                        continue
                    if key in ['work_phone', 'personal_phone']:
                        new_data = f"{new_data[:1]}({new_data[1:4]}) {new_data[4:7]}-{new_data[7:9]}-{new_data[9:]}"
                    entry[key] = new_data
                    break

            directory.save_entries()
            print("Запись успешно обновлена!")
            break
        else:
            print("Запись с таким id не найдена.")

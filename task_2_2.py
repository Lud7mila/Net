HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""

today_tasks = []  # список задач на сегодня
tomorrow_tasks = []  # список задач на завтра
other_tasks = []  # список задач на другое время

while 1:
    command = input('\nВведите команду: ')

    if command == 'help':
        print(HELP)
    elif command == 'add':
        task = input('Введите название задачи: ')
        time = input("Введите дату выполнения задачи: ").lower()
        if time == 'today':
            today_tasks.append(task)
        if time == 'tomorrow':
            tomorrow_tasks.append(task)
        else:
            other_tasks.append(task)
        print('Задача добавлена!')

    elif command == 'show':
        print(f'Задачи на сегодня: {today_tasks}')
        print(f'Задачи на завтра: {tomorrow_tasks}')
        print(f'Задачи на другие дни: {other_tasks}')
    elif command == 'exit':
        print('Спасибо за использование! До свидания!')
        break
    else:
        print('Неизвестная команда. До свидания!')
        break
tasks = []
dates = []
for _ in range(0, 3):
    dates.append(input('Введите дату: '))
    tasks.append(input('Введите задачу: '))

for ind in range(0, 3):
    print(dates[ind], tasks[ind])
def read_data_from_file(name): # функция для чтения данных из файлов 'txt'
    result = []
    with open(name, 'r', encoding='utf8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').split(','))
        return result

def add_item_to_file(name, rawdata): # функция на добавление данных в текстовый документ
    with open(name, 'a', encoding='utf8') as datafile: # открыл файл, он сам закроется
        datafile.write(', '.join(rawdata)+'\n') # запись в одну стороку через запятую в пробелом и переход на новую строку


def print_bus(): # функция для печати в терминале инфо об автобусах из 'bus.txt'
    bus = read_data_from_file('bus.txt')
    count = 0
    print('_'*35)
    print('| Название автобуса  | Гос.номер  |')
    print('-'*35)
    for name_bus, num_bus in bus: # цикл для последующей печати в заданных границах
        count += 1
        print('|{:>2}{:>18}|{:>12}| '.format(count, name_bus, num_bus))
    

def add_bus(): # функция для добавления данных об автобусах в 'bus.txt'
    name, number = input('Введите название автобуса: '), input('Введите гос. номер: ')
    add_item_to_file('bus.txt', [name, number])
    print('Информация об автобус добавлена.')
    

    

def del_data_bus_number():
    '''удаление по порядковому номеру записи'''
    while True:
        print_bus()
        answer = input("Номер строки для удаления(Q - выход)>: ")
        if answer.upper() == "Q":
            return
        if not answer.isnumeric():
            continue
        answer = int(answer)
        print(answer)
        phonedata = ""
        count = 0
        with open('bus.txt', "r", encoding="utf8") as datafile:
            for line in datafile:
                count += 1
                if answer == count:
                    continue
                phonedata += line

        with open('bus.txt', "w", encoding="utf8") as datafile:
            datafile.write(phonedata)

def search_bus():
    return

def print_driver(): # функция для печати в терминале инфо о водителях из 'driver.txt'
    drivers = read_data_from_file('driver.txt')
    count = 0
    print('_'*32)
    print('| Имя водителя  |    Фамилия   |')
    print('-'*32)
    for num_driver, surname_driver in drivers: # цикл для печати данных в заданных границах
        count += 1
        print('|{:>2}{:>13s}|{:>14s}|'.format(count, num_driver, surname_driver))
    

def add_driver(): # функция добавления данных о водителях в 'driver.txt'
    num_driver, surname_driver = input('Введите id водителя: '), input('Введите фамилию водителя: ')
    add_item_to_file('driver.txt', [num_driver, surname_driver])
    print('Информация о водителе добавлена')

def del_data_driver_number(): # функция удаления записи по номеру строки
    while True:
        print_driver()
        answer = input("Номер строки для удаления(Q - выход)>: ")
        if answer.upper() == "Q":
            return
        if not answer.isnumeric():
            continue
        answer = int(answer)
        print(answer)
        phonedata = ""
        count = 0
        with open('driver.txt', "r", encoding="utf8") as datafile:
            for line in datafile:
                count += 1
                if answer == count:
                    continue
                phonedata += line

        with open('driver.txt', "w", encoding="utf8") as datafile:
            datafile.write(phonedata)

def search_driver():
    return

def print_route():
    route = read_data_from_file('marshrut.txt')
    count = 0
    print('_' * 47)
    print(' № | id | Номер маршрута | Автобус | Водитель |')
    print('-' * 47)
    for id, numRoute, busRoute, drRoute in route:
        count += 1
        print('{:3}|{:>4}|{:>16}|{:>9}|{:>10}|'.format(count, id, numRoute, busRoute, drRoute))
    

def add_route():
    id_route = input('Введите id маршрута: ')
    num_route = input('Введите номер маршрута: ')
    bus_route = input('Укажите автобус для текущего маршрута: ')
    driver_route = input('Укажите водителя для текущего маршрута: ')
    add_item_to_file('marshrut.txt', [id_route, num_route, bus_route, driver_route])
    print('Информация о маршруте добавлена')

def del_data_route_number():
    '''удаление по порядковому номеру записи'''
    while True:
        print_route()
        answer = input("Номер стороки для удаления(Q - выход)>: ")
        if answer.upper() == "Q":
            return
        if not answer.isnumeric():
            continue
        answer = int(answer)
        print(answer)
        phonedata = ""
        count = 0
        with open('marshrut.txt', "r", encoding="utf8") as datafile:
            for line in datafile:
                count += 1
                if answer == count:
                    continue
                phonedata += line

        with open('marshrut.txt', "w", encoding="utf8") as datafile:
            datafile.write(phonedata)

def search_route():
    return
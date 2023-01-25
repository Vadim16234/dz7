from menu import Menu
import function as fn

# if __name__ == "__main__":
#     # основной блок
menuitems = [
        ("1", "Вывод автобусов", fn.print_bus),
        ("2", "Добавление автобуса", fn.add_bus),
        ("3", "Удаление данных об автобусе", fn.del_data_bus_number),
        ("4", "Вывод водителей", fn.print_driver),
        ("5", "Добавление водителей", fn.add_driver),
        ("6", "Удаление данных о водителе", fn.del_data_driver_number),
        ("7", "Вывод маршрута", fn.print_route),
        ("8", "Добавление маршрута", fn.add_route),
        ("9", "Удаление данных о маршруте", fn.del_data_route_number),
        ("10", "Выход", lambda: exit())]

menu = Menu(menuitems)
    # menu.run('>:')

for i in menuitems:
    print(i[0], i[1])

text = input('Выберите действие: ')
if text == '0':
    print('Неверный ввод')
elif text == '1':
    print(fn.print_bus())
elif text == '2':
    fn.add_bus()
elif text == '3':
    fn.del_data_bus_number()
elif text == '4':
    print(fn.print_driver())
elif text == '5':
    fn.add_driver()  
elif text == '6':
    fn.del_data_driver_number()
elif text == '7':
    print(fn.print_route())
elif text == '8':
    fn.add_route()
elif text == '9':
    fn.del_data_route_number()
elif text == '10':
    print()
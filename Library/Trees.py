from tkinter import *
from ttkthemes import ThemedStyle
from tkinter import messagebox
from tkinter import ttk
import Datas as prog
import Filter as filtr
from random import randint
import Charts as ch

# Для открытия/закрытия фильтра
global check_open
check_open = False


def open_tables():
    """
    Автор: Исмаилов Асад
    Цель: Вывод данных таблицы в treeview
    Вход: Нет входных данных
    Выход: Обновленный treeview (с добавленными из таблицы данными)

    """
    prog.insert_type(tree_type) # Вывод данных из Excel в treeview
    prog.insert_orders(tree_orders) # Вывод данных из Excel в treeview
    prog.insert_menu(tree_menu) # Вывод данных из Excel в treeview
    prog.insert_full(tree_full) # Вывод данных из Excel в treeview


#Создание таблицы типа блюд
def create_tree_type(f_type, root):
    """
    Автор: Ворожцов Михаил
    Цель: Создание treeview c таблицей типов блюд. Cоздаем scroll для этого treeview
    Вход: f_type (рамка в данном разделе note_tree), root
    Выход: Глобальные переменные(tree_type,check_open)

    """
    global tree_type
    global check_open
    check_open = False

    #Создаем дерево
    tree_type = ttk.Treeview(f_type, style="style.Treeview")
    tree_type.pack(side = 'left', fill = 'y')


    #Присоединим scroll к tree
    def create_scroll_type():
        global scroll_type
        scroll_type = ttk.Scrollbar(f_type, orient="vertical", command=tree_type.yview)
        scroll_type.pack(side='left', fill='y')
        tree_type.configure(yscrollcommand=scroll_type.set)  # прикрепляем scroll к tree
    create_scroll_type()

    #Объявляем столбцы
    tree_type["columns"] = ("one")
    tree_type.column("#0", width=370, minwidth=100)
    tree_type.column("#1", width=880, minwidth=130)

    tree_type.heading("#0", text="Тип блюда", anchor=W, command=lambda:filtr.create_filter(root, check_open, tree_type, "Тип блюда", "0"))
    tree_type.heading("#1", text="Название", anchor=W, command=lambda:filtr.create_filter(root, check_open, tree_type, "Название", "1"))


#Создание таблицы заказов
def create_tree_orders(f_orders, root):
    """
        Автор: Ворожцов Михаил
        Цель: Создание treeview c таблицей заказов. Cоздаем scroll для этого treeview
        Вход: f_type (рамка в данном разделе note_tree), root
        Выход: Глобальные переменные(tree_orders,check_open)

    """
    global tree_orders
    global check_open
    check_open = False

    #Создаем дерево
    tree_orders = ttk.Treeview(f_orders, style="style.Treeview")
    tree_orders.pack(side = 'left', fill = 'y')

    #Присоединим scroll к tree
    def create_scroll_orders():
        global scroll_orders
        scroll_orders = ttk.Scrollbar(f_orders, orient="vertical", command=tree_orders.yview)
        scroll_orders.pack(side='left', fill='y')
        tree_orders.configure(yscrollcommand=scroll_orders.set)  # прикрепляем scroll к tree
    create_scroll_orders()

    #Объявляем столбцы
    tree_orders["columns"] = ("one", "two", "three", "four", "five")
    tree_orders.column("#0", width=200, minwidth=100)
    tree_orders.column("#1", width=270, minwidth=130)
    tree_orders.column("#2", width=250, minwidth=130)
    tree_orders.column("#3", width=170, minwidth=150)
    tree_orders.column("#4", width=190, minwidth=120)
    tree_orders.column("#5", width=170, minwidth=120)

    tree_orders.heading("#0", text="Код заказа", anchor=W, command=lambda:filtr.create_filter(root, check_open, tree_orders, "Код заказа", "0"))
    tree_orders.heading("#1", text="Дата посещения", anchor=W, command=lambda:filtr.create_filter(root, check_open, tree_orders, "Дата посещения", "1"))
    tree_orders.heading("#2", text="Время посещения", anchor=W, command=lambda:filtr.create_filter(root, check_open, tree_orders, "Время посещения", "2"))
    tree_orders.heading("#3", text="Код блюда", anchor=W, command=lambda:filtr.create_filter(root, check_open, tree_orders, "Код блюда", "3"))
    tree_orders.heading("#4", text="Количество порций", anchor=W, command=lambda:filtr.create_filter(root, check_open, tree_orders, "Количество порций", "4"))
    tree_orders.heading("#5", text="Сумма заказа", anchor=W, command=lambda:filtr.create_filter(root, check_open, tree_orders, "Сумма заказа", "5"))

    tree_orders.tag_configure("COLOR", background = '#fff8dc')#у каждой четной делай bg
    

#Создание таблицы меню
def create_tree_menu(f_menu, root):
    """
        Автор: Ворожцов Михаил
        Цель: Создание treeview c таблицей меню. Cоздаем scroll для этого treeview
        Вход: f_type (рамка в данном разделе note_tree), root
        Выход: Глобальные переменные(tree_menu)

    """
    global tree_menu
    #Создаем дерево
    tree_menu = ttk.Treeview(f_menu, style="style.Treeview")
    tree_menu.pack(side = 'left', fill = 'y')

    #Присоединим scroll к tree
    def create_scroll_menu():
        global scroll_menu
        scroll_menu = ttk.Scrollbar(f_menu, orient="vertical", command=tree_menu.yview)
        scroll_menu.pack(side='left', fill='y')
        tree_menu.configure(yscrollcommand=scroll_menu.set)  # прикрепляем scroll к tree
    create_scroll_menu()

    #Объявляем столбцы
    tree_menu["columns"] = ("one", "two", "three", "four")
    tree_menu.column("#0", width=240, minwidth=100)
    tree_menu.column("#1", width=320, minwidth=130)
    tree_menu.column("#2", width=270, minwidth=130)
    tree_menu.column("#3", width=220, minwidth=150)
    tree_menu.column("#4", width=200, minwidth=120)

    tree_menu.heading("#0", text="Код блюда", anchor=W, command=lambda:filtr.create_filter(root, check_open, tree_menu, "Код блюда", "0"))
    tree_menu.heading("#1", text="Наименование блюда", anchor=W, command=lambda:filtr.create_filter(root, check_open, tree_menu, "Наименование блюда", "1"))
    tree_menu.heading("#2", text="Стоимость", anchor=W, command=lambda:filtr.create_filter(root, check_open, tree_menu, "Стоимость", "2"))
    tree_menu.heading("#3", text="Размерность", anchor=W, command=lambda:filtr.create_filter(root, check_open, tree_menu, "Размерность", "3"))
    tree_menu.heading("#4", text="Тип блюда", anchor=W, command=lambda:filtr.create_filter(root, check_open, tree_menu, "Тип блюда", "4"))


#Создаем полную таблицу
def create_tree_full(f_full, root):
    """
        Автор: Ворожцов Михаил
        Цель: Создание treeview c полной таблицей. Cоздаем scroll для этого treeview
        Вход: f_type (рамка в данном разделе note_tree), root
        Выход: Глобальные переменные(tree_full)

    """
    global tree_full

    #Создаем дерево
    tree_full = ttk.Treeview(f_full, style="style.Treeview")
    tree_full.pack(side = 'left', fill = 'y')

    #Присоединим scroll к tree
    def create_scroll_full():
        global scroll_full
        scroll_full = ttk.Scrollbar(f_full, orient="vertical", command=tree_full.yview)
        scroll_full.pack(side='left', fill='y')
        tree_full.configure(yscrollcommand=scroll_full.set)  # прикрепляем scroll к tree
    create_scroll_full()

    #Объявляем столбцы
    tree_full["columns"] = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    tree_full.column("#0", width=100, minwidth=100)
    tree_full.column("#1", width=170, minwidth=130)
    tree_full.column("#2", width=100, minwidth=100)
    tree_full.column("#3", width=110, minwidth=110)
    tree_full.column("#4", width=100, minwidth=100)
    tree_full.column("#5", width=100, minwidth=100)
    tree_full.column("#6", width=130, minwidth=130)
    tree_full.column("#7", width=150, minwidth=130)
    tree_full.column("#8", width=170, minwidth=150)
    tree_full.column("#9", width=120, minwidth=120)

    tree_full.heading("#0", text="Код блюда", anchor=W, command= lambda:filtr.create_filter(root, check_open, tree_full, "Код блюда", "0"))
    tree_full.heading("#1", text="Наименование блюда", anchor=W, command= lambda:filtr.create_filter(root, check_open, tree_full, "Наименование блюда", "1"))
    tree_full.heading("#2", text="Стоимость", anchor=W, command= lambda:filtr.create_filter(root, check_open, tree_full, "Стоимость", "2"))
    tree_full.heading("#3", text="Размерность", anchor=W, command= lambda:filtr.create_filter(root, check_open, tree_full, "Размерность", "3"))
    tree_full.heading("#4", text="Тип", anchor=W, command= lambda:filtr.create_filter(root, check_open, tree_full, "Тип", "4"))
    tree_full.heading("#5", text="Код заказа", anchor=W, command= lambda:filtr.create_filter(root, check_open, tree_full, "Код заказа", "5"))
    tree_full.heading("#6", text="Дата посещения", anchor=W, command= lambda:filtr.create_filter(root, check_open, tree_full, "Дата посещения", "6"))
    tree_full.heading("#7", text="Время посещения", anchor=W, command= lambda:filtr.create_filter(root, check_open, tree_full, "Время посещения", "7"))
    tree_full.heading("#8", text="Количество порций", anchor=W, command= lambda:filtr.create_filter(root, check_open, tree_full, "Количество порций", "8"))
    tree_full.heading("#9", text="Сумма заказа", anchor=W, command= lambda:filtr.create_filter(root, check_open, tree_full, "Сумма заказа", "9"))

    tree_full.tag_configure("COLOR", background = '#fff8dc')#у каждой четной делай bg
    

def histo(name):
    """
        Автор: Ворожцов Михаил
        Цель: Вызов функции и передача данных для построения гистограммы
        Вход: Название типа данных
        Выход: Нет выходных данных

    """

    if name != "X":
        ch.create_histogram(tree_type, tree_orders, tree_menu, name)
    else:
        messagebox.showinfo("Подсказка", "Пожалуйста, выберите одно из значений в поле X ")

def barchart(name_f, name_t):
    """
        Автор: Ворожцов Михаил
        Цель: Вызов функции и передача данных для построения ступенчатой диаграммы
        Вход: Название типа данных
        Выход: Нет выходных данных

    """
    if name_f != name_t and name_f != "X" and name_t != "Y":
        ch.create_barchart(tree_type, tree_orders, tree_menu,name_f, name_t)
    else:
        messagebox.showinfo("Подсказка", "Пожалуйста, выберите разные значений в поле X и Y")

def box_plot(name):
    """
        Автор: Ворожцов Михаил
        Цель: Вызов функции и передача данных для построения диаграмма размаха
        Вход: Название типа данных
        Выход: Нет выходных данных

    """
    if name != "X":
        ch.create_box_plot(tree_type, tree_orders, tree_menu,name)
    else:
        messagebox.showinfo("Подсказка", "Пожалуйста, выберите одно из значений в поле X ")
def scatter_plot(name_f, name_t):
    """
        Автор: Ворожцов Михаил
        Цель: Вызов функции и передача данных для построения точечной диаграммы
        Вход: Название типа данных
        Выход: Нет выходных данных

    """
    if name_f != name_t and name_f != "X" and name_t != "Y":
        ch.create_scatter_plot(tree_type, tree_orders, tree_menu,name_f, name_t)
    else:
        messagebox.showinfo("Подсказка", "Пожалуйста, выберите разные значений в поле X и Y")

# Добавление типа в treeview (в таблицу типов)
def insert_type_string():
    """
    Автор: Исмаилов Асад
    Цель: Вызов функции и передача данных дерева типов
    Вход: Нет входных данных
    Выход: Нет выходных данных

    """
    prog.insert_type_string_tree(tree_type)

# Добавление блюда в treeview (в таблицу Меню)
def insert_menu_string():
    """
    Автор: Исмаилов Асад
    Цель: Вызов функции и передача данных дерева меню
    Вход: Нет входных данных
    Выход: Нет выходных данных

    """
    prog.insert_menu_string_tree(tree_menu, tree_full)

# Добавление заказа в treeview (в таблицу заказов)
def insert_orders_string():
    """
    Автор: Исмаилов Асад
    Цель: Вызов функции и передача данных дерева заказов
    Вход: Нет выходных данных
    Выход: Нет выходных данных

    """
    prog.insert_orders_string_tree(tree_orders, tree_full)

def delete_all_trees():
    """
    Автор: Исмаилов Асад
    Цель: Очистка treeview
    Вход: Нет входных данных
    Выход: Очищенный treeview

    """
    global tree_type
    global tree_menu
    global tree_orders
    global tree_full
    for i in tree_type.get_children(): 
        tree_type.delete(i)
    for i in tree_menu.get_children(): 
        tree_menu.delete(i)
    for i in tree_orders.get_children(): 
        tree_orders.delete(i)
    for i in tree_full.get_children(): 
        tree_full.delete(i)
    
# Изменение строки
def changing_string(note_tree, string_dish):
    """
    Автор: Исмаилов Асад
    Цель: Изменение выделенной строки и элементов, зависящих от данной строки, как в treeview, так и в Excel
    Вход: note_tree (виджет для управления коллекцией окон и отображения только 1 окна за раз), string_dish (массив из данных новой строки)
    Выход: номер выделенной типа/блюда в таблице Excel
    
    """
    global tree_type
    global tree_menu
    global tree_orders
    global tree_full
    
    print("Current tree is number ", note_tree.index("current"))
    id_tree = note_tree.index("current") # Номер открытой пользователем таблицы [0, 1, 2, 3]
    
    if id_tree == 0: # Если открыта таблица типов
        selected_item = tree_type.selection()[0] # Id выделенной строки "type0", где 0 - номер типа в таблице типов
        values = tree_type.item(selected_item, option="values") # Данные выделенной строки
        tree_type.item(selected_item, values=(string_dish[0]))
        print(values)
        dish_child = tree_menu.get_children()
        for id_dish in range(len(dish_child)):
            item_menu = dish_child[id_dish]
            values_dish = tree_menu.item(item_menu, option="values")
            if int(float(values_dish[3])) == int(selected_item[4:]):
                tree_full.item("full%d"%(int(item_menu[4:])), values=(values_dish[0], values_dish[1], values_dish[2], string_dish[0]))
        return (int(selected_item[4:])-1)
    
    if id_tree == 2: # Если открыта таблица Меню
        selected_item = tree_menu.selection()[0] # Id выделенной строки "menu0", где 0 - номер блюда в таблице Меню
        values = tree_menu.item(selected_item, option="values") # Данные выделенной строки
        price_dish = int(string_dish[1])
        if int(string_dish[1]) != int(values[1]):
            for id_orders in range(len(tree_orders.get_children())):
                values_orders = tree_orders.item("order%d"%(id_orders+1), option="values")
                if int(float(values_orders[2])) == int(selected_item[4:]):
                    tree_orders.item("order%d"%(id_orders+1), values=(values_orders[0], values_orders[1], values_orders[2], values_orders[3], price_dish*int(float(values_orders[3]))))
                    prog.change_order_string_excel([0,values_orders[0], values_orders[1], values_orders[2], values_orders[3], price_dish*int(float(values_orders[3]))], id_orders)
                    k = prog.num_sub(id_orders+1) # Номер данного заказа в полной таблице
                    values_sub = tree_full.item("sub%d%d"%(int(selected_item[4:]), k), option="values")
                    tree_full.item("sub%d%d"%(int(selected_item[4:]), k), values = ('', '', '', '', '', values_sub[5], values_sub[6], values_sub[7], price_dish*int(float(values_orders[3]))))
        tree_menu.item(selected_item, values=(string_dish[0], string_dish[1], string_dish[2], string_dish[3]))
        values_type = tree_type.item("type%d"%(int(string_dish[3])), option="values") # Данные выделенной строки
        tree_full.item("full%d"%(int(selected_item[4:])), values=(string_dish[0], string_dish[1], string_dish[2], values_type[0]))
        print(values)
        return (int(selected_item[4:])-1)

# Удаление строки
def deleting_string(note_tree):
    """
    Автор: Исмаилов Асад
    Цель: Удаление выделенной строки и элементов, зависящих от данной строки, как в treeview, так и в Excel
    Вход: note_tree (виджет для управления коллекцией окон и отображения только 1 окна за раз)
    Выход: Обновленные treeview и Excel (после удаления)
    
    """
    global tree_type
    global tree_menu
    global tree_orders
    global tree_full
    
    print("Current tree is number ", note_tree.index("current"))
    id_tree = note_tree.index("current") # Номер открытой пользователем таблицы [0, 1, 2, 3]
    
    if id_tree == 0: # Если открыта таблица типов
        selected_item = tree_type.selection()[0] # Id выделенной строки "type0", где 0 - номер типа в таблице типов
        values = tree_type.item(selected_item, option="values") # Данные выделенной строки
        print(values)
        tree_type.delete(selected_item) # Удаление строки в treeview (в таблице типов)
        dish_child = tree_menu.get_children()
        for id_dish in range(len(dish_child)-1, -1, -1): # С конца, иначе удаляется через 1 из-за сдвига
            item_menu = dish_child[id_dish]
            values_dish = tree_menu.item(item_menu, option="values")
            if int(float(values_dish[3])) == int(selected_item[4:]):
                print(id_dish)
                tree_menu.delete(item_menu) # Удаление блюда в treeview (в таблице Меню)
                prog.deleting_string(int(id_dish), 2) # Удаление блюда в Excel
                full_child = tree_full.get_children("full%d"%(int(item_menu[4:]))) # "Дети" данного блюда в полной таблице, т.е. подстроки, заказы с этим блюдом
                for id_orders in range(len(full_child)): # id_orders - id заказов с данным блюдом - "subAB", где A - номер блюда в Меню, B - номер заказа среди "детей"
                    tree_orders.delete("order%d"%(int(((tree_full.item(full_child[id_orders], option="values"))[4])[1:]))) # Удаление заказов в treeview (в таблице заказов)
                    prog.deleting_string(int(((tree_full.item(full_child[id_orders], option="values"))[4])[1:])-1, 1) # Удаление заказа в Excel
                tree_full.delete("full%d"%(int(item_menu[4:]))) # Удаление блюда в treeview (в полной таблице с его подстроками)
        print(selected_item)
        prog.deleting_string(int(selected_item[4:])-1, id_tree) # Удаление типа в Excel
    
    if id_tree == 1: # Если открыта таблица заказов
        selected_item = tree_orders.selection()[0] # Id выделенной строки "order0", где 0 - номер заказа в таблице заказов
        values = tree_orders.item(selected_item, option="values") # Данные выделенной строки
        print(values)
        k = prog.num_sub(int(selected_item[5:])) # Номер данного заказа в полной таблице
        tree_full.delete("sub%d%d"%(int(float(values[2])), k)) # Удаление заказа в treeview (в полной таблице)
        tree_orders.delete(selected_item) # Удаление заказа в treeview (в таблице заказов)
        print(selected_item)
        prog.deleting_string(int(selected_item[5:])-1, id_tree) # Удаление заказа в Excel
    
    if id_tree == 2: # Если открыта таблица Меню
        selected_item = tree_menu.selection()[0] # Id выделенной строки "menu0", где 0 - номер блюда в таблице Меню
        values = tree_menu.item(selected_item, option="values") # Данные выделенной строки
        print(values)
        tree_menu.delete(selected_item) # Удаление блюда в treeview (в таблице Меню)
        full_child = tree_full.get_children("full%d"%(int(selected_item[4:]))) # "Дети" данного блюда в полной таблице, т.е. подстроки, заказы с этим блюдом
        print(full_child) # Вывод массива из "детей" блюда
        for id_orders in range(len(full_child)-1, -1, -1): # id_orders - id заказов с данным блюдом - "subAB", где A - номер блюда в Меню, B - номер заказа среди "детей"
            tree_orders.delete("order%d"%(int(((tree_full.item(full_child[id_orders], option="values"))[4])[1:]))) # Удаление заказов в treeview (в таблице заказов)
            prog.deleting_string(int(((tree_full.item(full_child[id_orders], option="values"))[4])[1:])-1, 1) # Удаление заказа в Excel
        tree_full.delete("full%d"%(int(selected_item[4:]))) # Удаление блюда в treeview (в полной таблице с его подстроками)
        print(selected_item)
        prog.deleting_string(int(selected_item[4:])-1, id_tree) # Удаление блюда в Excel
    
    if id_tree == 3: # Если открыта полная таблица
        # Id выделенной строки:
        # "full0", если это блюдо в полной таблице, где 0 - номер блюда в таблице
        # "subAB", если это заказ в полной таблице, где A - номер блюда в таблице, B - номер заказа среди "детей" блюда6
        selected_item = tree_full.selection()[0]
        values = tree_full.item(selected_item, option="values") # Данные выделенной строки
        print(values)
        if selected_item[0] == 'f': # Если это блюдо ("full0"[0] = 'f')
            full_child = tree_full.get_children(selected_item) # "Дети" данного блюда в полной таблице, т.е. подстроки, заказы с этим блюдом
            print(full_child) # Вывод массива из "детей" блюда
            for id_orders in range(len(full_child)-1, -1, -1): # id_orders - id заказов с данным блюдом - "subAB", где A - номер блюда в Меню, B - номер заказа среди "детей"
                tree_orders.delete("order%d"%(int(((tree_full.item(full_child[id_orders], option="values"))[4])[1:]))) # Удаление заказов в treeview (в таблице заказов)
                prog.deleting_string(int(((tree_full.item(full_child[id_orders], option="values"))[4])[1:])-1, 1) # Удаление заказа в Excel
            tree_menu.delete("menu%d"%(int(selected_item[4:]))) # Удаление блюда в treeview (в таблице Меню)
            prog.deleting_string(int(selected_item[4:])-1, 2) # Удаление блюда в Excel
        elif selected_item[0] == 's': # Если это заказ ("subAB"[0] = 's')
            tree_orders.delete("order%d"%(int((values[4])[1:]))) # Удаление заказа в treeview (в таблице заказов)
            full_child = tree_full.get_children("full%d"%(int(selected_item[3:-1]))) # "Дети" данного блюда в полной таблице, т.е. подстроки, заказы с этим блюдом
            prog.deleting_string(int(((tree_full.item(full_child[int(selected_item[-1])-1], option="values"))[4])[1:])-1, 1) # Удаление заказа в Excel
        tree_full.delete(selected_item) # Удаление строки в treeview (в полной таблице)
        print(selected_item)

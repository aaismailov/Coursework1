# -*- coding: utf-8 -*-
"""
Created on Sun May  3 18:42:09 2020

@author: Асад
"""
from random import *
import Scripts.default as default
import Scripts.Customize as custom
from tkinter import *
import os
from tkinter import messagebox
from ttkthemes import ThemedStyle
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox as mb
import datetime
import time
from tkinter import Menu
from PIL import Image, ImageTk
import Datas2 as prog
import Trees2 as trees
import Filter as filtr
import Filter_functions as ff
string_dish = []

def create_background(root):
    """
        Автор: Ворожцов Михаил
        Цель: Создает фон основного окна
        Вход: -
        Выход: -

    """
    global lb
    global img_photo


    Library = os.getcwd()
    img_name = default.way

    os.chdir(img_name)
    img = Image.open(default.name_back)
    os.chdir(Library)

    img_photo = ImageTk.PhotoImage(img)
    lb = Label(root, image=img_photo)
    lb.place(x=0, y=0)

def create_buttons():
    """
            Автор: Ворожцов Михаил
            Цель: Создает кнопки в note
            Вход: -
            Выход:

    """
    global style_all
    #Таблица
    but_new_table = ttk.Button(f_table,text = "Открыть", width = 9, command=open_table)
    but_new_table.place(x = 10, y = 17)
    
    but_save = ttk.Button(f_table,text = "Сохранить", width = 9, command=save_table)
    but_save.place(x = 130, y= 17)
    
    but_excp = ttk.Button(f_table,text = "Экспорт", width = 9, command=export_table)
    but_excp.place(x = 250, y= 17)

    but_del_table = ttk.Button(f_table,text = "Удалить", width = 9, command=del_tree)
    but_del_table.place(x = 370, y= 17)

    but_сustomize = ttk.Button(f_table, text="Кастомизация", width=13, command = lambda : custom.create_menu_castom(style_all, lb, root))
    but_сustomize.place(x=490, y=17)



    #Изменить
    but_add_type = ttk.Button(f_insert, text= "Добавить тип", width=16, command=entry_type)
    but_add_type.place(x=10, y=17)
    
    but_add = ttk.Button(f_insert, text= "Добавить блюдо", width=16, command=entry_dish)
    but_add.place(x=185, y=17)
    
    but_add_orders = ttk.Button(f_insert, text= "Добавить заказ", width=16, command=entry_orders)
    but_add_orders.place(x=360, y=17)
    
    but_change = ttk.Button(f_insert, text= "Изменить строчку", width=16, command=change_str)
    but_change.place(x = 535, y= 17)
    
    but_del_row = ttk.Button(f_insert, text= "Удалить строчку", width=16, command=delete_str)
    but_del_row.place(x = 710, y= 17)

    #Анализ
    combo_val_f = ["X","Дата посещения", "Время посещения","Код блюда", "Количество порций", "Сумма заказа",\
                    "Стоимость", "Размерность", "Тип блюда"]

    combo_val_t = ["Y","Дата посещения", "Время посещения","Код блюда", "Количество порций", "Сумма заказа",\
                    "Стоимость", "Размерность", "Тип блюда"]

    combo_1 = ttk.Combobox(f_analysis, width = 25)
    combo_1["values"] = combo_val_f
    combo_1.current(0)
    combo_1.place(x=10, y=5)

    combo_2 = ttk.Combobox(f_analysis, width = 25)
    combo_2["values"] = combo_val_t
    combo_2.current(0)
    combo_2.place(x=10, y=40, height = 25)

    but_histo = ttk.Button(f_analysis, text="Гистограмма", width=21, command=lambda: trees.histo(combo_1.get()))
    but_histo.place(x=210, y=17)

    but_barchart = ttk.Button(f_analysis, text="Ступенчатая диаграмма", width=21, command=lambda: trees.barchart(combo_1.get(), combo_2.get()))
    but_barchart.place(x=430, y=17)

    but_box = ttk.Button(f_analysis, text="Диаграмма размаха", width=21, command=lambda: trees.box_plot(combo_1.get()))
    but_box.place(x=650, y=17)

    but_scatter= ttk.Button(f_analysis, text="Точечная диаграмма", width=21, command=lambda: trees.scatter_plot(combo_1.get(), combo_2.get()))
    but_scatter.place(x = 870, y= 17)


#Деревья
def create_tree():
    """
    Автор: Ворожцов Михаил
    Цель: Вызывает функции создания tree в note_tree
    Вход: -
    Выход: -

    """
    trees.create_tree_type(f_type, root)
    trees.create_tree_orders(f_orders,root)
    trees.create_tree_menu(f_menu,root)
    trees.create_tree_full(f_full,root)

def del_tree():
    """
    Автор: Исмаилов Асад
    Цель: Вызывается кнопкой "Удалить", очищает существующий treeview
    Вход: Нет входных данных
    Выход: Пустой treeview
    
    """
    trees.delete_all_trees()

# Кнопка "Изменить строку"
def change_str():
    """
    Автор: Исмаилов Асад
    Цель: Вызывается кнопкой "Изменить строчку", создает окно для ввода данных для изменения строки
    или окно с предупреждением, если невозможно изменить строку, вызывает функции для изменения строки в treeview и Excel
    Вход: Нет входных данных
    Выход: Обновленные данные в Excel и treeview
    
    """
    global note_tree
    string_dish = [] # Массив из данных, которые ввел пользователь
    id_tree = note_tree.index("current") # Номер открытой пользователем таблицы [0, 1, 2, 3]
    if id_tree == 0:
        def clear(event):
            name_entry.delete(0, END)
        def dest_type(event):
            print(name_entry.get())
            string_dish.append(name_entry.get())
            index_type = trees.changing_string(note_tree, string_dish)
            prog.change_type_string_excel(string_dish, index_type) # Ввод типа в таблицу Excel
            print("KILL")
            ins_enter.destroy() # Удаление окна
    
        ins_enter = Tk() # Окошко для ввода данных пользователем
        ins_enter.title("Изменить тип")
        
        name = StringVar() # Название типа
        name_label = Label(ins_enter, text="Название типа:")
        name_label.grid(row=0, column=0, sticky="w")
        name_entry = Entry(ins_enter, textvariable=name)
        name_entry.grid(row=0,column=1, padx=5, pady=5)
        
        clear_button = Button(ins_enter, text="Очистить поле")
        clear_button.grid(row=1,column=0, padx=5, pady=5, sticky="e")
        clear_button.bind("<Button-1>", clear)
        
        message_button = Button(ins_enter, text="Click Me")
        message_button.grid(row=1,column=1, padx=5, pady=5, sticky="e")
        message_button.bind("<Button-1>", dest_type)
        ins_enter.mainloop()
        string_dish = []
    if id_tree == 1:
        mb.showwarning("Предупреждение", "Нельзя изменить заказ, \nпотому что заказы константные величины.")
    if id_tree == 2:
        def clear(event):
            name_entry.delete(0, END)
            price_entry.delete(0, END)
            size_entry.delete(0, END)
            size_entry.insert(0, '1\\')
            typed_entry.delete(0, END)
        def dest_dish(event):
                print(name_entry.get())
                string_dish.append(name_entry.get())
                string_dish.append(price_entry.get())
                string_dish.append(size_entry.get())
                string_dish.append(typed_entry.get())
                print(string_dish)
                index_dish = trees.changing_string(note_tree, string_dish)
                prog.change_dish_string_excel(string_dish, index_dish) # Ввод типа в таблицу Excel
                print("KILL")
                ins_enter.destroy() # Удаление окна
        def data_format_price(event):
            if not (price_entry.get()).isdigit() and len(price_entry.get()) > 0:
                mb.showerror('Ошибка', 'Неверный ввод данных\nПовторите ввод')
                price_entry.delete(0, END)
        def data_format_size(event):
            if len(size_entry.get()) == 0:
                size_entry.insert(0, '1\\')
            if len(size_entry.get()) == 1:
                size_entry.insert(1, '\\')
            if not (size_entry.get())[2:].isdigit() and len((size_entry.get())[2:]) > 0:
                mb.showerror('Ошибка', 'Неверный ввод данных\nПовторите ввод')
                size_entry.delete(2, END)
        def data_format_type(event):
            if not (typed_entry.get()).isdigit() and len(typed_entry.get()) > 0:
                mb.showerror('Ошибка', 'Неверный ввод данных\nПовторите ввод')
                typed_entry.delete(0, END)
        ins_enter = Tk() # Окошко для ввода данных пользователем
        ins_enter.title("Изменить блюдо")
        
        name = StringVar() # Название блюда
        price = IntVar() # Стоимость
        size = StringVar() # Размер порции, гр
        typed = IntVar() # Тип блюда
        
        name_label = Label(ins_enter, text="Название блюда:")
        price_label = Label(ins_enter, text="Стоимость:")
        size_label = Label(ins_enter, text="Размер порции, гр:")
        typed_label = Label(ins_enter, text="Тип:")
        name_label.grid(row=0, column=0, sticky="w")
        price_label.grid(row=1, column=0, sticky="w")
        size_label.grid(row=2, column=0, sticky="w")
        typed_label.grid(row=3, column=0, sticky="w")
        
        name_entry = Entry(ins_enter, textvariable=name)
        price_entry = Entry(ins_enter, textvariable=price)
        price_entry.bind('<KeyRelease>', data_format_price)
        size_entry = Entry(ins_enter, textvariable=size)
        size_entry.insert(0, '1\\')
        size_entry.bind('<KeyRelease>', data_format_size)
        typed_entry = Entry(ins_enter, textvariable=typed)
        typed_entry.bind('<KeyRelease>', data_format_type)
        
        name_entry.grid(row=0,column=1, padx=5, pady=5)
        price_entry.grid(row=1,column=1, padx=5, pady=5)
        size_entry.grid(row=2,column=1, padx=5, pady=5)
        typed_entry.grid(row=3,column=1, padx=5, pady=5)
        
        clear_button = Button(ins_enter, text="Очистить поля")
        clear_button.grid(row=4,column=0, padx=5, pady=5, sticky="e")
        clear_button.bind("<Button-1>", clear)
        
        message_button = Button(ins_enter, text="Click Me")
        message_button.grid(row=4,column=1, padx=5, pady=5, sticky="e")
        message_button.bind("<Button-1>", dest_dish)
        ins_enter.mainloop()
        
        string_dish = []
    if id_tree == 3:
        mb.showwarning("Предупреждение", "Нельзя изменить строку в полной таблице, \nчтобы поддерживать трехнормированную форму")
        # showerror(), showinfo() и showwarning()

# Кнопка "Удалить строку"
def delete_str():
    """
    Автор: Исмаилов Асад
    Цель: Вызывается кнопкой "Удалить строку", удаляет данные выделенной строки и зависящих от нее строк из treeview и Excel
    Вход: Нет входных данных
    Выход: Нет выходных данных
    
    """
    global note_tree
    trees.deleting_string(note_tree)

# Открыть таблицу Excel
def open_table():
    """
    Автор: Исмаилов Асад, Гамидов Шамсудин
    Цель: Вызывается кнопкой "Открыть", открытие вводимой пользователем таблицы и вывод ее данных в treeview
    Вход: Нет входных данных
    Выход: Обновленный treeview
    
    """
    file_name = filedialog.askopenfilename() # Получение директории папки с данными
    print(file_name)
    prog.open_table_name(file_name)
    trees.open_tables()
    
def save_table():
    """
    Автор: Исмаилов Асад, Гамидов Шамсудин
    Цель: Вызывается кнопкой "Сохранить", сохранение данных treeview (в исходный файл)
    Вход: Нет входных данных
    Выход: Обновленные данные исходного файла
    
    """
    prog.save_table_name()

# Экспорт таблицы в Excel
def export_table():
    """
    Автор: Исмаилов Асад, Гамидов Шамсудин
    Цель: Вызывается кнопкой "Экспорт", экспорт данных treeview (директорию выбирает пользователь)
    Вход: Нет входных данных
    Выход: Файл с данными с treeview
    
    """
    fname = filedialog.asksaveasfilename(filetypes=[("Excel files","*.xlsx")]) # Получение директории папки, куда сохранять
    print(fname)
    prog.export_table_name(fname)

# Кнопка "Добавить тип"
def entry_type():
    """
    Автор: Исмаилов Асад
    Цель: Вызывается кнопкой "Добавить тип", вызывает окно для ввода данных нового типа пользователем,
    создание нового типа в Excel и treeview
    Вход: Нет входных данных
    Выход: Новый тип
    
    """
    string_dish = [] # Массив из данных, которые ввел пользователь
    def clear(event):
        name_entry.delete(0, END)
    
    def dest(event):
        print(name_entry.get())
        string_dish.append(name_entry.get())
        prog.insert_type_string_excel(string_dish) # Ввод типа в таблицу Excel
        trees.insert_type_string() # Вывод типа в treeview (в типы и в полную таблицы)
        print("KILL")
        ins_enter.destroy() # Удаление окна

    ins_enter = Tk() # Окошко для ввода данных пользователем
    ins_enter.title("Добавить тип")
    
    name = StringVar() # Название типа
    name_label = Label(ins_enter, text="Название типа:")
    name_label.grid(row=0, column=0, sticky="w")
    name_entry = Entry(ins_enter, textvariable=name)
    name_entry.grid(row=0,column=1, padx=5, pady=5)
    
    message_button = Button(ins_enter, text="Click Me")
    message_button.grid(row=1,column=1, padx=5, pady=5, sticky="e")
    message_button.bind("<Button-1>", dest)
    
    clear_button = Button(ins_enter, text="Очистить поле")
    clear_button.grid(row=1,column=0, padx=5, pady=5, sticky="e")
    clear_button.bind("<Button-1>", clear)
    
    ins_enter.mainloop()
    string_dish = []


# Кнопка "Добавить блюдо"
def entry_dish():
    """
    Автор: Исмаилов Асад
    Цель: Вызывается кнопкой "Добавить блюдо", вызывает окно для ввода данных нового блюда пользователем,
    создание нового блюда в Excel и treeview
    Вход: Нет входных данных
    Выход: Новое блюдо
    
    """
    string_dish = [] # Массив из данных, которые ввел пользователь
    def clear(event):
        name_entry.delete(0, END)
        price_entry.delete(0, END)
        size_entry.delete(0, END)
        size_entry.insert(0, '1\\')
        typed_entry.delete(0, END)
    def dest(event):
        print(name_entry.get())
        string_dish.append(name_entry.get())
        string_dish.append(price_entry.get())
        string_dish.append(size_entry.get())
        string_dish.append(typed_entry.get())
        print(string_dish)
        prog.insert_menu_string_excel(string_dish) # Ввод блюда в таблицу Excel
        trees.insert_menu_string() # Вывод блюда в treeview (в Меню и в полную таблицы)
        print("KILL")
        ins_enter.destroy() # Удаление окна
    def data_format_price(event):
        if not (price_entry.get()).isdigit() and len(price_entry.get()) > 0:
            mb.showerror('Ошибка', 'Неверный ввод данных\nПовторите ввод')
            price_entry.delete(0, END)
    def data_format_size(event):
        if len(size_entry.get()) == 0:
            size_entry.insert(0, '1\\')
        if len(size_entry.get()) == 1:
            size_entry.insert(1, '\\')
        if not (size_entry.get())[2:].isdigit() and len((size_entry.get())[2:]) > 0:
            mb.showerror('Ошибка', 'Неверный ввод данных\nПовторите ввод')
            size_entry.delete(2, END)
    def data_format_type(event):
        if not (typed_entry.get()).isdigit() and len(typed_entry.get()) > 0:
            mb.showerror('Ошибка', 'Неверный ввод данных\nПовторите ввод')
            typed_entry.delete(0, END)
    ins_enter = Tk() # Окошко для ввода данных пользователем
    ins_enter.title("Добавить блюдо")
    
    name = StringVar() # Название блюда
    price = IntVar() # Стоимость
    size = StringVar() # Размер порции, гр
    typed = IntVar() # Тип блюда
    
    name_label = Label(ins_enter, text="Название блюда:")
    price_label = Label(ins_enter, text="Стоимость:")
    size_label = Label(ins_enter, text="Размер порции, гр:")
    typed_label = Label(ins_enter, text="Тип:")
    name_label.grid(row=0, column=0, sticky="w")
    price_label.grid(row=1, column=0, sticky="w")
    size_label.grid(row=2, column=0, sticky="w")
    typed_label.grid(row=3, column=0, sticky="w")
    
    name_entry = Entry(ins_enter, textvariable=name)
    price_entry = Entry(ins_enter, textvariable=price)
    price_entry.bind('<KeyRelease>', data_format_price)
    size_entry = Entry(ins_enter, textvariable=size)
    size_entry.insert(0, '1\\')
    size_entry.bind('<KeyRelease>', data_format_size)
    typed_entry = Entry(ins_enter, textvariable=typed)
    typed_entry.bind('<KeyRelease>', data_format_type)
    
    name_entry.grid(row=0,column=1, padx=5, pady=5)
    price_entry.grid(row=1,column=1, padx=5, pady=5)
    size_entry.grid(row=2,column=1, padx=5, pady=5)
    typed_entry.grid(row=3,column=1, padx=5, pady=5)
    
    message_button = Button(ins_enter, text="Click Me")
    message_button.grid(row=4,column=1, padx=5, pady=5, sticky="e")
    message_button.bind("<Button-1>", dest)
    
    clear_button = Button(ins_enter, text="Очистить поля")
    clear_button.grid(row=4,column=0, padx=5, pady=5, sticky="e")
    clear_button.bind("<Button-1>", clear)
    
    ins_enter.mainloop()
    string_dish = []

# Кнопка "Добавить заказ"
def entry_orders():
    """
    Автор: Исмаилов Асад
    Цель: Вызывается кнопкой "Добавить заказ", вызывает окно для ввода данных нового заказа пользователем,
    создание нового заказа в Excel и treeview
    Вход: Нет входных данных
    Выход: Новый заказ
    
    """
    string_dish = [] # Массив из данных, которые ввел пользователь
    def clear(event):
        data_entry.delete(0, END)
        time_entry.delete(0, END)
        code_dish_entry.delete(0, END)
        kolvo_entry.delete(0, END)
    def dest(event):
        string_dish.append(0)
        string_dish.append(data_entry.get())
        string_dish.append(time_entry.get())
        string_dish.append(code_dish_entry.get())
        string_dish.append(kolvo_entry.get())

        print(string_dish)
        prog.insert_orders_string_excel(string_dish) # Ввод заказа в таблицу Excel
        trees.insert_orders_string() # Вывод заказа в treeview (в Заказы и в полную таблицу под блюдо из заказа)
        print("KILL")
        ins_enter.destroy() # Удаление окна
    def foo(s):
        try:
            s = str(datetime.datetime.strptime(s, '%d.%m.%Y'))
            stoday = str(datetime.datetime.today())
            if int(s[:4]) == int(stoday[:4]):
                if int(s[5:7]) == int(stoday[5:7]):
                    if int(s[8:10]) <= int(stoday[8:10]):
                        return True
                    else:
                        return False
                if int(s[5:7]) > int(stoday[5:7]):
                    return False
                if int(s[5:7]) < int(stoday[5:7]):
                    return True
            elif int(s[:4]) > int(stoday[:4]):
                return False
            elif int(s[:4]) < int(stoday[:4]):
                return True
        except:
            return False
    def data_format(event):
        if len(data_entry.get()) is 2:
            data_entry.insert(END,".")
        elif len(data_entry.get()) is 5:
            data_entry.insert(END,".")
        elif len(data_entry.get()) is 11:
            data_entry.delete(10, END)
        if not foo(data_entry.get()) and (len(data_entry.get()) is 10):
            mb.showerror('Ошибка', 'Неверный ввод данных\nПовторите ввод')
            data_entry.delete(0, END)
    def foo_time(s):
        try:
            s = str(datetime.time(int(s[:2]), int(s[3:5])))
            print(s)
            return True
        except:
            return False
    def data_format_time(event):
        if len(time_entry.get()) is 2:
            time_entry.insert(END,":")
        elif len(time_entry.get()) is 6:
            time_entry.delete(5, END)
        if not foo_time(time_entry.get()) and (len(time_entry.get()) is 5):
            mb.showerror('Ошибка', 'Неверный ввод данных\nПовторите ввод')
            time_entry.delete(0, END)
    def data_format_code_dish(event):
        if not (code_dish_entry.get()).isdigit() and len(code_dish_entry.get()) > 0:
            mb.showerror('Ошибка', 'Неверный ввод данных\nПовторите ввод')
            code_dish_entry.delete(0, END)
    def data_format_kolvo(event):
        if not (kolvo_entry.get()).isdigit() and len(kolvo_entry.get()) > 0:
            mb.showerror('Ошибка', 'Неверный ввод данных\nПовторите ввод')
            kolvo_entry.delete(0, END)
    ins_enter = Tk() # Окошко для ввода данных пользователем
    ins_enter.title("Добавить заказ")
    
    data = StringVar() # Дата посещения
    time = StringVar() # Время посещения
    code_dish = IntVar() # Код блюда
    kolvo = IntVar() # Кол-во порций
    
    data_label = Label(ins_enter, text="Дата посещения:")
    time_label = Label(ins_enter, text="Время посещения:")
    code_dish_label = Label(ins_enter, text="Код блюда:")
    kolvo_label = Label(ins_enter, text="Кол-во порций:")

    data_label.grid(row=0, column=0, sticky="w")
    time_label.grid(row=1, column=0, sticky="w")
    code_dish_label.grid(row=2, column=0, sticky="w")
    kolvo_label.grid(row=3, column=0, sticky="w")
    
    data_entry = Entry(ins_enter, textvariable=data)
    time_entry = Entry(ins_enter, textvariable=time)
    code_dish_entry = Entry(ins_enter, textvariable=code_dish)
    kolvo_entry = Entry(ins_enter, textvariable=kolvo)
    
    data_entry.grid(row=0,column=1, padx=5, pady=5)
    time_entry.grid(row=1,column=1, padx=5, pady=5)
    code_dish_entry.grid(row=2,column=1, padx=5, pady=5)
    kolvo_entry.grid(row=3,column=1, padx=5, pady=5)
    data_entry.bind('<KeyRelease>', data_format)
    time_entry.bind('<KeyRelease>', data_format_time)
    code_dish_entry.bind('<KeyRelease>', data_format_code_dish)
    kolvo_entry.bind('<KeyRelease>', data_format_kolvo)
    
    message_button = Button(ins_enter, text="Click Me")
    message_button.grid(row=5,column=1, padx=5, pady=5, sticky="e")
    message_button.bind("<Button-1>", dest)
    
    clear_button = Button(ins_enter, text="Очистить поля")
    clear_button.grid(row=5,column=0, padx=5, pady=5, sticky="e")
    clear_button.bind("<Button-1>", clear)
    
    ins_enter.mainloop()
    string_dish = []

def create_style():
    """
    Автор: Ворожцов Михаил
    Цель: Создает style для вилджетов
    Вход: -
    Выход: -

    """
    global style_all
   #Инициализируем стиль
    style_all = ThemedStyle(root)
    style_all.set_theme(default.style)
    # Для конкретных виджетов
    style = ttk.Style()
    style.configure("style.Treeview", highlightthickness=10, bd=0, font=('Calibri', 8))
    style.configure("style.Treeview.Heading", font=('Calibri', 13))
    style.configure('style.TNotebook', tabposition='nw')


def create_note_frame(root):
    """
    Автор: Ворожцов Михаил
    Цель: Создает note, note_tree и Frame'ы для них. Биндим Button-1, если пользователь меняет frame
    Вход: -
    Выход: Глобальные переменные(f_table,f_insert,f_analysis,f_full,f_type,f_orders,f_menu,f_main)

    """
    #Заголовок
    global f_table
    global f_insert
    global f_analysis

    #Таблицы
    global f_full
    global f_type
    global f_orders
    global f_menu
    global f_main
    global note_tree

    note = ttk.Notebook(root, style='style.TNotebook', width = 1270)
    note_tree = ttk.Notebook(root, style='style.TNotebook', height = 350, width = 1270)

    #Рамки
    #Под заголовок
    f_table = Frame(note, width=750, height=80)
    f_insert = Frame(note, width=750, height=80)
    f_analysis  = Frame(note, width=750, height=80)


    #Таблицы
    f_full = Frame(note_tree, width = 1310, height=350)
    f_type = Frame(note_tree, width = 1310, height=350)
    f_orders = Frame(note_tree, width = 1310, height=350)
    f_menu = Frame(note_tree, width = 1310, height=350)


    #Добавляем
    note.add(f_table, text = "Таблица")
    note.add(f_insert, text = "Изменить")
    note.add(f_analysis, text= "Анализ")
    #note.place(x=10, y=10)
    note.grid(row = 0, column = 0, pady = 5, padx = 5, sticky = N)

    note_tree.add(f_type, text="Тип блюда")
    note_tree.add(f_orders, text="Заказы")
    note_tree.add(f_menu, text="Меню")
    note_tree.add(f_full, text = "Полная таблица")
    #note_tree.place(x=10, y=125)
    note_tree.grid(row=1, column=0, pady = 5, padx = 5, sticky = N)
    note_tree.select(f_type)

    note_tree.bind('<ButtonRelease-1>', lambda event,note_tree = note_tree: ff.change_note_frame(event,note_tree))


def main_loop():
    """
    Автор: Ворожцов Михаил
    Цель: Вызывает функции для отрисовки приложения. Делаем loop.
    Вход:-
    Выход:Глобальные переменные(root,check_open)

    """
    #создание гланого окна
    global root
    #Для открытия/закрытия фильтра
    global check_open
    check_open = False

    root = Tk()
    root.title("База данных Столовой")
    root.geometry("1285x515+130+120")

    #Создаем style
    create_style()

    #Создаем фон
    create_background(root)

    #Создаем note и frame
    create_note_frame(root)

    #Создаем кнопки
    create_buttons()

    #Создаем Tree
    create_tree()

    root.mainloop()

# main_loop()

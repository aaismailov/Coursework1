# -*- coding: utf-8 -*-
"""
Created on Sun May  3 19:37:37 2020

@author: Асад
"""

import xlwings as xw
import pandas as pd

def open_table_name(file_name):
    """
    Автор: Исмаилов Асад
    Цель: Чтение данных из файла в соответсвующие датафреймы, создание датафреймов для полной таблицы
    Вход: Название файла Excel file_name
    Выход: Обновленные глобальные переменные
    
    """
    global wb
    global data_pd_type # Датафрейм типов блюд
    global data_pd_orders # Датафрейм заказов
    global data_pd_menu # Датафрейм блюд
    global data_pd_full # Датафрейм полной таблицы без заказов
    global data_pd_full_sub # Датафрейм полной таблицы с заказами
    
    global data_excel_type
    global data_excel_orders
    global data_excel_menu
    global file_name_global
    wb=xw.Book(file_name) # Открываем книгу
    file_name_global = file_name
    
    # import pandas as pd
    # import xlwings as xw
    # wb=xw.Book('C:\\Anaconda\\Project_python\\Library\\Menyu_stolovoy.xlsx') # Открываем книгу
    
    data_excel_type = wb.sheets['Тип блюда'] # Читаем лист Тип блюда
    data_excel_orders = wb.sheets['Заказы'] # Читаем лист Заказы
    data_excel_menu = wb.sheets['Меню'] # Читаем лист Меню
    
    # Чтение типов из Excel
    data_pd_type = data_excel_type.range('A1:B9').options(pd.DataFrame, header = 1, index = False).value
    print(data_pd_type)
    
    # Чтение заказов из Excel
    data_pd_orders = data_excel_orders.range('A1:F23').options(pd.DataFrame, header = 1, index = False).value
    print(data_pd_orders)
    
    # Чтение блюд из Excel
    data_pd_menu = data_excel_menu.range('A1:E82').options(pd.DataFrame, header = 1, index = False).value
    print(data_pd_menu)
    
    # Создание датафрейма полной таблицы
    data_pd_full = pd.merge(data_pd_menu, data_pd_type, how='inner', left_on='Тип блюда', right_on='Тип блюда') # Объединение меню с типами
    data_pd_full.drop(['Тип блюда'], axis=1, inplace=True) # Удаление лишнего столбца 'Тип блюда' (один из таблицы блюд, второй из таблицы типы блюд)
    data_pd_full.rename(columns={'Название': 'Тип блюда'}, inplace=True) # Переименование столбца 'Название' из таблицы типов в 'Тип блюда'
    data_pd_full_sub = pd.merge(data_pd_full, data_pd_orders, how='inner', left_on='Код блюда', right_on='Код блюда') # Объединение таблицы с блюдами и типами еще и с заказами


def save_table_name():
    """
    Автор: Исмаилов Асад
    Цель: Сохранение данных датафреймов в исходный файл
    Вход: Нет входных данныъ
    Выход: Обновленные данные исходного файла
    
    """
    # wn = xw.Book(file_name_global)
    
    # save_excel_type = wn.sheets['Тип блюда'] # Читаем лист Тип блюда
    # save_excel_orders = wn.sheets['Заказы'] # Читаем лист Заказы
    # save_excel_menu = wn.sheets['Меню'] # Читаем лист Меню
    
    # save_excel_type.clear_contents()
    # save_excel_orders.clear_contents()
    # save_excel_menu.clear_contents()
    
    data_excel_type.range('A1').options(index = False).value = data_pd_type
    data_excel_orders.range('A1').options(index = False).value = data_pd_orders
    data_excel_menu.range('A1').options(index = False).value = data_pd_menu
    
    data_excel_type.autofit()
    data_excel_orders.autofit()
    data_excel_menu.autofit()
    
    wb.save() # Сохранение файла в данной директории
    
# Создание файла в директории fname и запись данных в него с сохранением
def export_table_name(fname):
    """
    Автор: Исмаилов Асад
    Цель: Сохранение данных датафреймов в выбранный файл (можно создать новый файл)
    Вход: Название файла Excel fname
    Выход: Передача данных датафреймов в файл
    
    """
    new_wb=xw.Book() # Создание нового .xlsx файла
    data_excel_type.api.Copy(Before=new_wb.sheets['Лист1'].api)
    data_excel_orders.api.Copy(Before=new_wb.sheets['Лист1'].api)
    data_excel_menu.api.Copy(Before=new_wb.sheets['Лист1'].api)    
    new_wb.save(fname) # Сохранение файла в данной директории

# Вывод таблицы Тип блюда в treeview
def insert_type(tree):
    """
    Автор: Исмаилов Асад
    Цель: Вывод таблицы "Типы блюда" в treeview
    Вход: Дерево типов tree
    Выход: Обновленное дерево типов
    
    """
    global data_pd_type
    for i in range(len(data_pd_type)):
        if (i % 2 == 0):
            tree.insert("", i, "type%d"%(i+1), text ="%d" % (i+1), values=(data_pd_type['Название'].values[i], ''), tag = "COLOR")
        else:
            tree.insert("", i, "type%d"%(i+1), text ="%d" % (i+1), values=(data_pd_type['Название'].values[i], ''))
    
    tree.tag_configure("COLOR", background = '#fff8dc')#у каждой четной делай bg

# Вывод таблицы Заказы в treeview
def insert_orders(tree):
    """
    Автор: Исмаилов Асад
    Цель: Вывод таблицы "Заказы" в treeview
    Вход: Дерево заказов tree
    Выход: Обновленное дерево заказов
    
    """
    global data_pd_orders
    for i in range(len(data_pd_orders)):
        if (i % 2 == 0):
            tree.insert("", i, "order%d"%(i+1), text ="%d" % (i+1), values=(data_pd_orders['Дата посещения'].values[i], data_pd_orders['Время посещения'].values[i], int(data_pd_orders['Код блюда'].values[i]), int(data_pd_orders['Количество порций'].values[i]), int(data_pd_orders['Сумма'].values[i])), tag = "COLOR")
        else:
            tree.insert("", i, "order%d"%(i+1), text ="%d" % (i+1), values=(data_pd_orders['Дата посещения'].values[i], data_pd_orders['Время посещения'].values[i], int(data_pd_orders['Код блюда'].values[i]), int(data_pd_orders['Количество порций'].values[i]), int(data_pd_orders['Сумма'].values[i])))

    tree.tag_configure("COLOR", background = '#fff8dc')#у каждой четной делай bg

# Вывод таблицы Меню в treeview
def insert_menu(tree):
    """
    Автор: Исмаилов Асад
    Цель: Вывод таблицы "Меню" в treeview
    Вход: Дерево блюд tree
    Выход: Обновленное дерево "Меню"
    
    """
    global data_pd_menu
    for i in range(len(data_pd_menu)):
        if (i % 2 == 0):
            tree.insert("", i, "menu%d"%(i+1), text ="%d" % (i+1), values=(data_pd_menu['Наименование блюда'].values[i], int(data_pd_menu['Стоимость'].values[i]), data_pd_menu['Размерность'].values[i], int(data_pd_menu['Тип блюда'].values[i])), tag = "COLOR")
        else:
            tree.insert("", i, "menu%d"%(i+1), text ="%d" % (i+1), values=(data_pd_menu['Наименование блюда'].values[i], int(data_pd_menu['Стоимость'].values[i]), data_pd_menu['Размерность'].values[i], int(data_pd_menu['Тип блюда'].values[i])))

    tree.tag_configure("COLOR", background = '#fff8dc')#у каждой четной делай bg

# Вывод таблицы Меню в treeview
def insert_full(tree):
    """
    Автор: Исмаилов Асад
    Цель: Вывод полной таблицы в treeview
    Вход: Дерево полной таблицы tree
    Выход: Обновленное дерево полной таблицы
    
    """
    global data_pd_full
    global data_pd_full_sub
    for i in range(len(data_pd_full)):
        if(i % 2 == 0):
            folder = tree.insert("", i, "full%d"%(i+1), text ="%d" % (i+1), values=(data_pd_full['Наименование блюда'].values[i], int(data_pd_full['Стоимость'].values[i]), data_pd_full['Размерность'].values[i], data_pd_full['Тип блюда'].values[i]), tag = "COLOR")
        else:
            folder = tree.insert("", i, "full%d"%(i+1), text ="%d" % (i+1), values=(data_pd_full['Наименование блюда'].values[i], int(data_pd_full['Стоимость'].values[i]), data_pd_full['Размерность'].values[i], data_pd_full['Тип блюда'].values[i]))
        k = 0 # Заказ k: Заказ 1, Заказ 2,...
        for j in range(len(data_pd_full_sub)):
            if (i+1)==data_pd_full_sub['Код блюда'].values[j]:
                k += 1
                tree.insert(folder, "end", "sub%d%d"%(i+1, k), text="Заказ %d"%k, values= ( "","","","", data_pd_full_sub['Код заказа'].values[j], data_pd_full_sub['Дата посещения'].values[j], data_pd_full_sub['Время посещения'].values[j], int(data_pd_full_sub['Количество порций'].values[j]), int(data_pd_full_sub['Сумма'].values[j])))
    
    tree.tag_configure("COLOR", background = '#fff8dc')#у каждой четной делай bg


# Добавление типа в Excel в страницу "Типы блюд"
def insert_type_string_excel(string_dish):
    """
    Автор: Исмаилов Асад
    Цель: Добавление нового типа блюда в датафрейм и Excel
    Вход: string_dish (данные новой строки)
    Выход: Обновленная таблица типов
    
    """
    global data_pd_type
    data_pd_type = data_pd_type.append({'Тип блюда':len(data_pd_type)+1, 'Название':string_dish[0]}, ignore_index=True)
    data_excel_type.range('A1').options(index = False).value = data_pd_type
    print(data_pd_type)
    print(string_dish)

# Добавление типа в treeview (в таблицу типов)
def insert_type_string_tree(tree_type):
    """
    Автор: Исмаилов Асад
    Цель: Чтение данных нового типа из датафрейма и вывод в treeview
    Вход: tree_type (дерево типов)
    Выход: Обновленное дерево типов
    
    """
    global data_pd_type
    i = len(data_pd_type) - 1
    if (i % 2 == 0):
        tree_type.insert("", i, "type%d"%(i+1), text ="%d" % (i+1), values=(data_pd_type['Название'].values[i]), tag = "COLOR")
    else:
        tree_type.insert("", i, "type%d"%(i+1), text ="%d" % (i+1), values=(data_pd_type['Название'].values[i]))
    tree_type.tag_configure("COLOR", background = '#fff8dc')#у каждой четной делай bg

# Добавление блюда в Excel в страницу "Меню"
def insert_menu_string_excel(string_dish):
    """
    Автор: Исмаилов Асад
    Цель: Добавление нового блюда в датафрейм и Excel
    Вход: string_dish (данные нового блюда)
    Выход: Обновленная таблица блюд
    
    """
    global data_pd_menu
    data_pd_menu = data_pd_menu.append({'Код блюда':len(data_pd_menu)+1, 'Наименование блюда':string_dish[0], 'Стоимость':string_dish[1],'Размерность':string_dish[2], 'Тип блюда':string_dish[3]}, ignore_index=True)
    data_excel_menu.range('A1').options(index = False).value = data_pd_menu
    print(data_pd_menu)
    print(string_dish)

# Добавление блюда в treeview (в таблицу Меню и в полную таблицу)
def insert_menu_string_tree(tree_menu, tree_full):
    """
    Автор: Исмаилов Асад
    Цель: Чтение данных нового блюда из датафрейма и вывод в treeview
    Вход: tree_menu (дерево блюд), tree_full(дерево полной таблицы)
    Выход: Обновленные деревья блюд и полной таблицы
    
    """
    global data_pd_menu
    global data_pd_full
    global data_pd_type
    i = len(data_pd_menu) - 1
    if (i % 2 == 0):
        tree_menu.insert("", i, "menu%d"%(i+1), text ="%d" % (i+1), values=(data_pd_menu['Наименование блюда'].values[i], data_pd_menu['Стоимость'].values[i], data_pd_menu['Размерность'].values[i], data_pd_menu['Тип блюда'].values[i]), tag = "COLOR")
    else:
        tree_menu.insert("", i, "menu%d"%(i+1), text ="%d" % (i+1),values=(data_pd_menu['Наименование блюда'].values[i], data_pd_menu['Стоимость'].values[i], data_pd_menu['Размерность'].values[i], data_pd_menu['Тип блюда'].values[i]))
    k = len(data_pd_full)
    data_pd_full = data_pd_full.append({'Код блюда':k+1, 'Наименование блюда':data_pd_menu['Наименование блюда'].values[k], 'Стоимость':data_pd_menu['Стоимость'].values[k], 'Размерность':data_pd_menu['Размерность'].values[k], 'Тип блюда':data_pd_menu['Тип блюда'].values[k]}, ignore_index=True)
    if(k % 2 == 0):
        tree_full.insert("", k, "full%d"%(k+1), text ="%d" % (k+1), values=(data_pd_full['Наименование блюда'].values[k], data_pd_full['Стоимость'].values[k], data_pd_full['Размерность'].values[k], data_pd_type['Название'].values[int(data_pd_menu['Тип блюда'].values[k]) - 1]), tag = "COLOR")
    else:
        tree_full.insert("", k, "full%d"%(k+1), text ="%d" % (k+1), values=(data_pd_full['Наименование блюда'].values[k], data_pd_full['Стоимость'].values[k], data_pd_full['Размерность'].values[k], data_pd_type['Название'].values[int(data_pd_menu['Тип блюда'].values[k]) - 1]))
    
    tree_menu.tag_configure("COLOR", background = '#fff8dc')#у каждой четной делай 
    tree_full.tag_configure("COLOR", background = '#fff8dc')#у каждой четной делай bg

# Добавление заказа в Excel в страницу "Заказы"
def insert_orders_string_excel(string_dish):
    """
    Автор: Исмаилов Асад
    Цель: Добавление нового заказа в датафрейм и Excel
    Вход: string_dish (данные нового заказа)
    Выход: Обновленная таблица заказов
    
    """
    global data_pd_orders
    global data_pd_menu
    summ_order = int(data_pd_menu.iloc[int(string_dish[3])-1, 2])*int(string_dish[4])
    if len(data_pd_orders)+1 < 10:
        data_pd_orders = data_pd_orders.append({'Код заказа':'А0%d'%(len(data_pd_orders)+1), 'Дата посещения':string_dish[1], 'Время посещения':string_dish[2],'Код блюда':string_dish[3], 'Количество порций':string_dish[4], 'Сумма':summ_order}, ignore_index=True)
    else:
        data_pd_orders = data_pd_orders.append({'Код заказа':'А%d'%(len(data_pd_orders)+1), 'Дата посещения':string_dish[1], 'Время посещения':string_dish[2],'Код блюда':string_dish[3], 'Количество порций':string_dish[4], 'Сумма':summ_order}, ignore_index=True)        
    data_excel_orders.range('A1').options(index = False).value = data_pd_orders
    print(data_pd_orders)
    print(string_dish)

# Добавление заказа в treeview (в таблицу заказов и в полную таблицу)
def insert_orders_string_tree(tree_orders, tree_full):
    """
    Автор: Исмаилов Асад
    Цель: Чтение данных нового заказа из датафрейма и вывод в treeview
    Вход: tree_orders (дерево заказов), tree_full (дерево полной таблицы)
    Выход: Обновленные деревья заказов и полной таблицы
    
    """
    global data_pd_orders
    global data_pd_full_sub
    i = len(data_pd_orders) - 1
    if (i % 2 == 0):
        tree_orders.insert("", i, "order%d"%(i+1), text ="%d" % (i+1), values=(data_pd_orders['Дата посещения'].values[i], data_pd_orders['Время посещения'].values[i], data_pd_orders['Код блюда'].values[i], data_pd_orders['Количество порций'].values[i], data_pd_orders['Сумма'].values[i]), tag = "COLOR")
    else:
        tree_orders.insert("", i, "order%d"%(i+1), text ="%d" % (i+1), values=(data_pd_orders['Дата посещения'].values[i], data_pd_orders['Время посещения'].values[i], data_pd_orders['Код блюда'].values[i], data_pd_orders['Количество порций'].values[i], data_pd_orders['Сумма'].values[i]))
    k = len(data_pd_full_sub)
    data_pd_full_sub = data_pd_full_sub.append({'Код заказа':data_pd_orders['Код заказа'].values[k], 'Дата посещения':data_pd_orders['Дата посещения'].values[k], 'Время посещения':data_pd_orders['Время посещения'].values[k],'Код блюда':data_pd_orders['Код блюда'].values[k], 'Количество порций':data_pd_orders['Количество порций'].values[k], 'Сумма':data_pd_orders['Сумма'].values[k]}, ignore_index=True)
    s = len(tree_full.get_children("full%d"%(int(data_pd_full_sub['Код блюда'].values[k])))) + 1 #кол-во дочерних элементов + 1 для Заказ 1, Заказ 2, ...
    tree_full.insert("full%d"%(int(data_pd_full_sub['Код блюда'].values[k])), "end", "sub%d%d"%(int(data_pd_full_sub['Код блюда'].values[k])+1, s), text="Заказ %d"%s, values= ( "","","","", data_pd_full_sub['Код заказа'].values[k], data_pd_full_sub['Дата посещения'].values[k], data_pd_full_sub['Время посещения'].values[k], data_pd_full_sub['Количество порций'].values[k], data_pd_full_sub['Сумма'].values[k]))
    
    tree_orders.tag_configure("COLOR", background = '#fff8dc')#у каждой четной делай bg

def change_type_string_excel(string_dish, index_type):
    """
    Автор: Исмаилов Асад
    Цель: Изменение данных о типе блюда в датафрейме и Excel
    Вход: string_dish (новые данные изменяемого типа), index_type (номер типа в таблице)
    Выход: Обновленные датафрейма и Excel
    
    """
    global data_pd_type
    global data_pd_full
    global data_pd_full_sub
    source_type = data_pd_type.iloc[index_type,1] # Исходный тип до изменения
    data_pd_type.iloc[index_type,1] = string_dish[0]
    for i in range(len(data_pd_full)):
        if source_type is data_pd_full.iloc[i, 4]:
            data_pd_full.iloc[i, 4] = data_pd_type.iloc[index_type,1]
    for j in range(len(data_pd_full_sub)):
        if source_type is data_pd_full_sub.iloc[j, 4]:
            data_pd_full_sub[j, 4] = data_pd_type.iloc[index_type, 1]
    data_excel_type.range('A1').options(index = False).value = data_pd_type
    print(string_dish)
    print(index_type)

def change_order_string_excel(string_dish, index_order):
    """
    Автор: Исмаилов Асад
    Цель: Изменение данных о заказе в датафрейме и Excel
    Вход: string_dish (новые данные изменяемого заказа), index_order (номер заказа в таблице)
    Выход: Обновленные датафрейма и Excel
    
    """
    global data_pd_orders
    if index_order < 10:
        data_pd_orders.iloc[index_order, 0] = "А0%d"%(index_order+1)
    else:
        data_pd_orders.iloc[index_order, 0] = "А%d"%(index_order+1)
    for i in range(1, 6):
        data_pd_orders.iloc[index_order,i] = string_dish[i]
    data_excel_orders.range('A1').options(index = False).value = data_pd_orders
    print(string_dish)
    print(index_order)

def change_dish_string_excel(string_dish, index_menu):
    """
    Автор: Исмаилов Асад
    Цель: Изменение данных о блюде в датафрейме и Excel
    Вход: string_dish (новые данные изменяемого блюда), index_menu (номер блюда в таблице)
    Выход: Обновленные датафрейма и Excel
    
    """
    global data_pd_menu
    data_pd_menu.iloc[index_menu,0] = index_menu+1
    for i in range(1, 5):
        data_pd_menu.iloc[index_menu,i] = string_dish[i-1]
    data_excel_menu.range('A1').options(index = False).value = data_pd_menu
    print(string_dish)
    print(index_menu)

#Удаление строки под номером s в таблице
def deleting_string(s, id_tree):
    """
    Автор: Исмаилов Асад
    Цель: Удаление данных строки в датафрейме и Excel
    Вход: s (номер удаляемой строки в таблице), id_tree (id активного окна)
    Выход: Обновленные датафрейм и Excel
    
    """
    global data_pd_type
    global data_pd_orders
    global data_pd_menu
    global data_pd_full
    global data_pd_full_sub
    
    print(s)
    if id_tree == 0: # Если выделена строка из таблицы типов
        data_pd_type.drop([s], axis=0, inplace=True) # Удаление типа из датафрейма типов
        data_pd_type = data_pd_type.append({'Тип блюда':None, 'Название':None}, ignore_index=True)        
        data_excel_type.range('A1').options(index = False).value = data_pd_type
    
    if id_tree == 1: # Если выделена строка из таблицы заказов
        data_pd_orders.drop([s], axis=0, inplace=True) # Удаление заказа из датафрейма заказов
        data_pd_full_sub.drop([s], axis=0, inplace=True)
        data_pd_orders = data_pd_orders.append({'Код заказа':'', 'Дата посещения':'', 'Время посещения':'','Код блюда':None, 'Количество порций':None, 'Сумма':None}, ignore_index=True)    
        data_excel_orders.range('A1').options(index = False).value = data_pd_orders
    
    if id_tree == 2: # Если выделена строка из таблицы Меню
        data_pd_menu.drop([s], axis=0, inplace=True) # Удаление блюда из датафрейма Меню
        data_pd_full.drop([s], axis=0, inplace=True)
        data_pd_menu = data_pd_menu.append({'Код блюда':None, 'Наименование блюда':'', 'Стоимость':None,'Размерность':'', 'Тип блюда':''}, ignore_index=True)    
        data_excel_menu.range('A1').options(index = False).value = data_pd_menu
    
# При удалении заказа возвращает какую подстроку в полной удалить (Заказ 1 или Заказ 2?)
def num_sub(s):
    """
    Автор: Исмаилов Асад
    Цель: Узнать номер заказа в полной таблице в подстроке (Заказ 1, Заказ 2)
    Вход: s (номер заказа в treeview)
    Выход: Номер заказа в полной таблице
    
    """
    k = 1 # Заказ k: Заказ 1, Заказ 2,...
    global data_pd_full_sub
    a = data_pd_full_sub[['Код блюда','Код заказа']] # Датафрейм из кодов заказа с кодами заказанных блюд
    print(a)
    if s<10 and s>0: # Если это цифра, то заказ А0s, где s - номер заказа (Пример: А01, А07)
        b = a[a['Код заказа'] == "А0%d"%s]
    else: # Если это число больше 9, то заказ Аs, где s - номер заказа (Пример: А22, А13)
        b = a[a['Код заказа'] == "А%d"%s]
    b = int(b['Код блюда']) # Код блюда данного заказа
    print('Код блюда', b)
    a = a[a['Код блюда'] == b] # Все заказы с данным кодом блюда
    print(a)
    for i in range(len(a)):
        if s<10 and s>0:
            if a['Код заказа'].values[i] != "А0%d"%s:
                k += 1
            else:
                break
        elif s>9:
            if a['Код заказа'].values[i] != "А%d"%s:
                k += 1
            else:
                break
    return k

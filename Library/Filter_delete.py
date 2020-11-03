import Datas as prog
import Filter_functions as filtr
from ttkthemes import ThemedStyle
from tkinter import ttk
def init_number_of_frame(num):
    """
        Автор: Ворожцов Михаил
        Цель: Инициализация глобальной переменной(оперделить какой frame открыт)
        Вход: Номер столбца
        Выход: Измененная глобальная переменная

    """
    global number_of_frame
    number_of_frame = num


def delete(tree_list, tree):
    """
        Автор: Ворожцов Михаил
        Цель: Удаление выбранного фильтра
        Вход: Treeview текущий и списка фильтров
        Выход: Изменненые treeview

    """
    global number_of_frame
    #Удаляем в списке фильтров
    item = tree_list.selection()[0]
    tree_list.delete(item)
    filtr.delete_in_list_filtr_class(item)

    #Чистим дерево
    for i in tree.get_children():
        tree.delete(i)

    try:
        #Вставляем заново дерево
        if number_of_frame == 0:
            prog.insert_type(tree)
        elif number_of_frame == 1:
            prog.insert_orders(tree)
        elif number_of_frame == 2:
            prog.insert_menu(tree)
        else:
            prog.insert_full(tree)
    except:
        pass



    #Фильтруем
    filtr.delete_refresh(tree)



def delete_all(tree_list, tree):
    """
        Автор: Ворожцов Михаил
        Цель: Удаление фильтров
        Вход: Treeview текущий и списка фильтров
        Выход: Изменненые treeview

    """
    global number_of_frame

    for item in tree_list.get_children():
        tree_list.delete(item)
        filtr.delete_in_list_filtr_class(item)

    for i in tree.get_children():
        tree.delete(i)

    try:
        # Вставляем заново дерево
        if number_of_frame == 0:
            prog.insert_type(tree)
        elif number_of_frame == 1:
            prog.insert_orders(tree)
        elif number_of_frame == 2:
            prog.insert_menu(tree)
        else:
            prog.insert_full(tree)
    except:
        pass

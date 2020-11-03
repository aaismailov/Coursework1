from tkinter import *
from ttkthemes import ThemedStyle
from tkinter import ttk
import Filter_functions as fun
import Filter_delete as fd
import Scripts.default as default

integers = ["Тип блюда", "Код заказа", "Код блюда", "Количество порций", "Сумма заказа", "Стоимость", "Размерность"]
words = ["Название", "Наименование блюда", "Тип"]
dates = ["Дата посещения"]
times = ["Время посещения"]
global check_open_toplevel
check_open_toplevel = False

def on_close():
    """
        Автор: Ворожцов Михаил
        Цель: Закрывает окно Toplevel с фильтром
        Вход: -
        Выход: Измененная глобальная переменная check_open_toplevel

    """
    global check_open_toplevel
    check_open_toplevel = not check_open_toplevel
    fun.init_check_toplevel(check_open_toplevel)
    new_win.destroy()

def create_toplevel(root):
    """
        Автор: Ворожцов Михаил
        Цель: Создает окно Toplevel
        Вход:root
        Выход: Глобальные переменные(new_win, check_open_toplevel), создание Toplevel

    """
    global new_win
    global check_open_toplevel

    # создаем окно фильтра
    new_win = Toplevel(root)
    new_win.protocol("WM_DELETE_WINDOW", on_close)
    new_win.resizable(width = False,height= False)
    #new_win.geometry("+1300+100")
    check_open_toplevel = not check_open_toplevel
    fun.init_check_toplevel(check_open_toplevel)

def create_curr_list(root,tree):
    """
        Автор: Ворожцов Михаил
        Цель: Создает список текущих фильтров
        Вход: root, tree(текущее treeview в зависимости от frame'а)
        Выход: Глобальные переменные(label_filter,tree_list), создание списка в Toplevel

    """
    global label_filter
    global tree_list
    # Создаем LabelFrame


    label_filter = ttk.LabelFrame(new_win, text="Текущие фильтры", width=230, height=50, style = 'style.TLabelframe')
    #label_filter.place(x=1290, y=10)
    label_filter.grid(row = 0, column = 0,  pady = 5, padx = 5, sticky = N)

    #Создаем дерево для списка
    tree_list = ttk.Treeview(label_filter,height = 10)
    tree_list.pack(side = TOP, fill = 'y')
    tree_list.config(height = 7)

    tree_list["columns"] = ("one")
    tree_list.column("#0", width=100, minwidth=80)
    tree_list.column("#1", width=110, minwidth=105)

    tree_list.heading("#0", text="Колонка", anchor=W)
    tree_list.heading("#1", text= "Значение", anchor=W)

    but_dell = ttk.Button(label_filter, text="Удалить", width=20, command = lambda : fd.delete(tree_list,tree))
    but_dell.pack(side= TOP)

    but_dell_all = ttk.Button(label_filter, text="Очистить всё", width=20, command = lambda :fd.delete_all(tree_list,tree))
    but_dell_all.pack(side=TOP)

    fun.init_gl_tree(tree_list)
    fun.open_toplevel_check_filter()






def create_label_choice(new_win):
    global label
    """
        Автор: Ворожцов Михаил
        Цель: Создаем label'a для меню выбора фильтра/сортировки 
        Вход: окно Toplevel'
        Выход: Label для меню

    """

    label = ttk.LabelFrame(new_win, text="Меню выбора", width=216, height=270, style = 'style.TLabelframe')
    #label.place(x = 1290, y = 202)
    label.grid(row = 1, column = 0)


#Создаем шаблоны выбора
def pattern_integer(label, tree, num):
    """
        Автор: Ворожцов Михаил
        Цель: Создание шаблона меню выбора для целых чисел
        Вход: label меню выбора, текущий treeview для передачи в филтр, номер столбца
        Выход: Глобальные переменные(label_sort,label_range,check_open_toplevel), отрисованные кнопик и entry

    """
    global label_sort
    global label_range
    global check_open_toplevel

    fun.init_label_filter(label) #Чтобы потом удалить

    #Сортировка
    label_sort = ttk.LabelFrame(label, text="Сортировка", width=20, height=10, style='style.TLabelframe')
    label_sort.place(x=5, y=5)

    but_sort_ascending = ttk.Button(label_sort, text="По возростанию", width=20, command = lambda : fun.sort_descending(tree, num))
    but_sort_ascending.pack(side= TOP)

    but_sort_descending = ttk.Button(label_sort, text="По убыванию", width=20, command = lambda: fun.sort_ascending(tree, num))
    but_sort_descending.pack(side= TOP)


    #Диапазон
    label_range = ttk.LabelFrame(label, text="Диапазон", width=20, height=10, style='style.TLabelframe')
    label_range.place(x=5, y=105)


    #Создаем рамки для строк
    first_line = ttk.Label(label_range)
    first_line.pack(side = TOP)

    second_line = ttk.Label(label_range)
    second_line.pack(side=TOP)

    #Первая строка
    #От
    label_from = ttk.LabelFrame(first_line, text="От", width=20, height=10, style = 'style.TLabelframe')
    label_from.pack(side = LEFT)

    entry_from = ttk.Entry(label_from, width = 14)
    entry_from.pack()
    entry_from.insert(0,"0")

    #До
    label_to = ttk.LabelFrame(first_line, text="До", width=20, height=10, style='style.TLabelframe')
    label_to.pack(side = LEFT)

    entry_to  = ttk.Entry(label_to, width = 14)
    entry_to.pack()
    entry_to.insert(0,"255")

    #Вторая строка
    but_ok = ttk.Button(second_line, text="Применить", width=20, command = lambda : fun.filter_int(tree, entry_from.get(), entry_to.get(), num, tree_list))
    but_ok.pack()



def pattern_word(label,tree, num):
    """
        Автор: Ворожцов Михаил
        Цель: Создание шаблона меню выбора для слов
        Вход: label меню выбора, текущий treeview для передачи в филтр, номер столбца
        Выход: Глобальные переменные(label_sort,label_range), отрисованные кнопик и entry

    """
    global label_sort
    global label_range
    #Сортировка
    label_sort = ttk.LabelFrame(label, text="Сортировка", width=20, height=10, style='style.TLabelframe')
    label_sort.place(x=5, y=5)

    but_sort_ascending = ttk.Button(label_sort, text="От А до Я", width=20, command = lambda : fun.sort_ascending(tree, num))
    but_sort_ascending.pack(side=TOP)

    but_sort_descending = ttk.Button(label_sort, text="От Я до А", width=20, command = lambda :  fun.sort_descending(tree, num))
    but_sort_descending.pack(side=TOP)

    #Диапазон/Фильтр
    label_range = ttk.LabelFrame(label, text="Диапазон", width=20, height=10, style='style.TLabelframe')
    label_range.place(x=5, y=105)

    combo  = ttk.Combobox(label_range, values = ("Начиная с...", "Ключевое слово"),width = 29)
    combo.current(0)
    combo.pack()

    entry = ttk.Entry(label_range, width=25)
    entry.pack()
    entry.insert(0, "Слово")

    but_ok = ttk.Button(label_range, text="Применить", width=10, command = lambda :fun.filter_word(tree,combo.get(), entry.get(),num,tree_list))
    but_ok.pack()



def pattern_date(label, tree, num):
    """
        Автор: Ворожцов Михаил
        Цель: Создание шаблона меню выбора для даты
        Вход: label меню выбора, текущий treeview для передачи в филтр, номер столбца
        Выход: Глобальные переменные(label_sort,label_range), отрисованные кнопик и entry

    """
    global label_sort
    global label_range
    label_sort = ttk.LabelFrame(label, text="Сортировка", width=20, height=10, style='style.TLabelframe')
    label_sort.place(x=5, y=5)

    but_sort_ascending = ttk.Button(label_sort, text="Более новые", width=20, command = lambda : fun.sort_data_new(tree,num))
    but_sort_ascending.pack(side=TOP)

    but_sort_descending = ttk.Button(label_sort, text="Более старые", width=20, command = lambda : fun.sort_data_old(tree, num))
    but_sort_descending.pack(side=TOP)

    # Диапазон
    label_range = ttk.LabelFrame(label, text="Диапазон", width=20, height=10, style='style.TLabelframe')
    label_range.place(x=5, y=105)

    # Создаем рамки для строк
    first_line = ttk.Label(label_range)
    first_line.pack(side=TOP)

    second_line = ttk.Label(label_range)
    second_line.pack(side=TOP)

    # Первая строка
    # От
    label_from = ttk.LabelFrame(first_line, text="От", width=20, height=10, style='style.TLabelframe')
    label_from.pack(side=LEFT)

    entry_from_day = ttk.Entry(label_from, width=14)
    entry_from_day.pack(side = TOP)
    entry_from_day.insert(0, "День")

    entry_from_month = ttk.Entry(label_from, width=14)
    entry_from_month.pack(side = TOP)
    entry_from_month.insert(0, "Месяц")

    entry_from_year = ttk.Entry(label_from, width=14)
    entry_from_year.pack(side=TOP)
    entry_from_year.insert(0, "Год")

    # До
    label_to = ttk.LabelFrame(first_line, text="До", width=20, height=10, style='style.TLabelframe')
    label_to.pack(side=LEFT)

    entry_to_day = ttk.Entry(label_to, width=14)
    entry_to_day.pack(side=TOP)
    entry_to_day.insert(0, "День")

    entry_to_month = ttk.Entry(label_to, width=14)
    entry_to_month.pack(side=TOP)
    entry_to_month.insert(0, "Месяц")

    entry_to_year = ttk.Entry(label_to, width=14)
    entry_to_year.pack(side=TOP)
    entry_to_year.insert(0, "Год")

    # Вторая строка
    but_ok = ttk.Button(second_line, text="Применить", width=20, command = lambda : fun.filter_data(tree, entry_from_day.get(), entry_from_month.get(),
                                                                                        entry_from_year.get(), entry_to_day.get(), entry_to_month.get(),
                                                                                                    entry_to_year.get(), num, tree_list))
    but_ok.pack()

def pattern_time(label, tree, num):
    """
        Автор: Ворожцов Михаил
        Цель: Создание шаблона меню выбора для времени
        Вход: label меню выбора, текущий treeview для передачи в филтр, номер столбца
        Выход: Глобальные переменные(label_sort,label_range), отрисованные кнопик и entry

    """
    global label_sort
    global label_range
    label_sort = ttk.LabelFrame(label, text="Сортировка", width=20, height=10, style='style.TLabelframe')
    label_sort.place(x=5, y=5)

    but_sort_ascending = ttk.Button(label_sort, text="Более новые", width=20, command = lambda: fun.sort_time_new(tree,num))
    but_sort_ascending.pack(side=TOP)

    but_sort_descending = ttk.Button(label_sort, text="Более старые", width=20, command = lambda: fun.sort_time_old(tree, num))
    but_sort_descending.pack(side=TOP)

    # Диапазон
    label_range = ttk.LabelFrame(label, text="Диапазон", width=20, height=10, style='style.TLabelframe')
    label_range.place(x=5, y=105)

    # Создаем рамки для строк
    first_line = ttk.Label(label_range)
    first_line.pack(side=TOP)

    second_line = ttk.Label(label_range)
    second_line.pack(side=TOP)

    # Первая строка
    # От
    label_from = ttk.LabelFrame(first_line, text="От", width=20, height=10, style='style.TLabelframe')
    label_from.pack(side=LEFT)

    entry_from = ttk.Entry(label_from, width=14)
    entry_from.pack()
    entry_from.insert(0, "00:00")

    # До
    label_to = ttk.LabelFrame(first_line, text="До", width=20, height=10, style='style.TLabelframe')
    label_to.pack(side=LEFT)

    entry_to = ttk.Entry(label_to, width=14)
    entry_to.pack()
    entry_to.insert(0, "23:59")

    # Вторая строка
    but_ok = ttk.Button(second_line, text="Применить", width=20, command = lambda : fun.filter_time(tree, entry_from.get(),entry_to.get() , num, tree_list))
    but_ok.pack()


def create_filter(root, check_open, tree, name, num):
    """
        Автор: Ворожцов Михаил
        Цель: Вызывает функции создания виджетов для Toplevel
        Вход: root, check_open(флаг), текущий treeview, название столбца, номер столбца
        Выход:

    """
    global check_open_toplevel
    global check_name


    original_data = [k for k in tree.get_children()]
    print(original_data)

    # Стиль для  Labelframe'ов
    style_new = ttk.Style()
    style_new.configure('style.TLabelframe', background= default.background_filter)

    #Если окно ещё не создано, то создаем
    if check_open_toplevel == False:
        #root.geometry("+0+115")
        create_toplevel(root)  # Создаем окно
        create_curr_list(root,tree)#Создаем виджеты в этой рамке
        create_label_choice(new_win)  # Создаем рамку и виджеты для фильтров

        if name in integers:
            pattern_integer(label,tree, num)
        elif name in words:
            pattern_word(label,tree, num)
        elif name in dates:
            pattern_date(label, tree, num)
        else:
            pattern_time(label, tree, num)

        check_name = name
    else:
        #Если создано, то смотрим убирать его или перерисовать фильтр
        if check_name == name:
            new_win.destroy()
            check_open_toplevel = False
            #root.geometry("1293x515+130+120")
        else:
            label.destroy()

            create_label_choice(new_win)  # Создаем рамку и виджеты для фильтров

            if name in integers:
                pattern_integer(label,tree, num)
            elif name in words:
                pattern_word(label, tree, num)
            elif name in dates:
                pattern_date(label, tree, num)
            else:
                pattern_time(label, tree, num)

            check_name = name


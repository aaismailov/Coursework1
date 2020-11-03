from datetime import datetime
from tkinter import messagebox
import Filter_delete as fd
import Delete_functions as del_f

list_filtr_class_0 = [] #инициализация списка
list_filtr_class_1 = []
list_filtr_class_2 = []
list_filtr_class_3 = []
refresh_list_how = []
refresh_list_type = []

integers = ["Тип блюда", "Код заказа", "Код блюда", "Количество порций", "Сумма заказа", "Стоимость", "Размерность"]
words = ["Название", "Наименование блюда", "Тип"]
dates = ["Дата посещения"]
times = ["Время посещения"]

class check_list_filter(object):
    """
                        Автор: Ворожцов Михаил
                        Цель: Создаем класс для храниения информации о фильтрах
                        Вход: __init__ - name_type, name_how, name_num,num, append_how - name_how, name_num и change -  name_how, name_num
                        Выход: Созданный/Измененный класс

    """
    #сохраняем список
    def __init__(self, name_type, name_how, name_num,num):
        self.name_type = name_type
        self.name_how = [name_how]
        self.name_num = [name_num]
        self.num = num
    def append_how(self, name_how, name_num):
        self.name_how.append(name_how)
        self.name_num.append(name_num)
    def change(self, name_how, name_num):
        self.name_num[self.name_how.index(name_how)-1] = name_num

def sort_ascending(tv, num):
    """
        Автор: Ворожцов Михаил
        Цель: Сортировка по возрастанию
        Вход: текущий treeview, номер выбранного столбцы
        Выход: Отсортированный по возрастанию treeview

    """
    #По возрастанию
    num = int(num)
    if num == 0:
        l = [(int(tv.item(k)["text"]), k) for k in tv.get_children()]
        l = sorted(l, key= lambda t: t[0], reverse=True)
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)
    else:
        num -= 1
        l = [(int(tv.item(k)["values"][num]), k) for k in tv.get_children()]  # Display column #0 cannot be set
        l = sorted(l, key= lambda t: t[0],reverse= True)

        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)

def sort_descending(tv, num):
    """
        Автор: Ворожцов Михаил
        Цель: Сортировка по убыванию
        Вход: текущий treeview, номер выбранного столбцы
        Выход: Отсортированный по убыванию treeview

    """
    #По убыванию
    num = int(num)
    if num == 0:
        l = [(int(tv.item(k)["text"]), k) for k in tv.get_children()]
        l = sorted(l, key = lambda t: t[0], reverse = False)

        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)
    else:
        num -= 1
        l = [(int(tv.item(k)["values"][num]), k) for k in tv.get_children()]  # Display column #0 cannot be set
        l = sorted(l, key=lambda t: t[0], reverse=False)

        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)

def sort_data_new(tv, num):
    """
        Автор: Ворожцов Михаил
        Цель: Сортировка даты(более новая)
        Вход: текущий treeview, номер выбранного столбцы
        Выход: Отсортированный treeview

    """
    #По убыванию
    num = int(num)
    num -= 1
    l = [(tv.item(k)["values"][num], k) for k in tv.get_children()]  # Display column #0 cannot be set
    l = sorted(l, key=lambda t: datetime.strptime(t[0], "%d.%m.%Y"), reverse=True)

    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

def sort_data_old(tv, num):
    """
        Автор: Ворожцов Михаил
        Цель: Сортировка даты(более поздняя)
        Вход: текущий treeview, номер выбранного столбцы
        Выход: Отсортированный treeview

    """
    #По убыванию
    num = int(num)
    num -= 1
    l = [(tv.item(k)["values"][num], k) for k in tv.get_children()]  # Display column #0 cannot be set
    l = sorted(l, key=lambda t: datetime.strptime(t[0], "%d.%m.%Y"), reverse=False)

    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

def sort_time_new(tv, num):
    """
        Автор: Ворожцов Михаил
        Цель: Сортировка даты(более новая)
        Вход: текущий treeview, номер выбранного столбцы
        Выход: Отсортированный treeview

    """
    #По убыванию
    num = int(num)
    num -= 1
    l = [(tv.item(k)["values"][num], k) for k in tv.get_children()]  # Display column #0 cannot be set
    l = sorted(l, key=lambda t: datetime.strptime(t[0], "%H:%M"), reverse = False)

    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

def sort_time_old(tv, num):
    """
        Автор: Ворожцов Михаил
        Цель: Сортировка даты(более поздняя)
        Вход: текущий treeview, номер выбранного столбцы
        Выход: Отсортированный treeview

    """
    #По убыванию
    num = int(num)
    num -= 1
    l = [(tv.item(k)["values"][num], k) for k in tv.get_children()]  # Display column #0 cannot be set
    l = sorted(l, key=lambda t: datetime.strptime(t[0], "%H:%M"), reverse = True)

    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

#Вставка новых данных
def insetr_curr_list(tree_list, name_type, name_how, name_num,num):
    """
        Автор: Ворожцов Михаил
        Цель: Вставка новых данных в список фильтров
        Вход: treeview для списков, название столбца, имя фильтра(как фильтруем),значение фильтра, номер столбца
        Выход: Измененные глобальные переменные, измененный список фильтров

    """
    #Списки с фильтрами
    global gl_tree
    global gl_tree_list
    global number_note_frame
    global list_filtr_class_0
    global list_filtr_class_1
    global list_filtr_class_2
    global list_filtr_class_3
    list_filtr_class = []

    #Какое окно
    if number_note_frame == 0:
        list_filtr_class = list_filtr_class_0
    elif number_note_frame == 1:
        list_filtr_class = list_filtr_class_1
    elif number_note_frame == 2:
        list_filtr_class = list_filtr_class_2
    else:
        list_filtr_class = list_filtr_class_3


    type = [(k.name_type) for k in list_filtr_class]# какой столбец
    if name_type in type:
        #Достаем какой фильтр
        how = list_filtr_class[type.index(name_type)].name_how
        if name_how in how:#Если уже есть такой фильтр
            tree_list.item(name_type+name_how, values = name_num)
            list_filtr_class[type.index(name_type) - 1].change(name_how,name_num)
        else:
            tree_list.insert(name_type, "end",id = name_type+name_how, text=name_how, values=(name_num))
            list_filtr_class[type.index(name_type) ].append_how(name_how,name_num)

    else:
        list_filtr_class.append(check_list_filter(name_type,name_how,name_num,num))
        tree_list.insert("", "end", id = name_type , text=name_type)
        tree_list.insert(name_type, "end", id = name_type+name_how, text=name_how, values=(name_num))


check_toplevel = False



#Обработка фильтра
def filter_int(tree, num_from, num_to, num, tree_list):
    """
        Автор: Ворожцов Михаил
        Цель: Обработка новых введеных данных и применение фильтра для целых чисел
        Вход: текущий treeview, начальное значение, конечно значение,номер столбца,treeview cо списком фильтров
        Выход: Отфильтрованный treeview,обновленный список фильтров

    """
    global list_filtr_class


    try:
        num_f = int(num_from)
    except:
        num_f = " "

    try:
        num_t = int(num_to)
    except:
        num_t = " "

    if num_f == " " and num_t == " ":
        messagebox.showwarning("Warning", "Неверный ввод. Введите числа(игнорируя буквы)")
    else:
        #смотрим какой столбец
        num = int(num)
        try:
            if num == 0:
                #если первый
                if num_f != " " and num_t != " ":
                    l = [ k for k in tree.get_children() if int(tree.item(k)["text"]) > num_f and int(tree.item(k)["text"]) < num_t]
                    insetr_curr_list(tree_list, tree.heading("#0")["text"],"Больше",num_f,num)
                    insetr_curr_list(tree_list, tree.heading("#0")["text"], "Меньше", num_t,num)
                elif num_f != " ":
                    l = [ k for k in tree.get_children() if int(tree.item(k)["text"]) > num_f ]
                    insetr_curr_list(tree_list, tree.heading("#0")["text"], "Больше", num_f,num)
                elif num_t != " ":
                    l = [ k for k in tree.get_children() if int(tree.item(k)["text"]) < num_t]
                    insetr_curr_list(tree_list, tree.heading("#0")["text"], "Меньше", num_t,num)
            else:
                if num_f != " " and num_t != " ":
                    l = [ k for k in tree.get_children() if int(tree.item(k)["values"][num-1]) > num_f and int(tree.item(k)["values"][num-1]) < num_t]
                    insetr_curr_list(tree_list, tree.heading(("#%d") % num)["text"], "Больше", num_f,num)
                    insetr_curr_list(tree_list, tree.heading(("#%d") % num)["text"], "Меньше", num_t,num)
                elif num_f != " ":
                    l = [ k for k in tree.get_children() if int(tree.item(k)["values"][num-1]) > num_f ]
                    insetr_curr_list(tree_list, tree.heading(("#%d") % num)["text"], "Больше", num_f,num)
                elif num_t != " ":
                    l = [ k for k in tree.get_children() if int(tree.item(k)["values"][num-1]) < num_t]
                    insetr_curr_list(tree_list, tree.heading(("#%d") % num)["text"], "Меньше", num_t,num)
        except:#Для заказов
            try:
                if num == 0:
                    #если первый
                    if num_f != " " and num_t != " ":
                        l = [ k for k in tree.get_children() if int(tree.item(k)["text"][1:]) > num_f and int(tree.item(k)["text"][1:]) < num_t]
                        insetr_curr_list(tree_list, tree.heading("#0")["text"],"Больше",num_f,num)
                        insetr_curr_list(tree_list, tree.heading("#0")["text"], "Меньше", num_t,num)
                    elif num_f != " ":
                        l = [ k for k in tree.get_children() if int(tree.item(k)["text"][1:]) > num_f ]
                        insetr_curr_list(tree_list, tree.heading("#0")["text"], "Больше", num_f,num)
                    elif num_t != " ":
                        l = [ k for k in tree.get_children() if int(tree.item(k)["text"][1:]) < num_t]
                        insetr_curr_list(tree_list, tree.heading("#0")["text"], "Меньше", num_t,num)
                else:
                    if num_f != " " and num_t != " ":
                        l = [ k for k in tree.get_children() if int(tree.item(k)["values"][num-1][1:]) > num_f and int(tree.item(k)["values"][num-1][1:]) < num_t]
                        insetr_curr_list(tree_list, tree.heading(("#%d") % num)["text"], "Больше", num_f,num)
                        insetr_curr_list(tree_list, tree.heading(("#%d") % num)["text"], "Меньше", num_t,num)
                    elif num_f != " ":
                        l = [ k for k in tree.get_children() if int(tree.item(k)["values"][num-1][1:]) > num_f ]
                        insetr_curr_list(tree_list, tree.heading(("#%d") % num)["text"], "Больше", num_f,num)
                    elif num_t != " ":
                        l = [ k for k in tree.get_children() if int(tree.item(k)["values"][num-1][1:]) < num_t]
                        insetr_curr_list(tree_list, tree.heading(("#%d") % num)["text"], "Меньше", num_t,num)

            except:#Для размерности
                if num == 0:
                    #если первый
                    if num_f != " " and num_t != " ":
                        l = [ k for k in tree.get_children() if int(tree.item(k)["text"][2:]) > num_f and int(tree.item(k)["text"][2:]) < num_t]
                        insetr_curr_list(tree_list, tree.heading("#0")["text"],"Больше",num_f,num)
                        insetr_curr_list(tree_list, tree.heading("#0")["text"], "Меньше", num_t,num)
                    elif num_f != " ":
                        l = [ k for k in tree.get_children() if int(tree.item(k)["text"][2:]) > num_f ]
                        insetr_curr_list(tree_list, tree.heading("#0")["text"], "Больше", num_f,num)
                    elif num_t != " ":
                        l = [ k for k in tree.get_children() if int(tree.item(k)["text"][2:]) < num_t]
                        insetr_curr_list(tree_list, tree.heading("#0")["text"], "Меньше", num_t,num)
                else:
                    if num_f != " " and num_t != " ":
                        l = [ k for k in tree.get_children() if int(tree.item(k)["values"][num-1][2:]) > num_f and int(tree.item(k)["values"][num-1][2:]) < num_t]
                        insetr_curr_list(tree_list, tree.heading(("#%d") % num)["text"], "Больше", num_f,num)
                        insetr_curr_list(tree_list, tree.heading(("#%d") % num)["text"], "Меньше", num_t,num)
                    elif num_f != " ":
                        l = [ k for k in tree.get_children() if int(tree.item(k)["values"][num-1][2:]) > num_f ]
                        insetr_curr_list(tree_list, tree.heading(("#%d") % num)["text"], "Больше", num_f,num)
                    elif num_t != " ":
                        l = [ k for k in tree.get_children() if int(tree.item(k)["values"][num-1][2:]) < num_t]
                        insetr_curr_list(tree_list, tree.heading(("#%d") % num)["text"], "Меньше", num_t,num)

        for i in tree.get_children():
            if not(i in l):
                tree.delete(i)


#Вставка существующих данных
def refresh_curr_list(tree_list, name_type, name_how, name_num):
    """
        Автор: Ворожцов Михаил
        Цель: Вставка уже сформированных в списке классов фильтров
        Вход:  текущий treeview, начальное значение, конечно значение,treeview cо списком фильтров
        Выход: Обновленный список фильтров

    """
    global refresh_list_how
    global refresh_list_type

    type = refresh_list_type# какой столбец

    if name_type in type:
        #Достаем какой фильтр
        how = refresh_list_how
        if name_how in how:#Если уже есть такой фильтр
            tree_list.item(name_type+name_how, values = name_num)
        else:
            tree_list.insert(name_type, "end",id = name_type+name_how, text=name_how, values=(name_num))
            refresh_list_how.append(name_how)

    else:
        refresh_list_type.append(name_type)
        refresh_list_how = []
        tree_list.insert("", "end", id = name_type , text=name_type)
        tree_list.insert(name_type, "end", id = name_type+name_how, text=name_how, values=(name_num))


#Отклик на смену frame'ов в note_tree
number_note_frame = 0
fd.init_number_of_frame(number_note_frame)
def change_note_frame(event, note_tree):
    """
        Автор: Ворожцов Михаил
        Цель: Отклик на изменение Frame'а в note
        Вход: evet, ссылка на note_tree
        Выход: Измененные глобальные переменные, обновленный списко фильтров для текущего treeview

    """
    global number_note_frame
    global gl_tree
    global gl_tree_list
    global refresh_list_how
    global list_filtr_class_0
    global list_filtr_class_1
    global list_filtr_class_2
    global list_filtr_class_3
    global refresh_list_how
    global refresh_list_type
    global check_toplevel
    global label_filter
    refresh_list_how = []
    refresh_list_type = []
    number_note_frame = note_tree.index(note_tree.select())
    fd.init_number_of_frame(number_note_frame)


    if check_toplevel == True:
        tree = gl_tree

        for i in tree.get_children():
            tree.delete(i)
        label_filter.destroy()

        if number_note_frame == 0:
            for i in list_filtr_class_0:
                for j in range(len(i.name_how)):
                    refresh_curr_list(tree, i.name_type, i.name_how[j], i.name_num[j])
        elif number_note_frame == 1:
            for i in list_filtr_class_1:
                for j in range(len(i.name_how)):
                    refresh_curr_list(tree, i.name_type, i.name_how[j], i.name_num[j])
        elif number_note_frame == 2:
            for i in list_filtr_class_2:
                for j in range(len(i.name_how)):
                    refresh_curr_list(tree, i.name_type, i.name_how[j], i.name_num[j])
        else:
            for i in list_filtr_class_3:
                for j in range(len(i.name_how)):
                    refresh_curr_list(tree, i.name_type, i.name_how[j], i.name_num[j])

#Инициализация для удаления label_sort при смене frame'a
def init_label_filter(label):
    """
        Автор: Ворожцов Михаил
        Цель: Инициализация для удаления label_sort при смене frame'a
        Вход: Label
        Выход: Измененные глобальные переменные

    """
    global label_filter
    label_filter = label

def init_gl_tree(tree):
    """
        Автор: Ворожцов Михаил
        Цель: Инициализация глобальной переменной для других функций
        Вход: Текущий treeview
        Выход: Измененная глобальная переменная

    """
    global gl_tree
    gl_tree = tree

def init_check_toplevel(check_open_toplevel):
    """
        Автор: Ворожцов Михаил
        Цель: Инициализация глобальной переменной для проверки открыт/закрыт ли toplevel
        Вход: Флаг
        Выход: Измененная глобальная переменная

    """
    global check_toplevel
    check_toplevel = check_open_toplevel


#Если закрыли, а потом опять открыли top_level
def open_toplevel_check_filter():
    """
        Автор: Ворожцов Михаил
        Цель: Реакция на закрытие toplevel и открытия заново
        Вход: -
        Выход: Появления списка фильтров для текущего treeview

    """
    global list_filtr_class_0
    global list_filtr_class_1
    global list_filtr_class_2
    global list_filtr_class_3
    global refresh_list_how
    global refresh_list_type
    global number_note_frame
    global gl_tree
    refresh_list_how = []
    refresh_list_type = []
    tree = gl_tree

    if number_note_frame == 0:
        for i in list_filtr_class_0:
            for j in range(len(i.name_how)):
                refresh_curr_list(tree, i.name_type, i.name_how[j], i.name_num[j])
    elif number_note_frame == 1:
        for i in list_filtr_class_1:
            for j in range(len(i.name_how)):
                refresh_curr_list(tree, i.name_type, i.name_how[j], i.name_num[j])
    elif number_note_frame == 2:
        for i in list_filtr_class_2:
            for j in range(len(i.name_how)):
                refresh_curr_list(tree, i.name_type, i.name_how[j], i.name_num[j])
    else:
        for i in list_filtr_class_3:
            for j in range(len(i.name_how)):
                refresh_curr_list(tree, i.name_type, i.name_how[j], i.name_num[j])



#Оброботка фильтра для word(новые данные)
def filter_word(tree, task, key,num,tree_list):
    global list_filtr_class
    """
        Автор: Ворожцов Михаил
        Цель: Обработка новых введеных данных и применение фильтра для слов
        Вход: текущий treeview, название фильтра, значение фильтра,номер столбца,treeview cо списком фильтров 
        Выход: Отфильтрованный treeview,обновленный список фильтров

    """

    #смотрим какой столбец
    num = int(num)
    if num == 0:
        if task == "Начиная с...":
            l = [ k for k in tree.get_children() if tree.item(k)["text"][:len(key)] == key]
            insetr_curr_list(tree_list, tree.heading("#0")["text"],task,key,num)
        else:
            l = [k for k in tree.get_children() if tree.item(k)["text"].find(key) != -1]
            insetr_curr_list(tree_list, tree.heading("#0")["text"], task, key,num)
    else:
        if task == "Начиная с...":
            l = [ k for k in tree.get_children() if tree.item(k)["values"][num-1][:len(key)] == key]
            insetr_curr_list(tree_list, tree.heading(("#%d") % num)["text"],task,key,num)
        else:
            l = [k for k in tree.get_children() if tree.item(k)["values"][num-1].find(key) != -1]
            insetr_curr_list(tree_list, tree.heading(("#%d") % num)["text"], task, key,num)



    for i in tree.get_children():
        if not(i in l):
            tree.delete(i)


#Обработка фильтра даты
def filter_data(tree, date_from, month_from, year_from, date_to, month_to, year_to, num, tree_list):
    """
        Автор: Ворожцов Михаил
        Цель: Обработка новых введеных данных и применение фильтра для даты
        Вход: текущий treeview, начальное значение дня, начальное значение месяца,начальное значение года,
        конечно значение дня, конечно значение месяца, конечно значение года, номер столбца,treeview cо списком фильтров
        Выход: Отфильтрованный treeview,обновленный список фильтров

    """
    global list_filtr_class
    date_from_all = ""
    date_to_all = ""


    try:
        date_from_all = "%.2d.%.2d.%.4d" % (int(date_from),int(month_from),int(year_from))
        date_from = int(date_from)
        month_from = int(month_from)
        year_from = int(year_from)
        datetime(year_from, month_from, date_from)
    except:
        date_from = " "

    try:
        date_to_all = "%.2d.%.2d.%.4d" % (int(date_to), int(month_to), int(year_to))
        date_to = int(date_to)
        month_to = int(month_to)
        year_to = int(year_to)
        datetime(year_to, month_to, date_to)
    except:
        date_to = " "


    if (date_from == " " and date_to == " " ) :
        messagebox.showwarning("Warning", "Неверный ввод. Пожалуйста, введите повторно.")
    else:
        #смотрим какой столбец
        num = int(num)

        if num == 0:
            #если первый
            if date_from != " " and date_to != " ":
                l = [ k for k in tree.get_children() if datetime(int(tree.item(k)["text"][6:]),int(tree.item(k)["text"][3:5]), int(tree.item(k)["text"][:2])) > datetime(year_from,month_from,date_from)
                      and datetime(int(tree.item(k)["text"][6:]),int(tree.item(k)["text"][3:5]), int(tree.item(k)["text"][:2])) < datetime(year_to,month_to,date_to)]
                insetr_curr_list(tree_list, tree.heading("#0")["text"],"От",date_from_all,num)
                insetr_curr_list(tree_list, tree.heading("#0")["text"], "До", date_to_all,num)
            elif date_from != " ":
                l = [ k for k in tree.get_children() if datetime(int(tree.item(k)["text"][6:]),int(tree.item(k)["text"][3:5]), int(tree.item(k)["text"][:2])) > datetime(year_from,month_from,date_from)]
                insetr_curr_list(tree_list, tree.heading("#0")["text"], "От", date_from_all,num)
                messagebox.showwarning("Warning", "Неверный ввод данных 'До'.\nПожалуйста, введите повторно.")
            elif date_to != " ":
                l = [ k for k in tree.get_children() if datetime(int(tree.item(k)["text"][6:]),int(tree.item(k)["text"][3:5]), int(tree.item(k)["text"][:2])) < datetime(year_to,month_to,date_to)]
                insetr_curr_list(tree_list, tree.heading("#0")["text"], "До", date_to_all,num)
                messagebox.showwarning("Warning", "Неверный ввод данных 'От'.\nПожалуйста, введите повторно.")
        else:

            if date_from != " " and date_to != " ":
                l = [ k for k in tree.get_children() if datetime(int(tree.item(k)["values"][num-1][6:]), int(tree.item(k)["values"][num-1][3:5]), int(tree.item(k)["values"][num-1][:2])) > datetime(year_from,month_from,date_from)
                      and datetime(int(tree.item(k)["values"][num-1][6:]),int(tree.item(k)["values"][num-1][3:5]), int(tree.item(k)["values"][num-1][:2])) < datetime(year_to,month_to,date_to)]
                insetr_curr_list(tree_list, tree.heading(("#%d") % num)["text"],"От",date_from_all,num)
                insetr_curr_list(tree_list, tree.heading(("#%d") % num)["text"], "До", date_to_all,num)
            elif date_from != " ":
                l = [ k for k in tree.get_children() if datetime(int(tree.item(k)["values"][num-1][6:]),int(tree.item(k)["values"][num-1][3:5]), int(tree.item(k)["values"][num-1][:2])) > datetime(year_from,month_from,date_from)]
                insetr_curr_list(tree_list, tree.heading(("#%d") % num)["text"], "От", date_from_all,num)
                messagebox.showwarning("Warning", "Неверный ввод данных 'До'.\nПожалуйста, введите повторно.")
            elif date_to != " ":
                l = [ k for k in tree.get_children() if datetime(int(tree.item(k)["values"][num-1][6:]),int(tree.item(k)["values"][num-1][3:5]), int(tree.item(k)["values"][num-1][:2])) < datetime(year_to,month_to,date_to)]
                insetr_curr_list(tree_list, tree.heading(("#%d") % num)["text"], "До", date_to_all,num)
                messagebox.showwarning("Warning", "Неверный ввод данных 'От'.\nПожалуйста, введите повторно.")




        for i in tree.get_children():
            if not(i in l):
                tree.delete(i)


#Обработка фильтра времени
def filter_time(tree, entry_from, entry_to, num, tree_list):
    """
        Автор: Ворожцов Михаил
        Цель: Обработка новых введеных данных и применение фильтра для времени
        Вход: текущий treeview, начальное значение, конечно значение,номер столбца,treeview cо списком фильтров
        Выход: Отфильтрованный treeview,обновленный список фильтров

    """
    global list_filtr_class
    time_from_all = ""
    time_to_all = ""


    try:
        time_from_all = entry_from
        hour_from = int(entry_from[:2])
        minutes_from = int(entry_from[3:])
        time_from = datetime(1,1,1,hour=hour_from,minute=minutes_from)
    except:
        hour_from = " "


    try:
        time_to_all = entry_to
        hour_to = int(entry_to[:2])
        minutes_to = int(entry_to[3:])
        time_to = datetime(1,1,1,hour=hour_to, minute=minutes_to)
    except:
        hour_to = " "


    if (hour_from == " " and hour_to == " " ) :
        messagebox.showwarning("Warning", "Неверный ввод. Пожалуйста, введите повторно.")
    else:
        #смотрим какой столбец
        num = int(num)

        if num == 0:
            #если первый
            if hour_from != " " and hour_to != " ":
                l = [ k for k in tree.get_children() if datetime(1,1,1, hour=int(tree.item(k)["text"][:2]),minute=int(tree.item(k)["text"][3:])) > time_from
                      and datetime(1,1,1, hour=int(tree.item(k)["text"][:2]),minute=int(tree.item(k)["text"][3:])) < time_to]
                insetr_curr_list(tree_list, tree.heading("#0")["text"],"От",time_from_all,num)
                insetr_curr_list(tree_list, tree.heading("#0")["text"], "До", time_to_all,num)
            elif hour_from != " ":
                l = [ k for k in tree.get_children() if datetime(1,1,1, hour=int(tree.item(k)["text"][:2]),minute=int(tree.item(k)["text"][3:])) > time_from]
                insetr_curr_list(tree_list, tree.heading("#0")["text"], "От", time_from_all,num)
                messagebox.showwarning("Warning", "Неверный ввод данных 'До'.\nПожалуйста, введите повторно.")
            elif hour_to != " ":
                l = [ k for k in tree.get_children() if datetime(1,1,1, hour=int(tree.item(k)["text"][:2]),minute=int(tree.item(k)["text"][3:])) < time_to]
                insetr_curr_list(tree_list, tree.heading("#0")["text"], "До", time_to_all,num)
                messagebox.showwarning("Warning", "Неверный ввод данных 'От'.\nПожалуйста, введите повторно.")
        else:

            if hour_from != " " and hour_to != " ":
                l = [ k for k in tree.get_children() if datetime(1,1,1, hour=int(tree.item(k)["values"][num-1][:2]),minute=int(tree.item(k)["values"][num-1][3:])) > time_from
                      and datetime(1,1,1, hour=int(tree.item(k)["values"][num-1][:2]),minute=int(tree.item(k)["values"][num-1][3:])) < time_to]
                insetr_curr_list(tree_list, tree.heading(("#%d") % num)["text"],"От",time_from_all,num)
                insetr_curr_list(tree_list, tree.heading(("#%d") % num)["text"], "До", time_to_all,num)
            elif hour_from != " ":
                l = [ k for k in tree.get_children() if datetime(1,1,1, hour=int(tree.item(k)["values"][num-1][:2]),minute=int(tree.item(k)["values"][num-1][3:])) > time_from]
                insetr_curr_list(tree_list, tree.heading(("#%d") % num)["text"], "От", time_from_all,num)
                messagebox.showwarning("Warning", "Неверный ввод данных 'До'.\nПожалуйста, введите повторно.")
            elif hour_to != " ":
                l = [ k for k in tree.get_children() if datetime(1,1,1, hour=int(tree.item(k)["values"][num-1][:2]),minute=int(tree.item(k)["values"][num-1][3:])) < time_to]
                insetr_curr_list(tree_list, tree.heading(("#%d") % num)["text"], "До", time_to_all,num)
                messagebox.showwarning("Warning", "Неверный ввод данных 'От'.\nПожалуйста, введите повторно.")



        for i in tree.get_children():
            if not(i in l):
                tree.delete(i)


def delete_in_list_filtr_class(type):
    """
        Автор: Ворожцов Михаил
        Цель: Удаляет выбранный фильтр из списка
        Вход: Название столбца
        Выход: Измененый спискок классов

    """
    if number_note_frame == 0:
        for i in list_filtr_class_0:
            if i.name_type == type:
                list_filtr_class_0.remove(i)
    elif number_note_frame == 1:
        for i in list_filtr_class_1:
            if i.name_type == type:
                list_filtr_class_1.remove(i)
    elif number_note_frame == 2:
        for i in list_filtr_class_2:
            if i.name_type == type:
                list_filtr_class_2.remove(i)
    else:
        for i in list_filtr_class_3:
            if i.name_type == type:
                list_filtr_class_3.remove(i)


def delete_refresh(tree):
    """
        Автор: Ворожцов Михаил
        Цель: Обновления treeview после удаления фильтра
        Вход: Текущий treeview
        Выход: Измененный treeview

    """
    if number_note_frame == 0:
        for i in list_filtr_class_0:
                if i.name_type in integers:
                    for j in range(len(i.name_how)):
                        if i.name_how[j] == "Больше":
                            del_f.delete_filter_int(tree,i.name_num[j]," ",i.num)
                        else:
                            del_f.delete_filter_int(tree, " ", i.name_num[j], i.num)
                else:
                    for j in range(len(i.name_how)):
                            del_f.delete_filter_word(tree,i.name_how[j],i.name_num[j],i.num)

    elif number_note_frame == 1:
        for i in list_filtr_class_1:
                if i.name_type in integers:
                    for j in range(len(i.name_how)):
                        if i.name_how[j] == "Больше":
                            del_f.delete_filter_int(tree,i.name_num[j]," ",i.num)
                        else:
                            del_f.delete_filter_int(tree, " ", i.name_num[j], i.num)
                elif i.name_type in words:#22.12.2000
                    for j in range(len(i.name_how)):
                            del_f.delete_filter_word(tree,i.name_how[j],i.name_num[j],i.num)
                elif i.name_type in dates:
                    for j in range(len(i.name_how)):
                        if i.name_how[j] == "От":
                            del_f.delete_filter_data(tree,i.name_num[j][:2],i.name_num[j][3:5],i.name_num[j][6:]," "," ", " ", i.num)
                        else:
                            del_f.delete_filter_data(tree, " ", " ", " ", i.name_num[j][:2], i.name_num[j][3:5], i.name_num[j][6:], i.num)

                elif i.name_type in times:
                    for j in range(len(i.name_how)):
                        if i.name_how[j] == "От":
                            del_f.delete_filter_time(tree,i.name_num[j]," ", i.num)
                        else:
                            del_f.delete_filter_time(tree," ",i.name_num[j], i.num)

    elif number_note_frame == 2:
        for i in list_filtr_class_2:
            if i.name_type in integers:
                for j in range(len(i.name_how)):
                    if i.name_how[j] == "Больше":
                        del_f.delete_filter_int(tree, i.name_num[j], " ", i.num)
                    else:
                        del_f.delete_filter_int(tree, " ", i.name_num[j], i.num)
            elif i.name_type in words:  # 22.12.2000
                for j in range(len(i.name_how)):
                    del_f.delete_filter_word(tree, i.name_how[j], i.name_num[j], i.num)
            elif i.name_type in dates:
                for j in range(len(i.name_how)):
                    if i.name_how[j] == "От":
                        del_f.delete_filter_data(tree, i.name_num[j][:2], i.name_num[j][3:5], i.name_num[j][6:], " ",
                                                 " ", " ", i.num)
                    else:
                        del_f.delete_filter_data(tree, " ", " ", " ", i.name_num[j][:2], i.name_num[j][3:5],
                                                 i.name_num[j][6:], i.num)

            elif i.name_type in times:
                for j in range(len(i.name_how)):
                    if i.name_how[j] == "От":
                        del_f.delete_filter_time(tree, i.name_num[j], " ", i.num)
                    else:
                        del_f.delete_filter_time(tree, " ", i.name_num[j], i.num)
    else:
       for i in list_filtr_class_3:
           if i.name_type in integers:
               for j in range(len(i.name_how)):
                   if i.name_how[j] == "Больше":
                       del_f.delete_filter_int(tree, i.name_num[j], " ", i.num)
                   else:
                       del_f.delete_filter_int(tree, " ", i.name_num[j], i.num)
           elif i.name_type in words:  # 22.12.2000
               for j in range(len(i.name_how)):
                   del_f.delete_filter_word(tree, i.name_how[j], i.name_num[j], i.num)
           elif i.name_type in dates:
               for j in range(len(i.name_how)):
                   if i.name_how[j] == "От":
                       del_f.delete_filter_data(tree, i.name_num[j][:2], i.name_num[j][3:5], i.name_num[j][6:], " ",
                                                " ", " ", i.num)
                   else:
                       del_f.delete_filter_data(tree, " ", " ", " ", i.name_num[j][:2], i.name_num[j][3:5],
                                                i.name_num[j][6:], i.num)

           elif i.name_type in times:
               for j in range(len(i.name_how)):
                   if i.name_how[j] == "От":
                       del_f.delete_filter_time(tree, i.name_num[j], " ", i.num)
                   else:
                       del_f.delete_filter_time(tree, " ", i.name_num[j], i.num)





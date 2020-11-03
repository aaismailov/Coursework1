from tkinter import messagebox
from datetime import datetime
def delete_filter_int(tree, num_from, num_to, num):
    """
        Автор: Ворожцов Михаил
        Цель: Обработать treeview после удаления числового фильтра
        Вход: текущий treeview, начальное значение, конечно значение,номер столбца
        Выход: Отфильтрованный treeview

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
                elif num_f != " ":
                    l = [ k for k in tree.get_children() if int(tree.item(k)["text"]) > num_f ]
                elif num_t != " ":
                    l = [ k for k in tree.get_children() if int(tree.item(k)["text"]) < num_t]
            else:
                if num_f != " " and num_t != " ":
                    l = [ k for k in tree.get_children() if int(tree.item(k)["values"][num-1]) > num_f and int(tree.item(k)["values"][num-1]) < num_t]
                elif num_f != " ":
                    l = [ k for k in tree.get_children() if int(tree.item(k)["values"][num-1]) > num_f ]
                elif num_t != " ":
                    l = [ k for k in tree.get_children() if int(tree.item(k)["values"][num-1]) < num_t]
        except:#Для заказов
            try:
                if num == 0:
                    #если первый
                    if num_f != " " and num_t != " ":
                        l = [ k for k in tree.get_children() if int(tree.item(k)["text"][1:]) > num_f and int(tree.item(k)["text"][1:]) < num_t]
                    elif num_f != " ":
                        l = [ k for k in tree.get_children() if int(tree.item(k)["text"][1:]) > num_f ]
                    elif num_t != " ":
                        l = [ k for k in tree.get_children() if int(tree.item(k)["text"][1:]) < num_t]
                else:
                    if num_f != " " and num_t != " ":
                        l = [ k for k in tree.get_children() if int(tree.item(k)["values"][num-1][1:]) > num_f and int(tree.item(k)["values"][num-1][1:]) < num_t]
                    elif num_f != " ":
                        l = [ k for k in tree.get_children() if int(tree.item(k)["values"][num-1][1:]) > num_f ]
                    elif num_t != " ":
                        l = [ k for k in tree.get_children() if int(tree.item(k)["values"][num-1][1:]) < num_t]

            except:#Для размерности
                if num == 0:
                    #если первый
                    if num_f != " " and num_t != " ":
                        l = [ k for k in tree.get_children() if int(tree.item(k)["text"][2:]) > num_f and int(tree.item(k)["text"][2:]) < num_t]
                    elif num_f != " ":
                        l = [ k for k in tree.get_children() if int(tree.item(k)["text"][2:]) > num_f ]
                    elif num_t != " ":
                        l = [ k for k in tree.get_children() if int(tree.item(k)["text"][2:]) < num_t]
                else:
                    if num_f != " " and num_t != " ":
                        l = [ k for k in tree.get_children() if int(tree.item(k)["values"][num-1][2:]) > num_f and int(tree.item(k)["values"][num-1][2:]) < num_t]
                    elif num_f != " ":
                        l = [ k for k in tree.get_children() if int(tree.item(k)["values"][num-1][2:]) > num_f ]
                    elif num_t != " ":
                        l = [ k for k in tree.get_children() if int(tree.item(k)["values"][num-1][2:]) < num_t]

        for i in tree.get_children():
            if not(i in l):
                tree.delete(i)


def delete_filter_word(tree, task, key,num):
    """
        Автор: Ворожцов Михаил
        Цель: Обработать treeview после удаления фильтра слов
        Вход: текущий treeview, название фильтра, значение фильтра,номер столбца
        Выход: Отфильтрованный treeview

    """
    global list_filtr_class

    #смотрим какой столбец
    num = int(num)
    if num == 0:
        if task == "Начиная с...":
            l = [ k for k in tree.get_children() if tree.item(k)["text"][:len(key)] == key]
        else:
            l = [k for k in tree.get_children() if tree.item(k)["text"].find(key) != -1]

    else:
        if task == "Начиная с...":
            l = [ k for k in tree.get_children() if tree.item(k)["values"][num-1][:len(key)] == key]
        else:
            l = [k for k in tree.get_children() if tree.item(k)["values"][num-1].find(key) != -1]




    for i in tree.get_children():
        if not(i in l):
            tree.delete(i)



def delete_filter_data(tree, date_from, month_from, year_from, date_to, month_to, year_to, num):
    """
        Автор: Ворожцов Михаил
        Цель: Обработать treeview после удаления фильтра даты
        Вход: текущий treeview, начальное значение дня, начальное значение месяца,начальное значение года,
            конечно значение дня, конечно значение месяца, конечно значение года, номер столбца
        Выход: Отфильтрованный treeview

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

            elif date_from != " ":
                l = [ k for k in tree.get_children() if datetime(int(tree.item(k)["text"][6:]),int(tree.item(k)["text"][3:5]), int(tree.item(k)["text"][:2])) > datetime(year_from,month_from,date_from)]

            elif date_to != " ":
                l = [ k for k in tree.get_children() if datetime(int(tree.item(k)["text"][6:]),int(tree.item(k)["text"][3:5]), int(tree.item(k)["text"][:2])) < datetime(year_to,month_to,date_to)]

        else:

            if date_from != " " and date_to != " ":
                l = [ k for k in tree.get_children() if datetime(int(tree.item(k)["values"][num-1][6:]), int(tree.item(k)["values"][num-1][3:5]), int(tree.item(k)["values"][num-1][:2])) > datetime(year_from,month_from,date_from)
                      and datetime(int(tree.item(k)["values"][num-1][6:]),int(tree.item(k)["values"][num-1][3:5]), int(tree.item(k)["values"][num-1][:2])) < datetime(year_to,month_to,date_to)]

            elif date_from != " ":
                l = [ k for k in tree.get_children() if datetime(int(tree.item(k)["values"][num-1][6:]),int(tree.item(k)["values"][num-1][3:5]), int(tree.item(k)["values"][num-1][:2])) > datetime(year_from,month_from,date_from)]

            elif date_to != " ":
                l = [ k for k in tree.get_children() if datetime(int(tree.item(k)["values"][num-1][6:]),int(tree.item(k)["values"][num-1][3:5]), int(tree.item(k)["values"][num-1][:2])) < datetime(year_to,month_to,date_to)]





        for i in tree.get_children():
            if not(i in l):
                tree.delete(i)


def delete_filter_time(tree, entry_from, entry_to, num):
    """
        Автор: Ворожцов Михаил
        Цель: Обработать treeview после удаления фильтра времени
        Вход: текущий treeview, начальное значение, конечно значение,номер столбца
        Выход: Отфильтрованный treeview

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

            elif hour_from != " ":
                l = [ k for k in tree.get_children() if datetime(1,1,1, hour=int(tree.item(k)["text"][:2]),minute=int(tree.item(k)["text"][3:])) > time_from]

            elif hour_to != " ":
                l = [ k for k in tree.get_children() if datetime(1,1,1, hour=int(tree.item(k)["text"][:2]),minute=int(tree.item(k)["text"][3:])) < time_to]

        else:

            if hour_from != " " and hour_to != " ":
                l = [ k for k in tree.get_children() if datetime(1,1,1, hour=int(tree.item(k)["values"][num-1][:2]),minute=int(tree.item(k)["values"][num-1][3:])) > time_from
                      and datetime(1,1,1, hour=int(tree.item(k)["values"][num-1][:2]),minute=int(tree.item(k)["values"][num-1][3:])) < time_to]

            elif hour_from != " ":
                l = [ k for k in tree.get_children() if datetime(1,1,1, hour=int(tree.item(k)["values"][num-1][:2]),minute=int(tree.item(k)["values"][num-1][3:])) > time_from]

            elif hour_to != " ":
                l = [ k for k in tree.get_children() if datetime(1,1,1, hour=int(tree.item(k)["values"][num-1][:2]),minute=int(tree.item(k)["values"][num-1][3:])) < time_to]




        for i in tree.get_children():
            if not(i in l):
                tree.delete(i)
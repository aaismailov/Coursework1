import matplotlib.pyplot as plt
from tkinter import messagebox
types = ["Название"]
orders = ["Дата посещения", "Время посещения","Код блюда", "Количество порций", "Сумма заказа"]
menu = ["Наименование блюда", "Стоимость", "Размерность", "Тип блюда"]
integers = ["Тип блюда", "Код заказа", "Код блюда", "Количество порций", "Сумма заказа", "Стоимость", "Размерность"]


def create_histogram(tree_type, tree_orders, tree_menu,name):
    """
        Автор: Ворожцов Михаил, Якупов Ильшат
        Цель: Создает гистограмму
        Вход: Ссылки на дерево типов, заказов и меню, название типа данных
        Выход: Отрисованный график

    """
    # Histogram (order cost / amount of orders)
    if name in types:
        tree = tree_type
        list = types
    elif name in orders:
        tree = tree_orders
        list = orders
    else:
        tree = tree_menu
        list = menu

    x = tree.get_children()
    orders_cost = []
    dif = []
    for i in x:
        orders_cost.append(tree.item(i).get('values')[list.index(name)])
        if not(tree.item(i).get('values')[list.index(name)] in dif):
            dif.append(tree.item(i).get('values')[list.index(name)])
    fig, ax = plt.subplots()
    ax.hist(orders_cost, bins= int(len(dif)))
    ax.set_title('Гистограмма распределения количества заказов от %s' % name)
    ax.set_ylabel('Количество заказов, шт.')
    ax.set_xlabel(name)
    plt.xticks(rotation=-30, horizontalalignment='left', fontsize=7)
    plt.show()

def create_barchart(tree_type, tree_orders, tree_menu,name_f, name_t):
    """
        Автор: Ворожцов Михаил, Якупов Ильшат
        Цель: Создает ступенчатую диаграмму
        Вход: Ссылки на дерево типов, заказов и меню, название типа данных в X и Y
        Выход: Отрисованный график

    """
    # Bar graph (average price / dish type)

    if name_f in types and name_t in types:
        tree = tree_type
        list = types
    elif name_f in orders and name_t in orders:
        tree = tree_orders
        list = orders
    elif name_t in menu and name_f in menu:
        tree = tree_menu
        list = menu
    else:
        messagebox.showinfo("Подсказка", "Данный график можно построить для данных из одной таблицы(выберите в X и Y)")
        return


    os_x =[]
    os_y = []
    x = tree.get_children()
    for i in x:
        os_x.append(tree.item(i).get('values')[list.index(name_f)])
        os_y.append(tree.item(i).get('values')[list.index(name_t)])

    fig, ax = plt.subplots()

    ax.bar(os_x, os_y)

    ax.set_title('Ступенчатая диаграмма %s от %s' % (name_f,name_t))
    ax.set_ylabel(name_t)
    ax.set_xlabel(name_f)
    fig.tight_layout()
    plt.xticks(rotation=-30, horizontalalignment='left', fontsize=7)
    plt.show()


def create_box_plot(tree_type, tree_orders, tree_menu,name):
    """
        Автор: Ворожцов Михаил, Якупов Ильшат
        Цель: Создает диаграмму размаха
        Вход: Ссылки на дерево типов, заказов и меню, название типа данных
        Выход: Отрисованный график

    """
    # Box plot (price of dishes for several types of dishes)

    if name != "Размерность" and name != "Стоимость":
        messagebox.showinfo("Подсказка", "Данный график можно построить для Стоимости и Размерности(выберите в поле X)")
        return

    if name in types:
        tree = tree_type
        list = types
    elif name in orders:
        tree = tree_orders
        list = orders
    else:
        tree = tree_menu
        list = menu



    dish_name = []


    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []

    list_type = {1: list1 , 2: list2, 3: list3, 4 : list4, 5 : list5, 6 : list6, 7 : list7, 8 : list8}


    x = tree.get_children()
    for i in x:
        #os_y.append(tree.item(i).get('values')[list.index(name)])
        list_type[int(tree.item(i).get('values')[-1])].append(tree.item(i).get('values')[list.index(name)])
    for i in tree_type.get_children():
        dish_name.append(tree_type.item(i).get('values')[0])
    fig, ax = plt.subplots()

    if name == "Размерность":
        for i in (list1,list2,list3,list4,list5,list6,list7,list8):
            print(i)
            for j in i:
                #print(j ,kek)
                i[i.index(j)] = int(j[2:])
            print(i)

    ax.boxplot((list1,list2,list3,list4,list5,list6,list7,list8) ,sym="o")
    ax.set_xticklabels(dish_name, rotation=-30, horizontalalignment='left', fontsize=7)

    ax.set_title('Диаграмма размаха %s(и) для типов блюд' % name)
    ax.set_ylabel(name)
    ax.set_xlabel("Тип блюда")
    fig.tight_layout()
    plt.xticks(rotation=-30, horizontalalignment='left', fontsize=7)
    plt.show()




def create_scatter_plot(tree_type, tree_orders, tree_menu,name_f, name_t):
    """
        Автор: Ворожцов Михаил, Якупов Ильшат
        Цель: Создает диаграмма рассеивания
        Вход: Ссылки на дерево типов, заказов и меню, название типа данных в X и Y
        Выход: Отрисованный график

    """
    # Scatter plot (order time / order cost)


    if name_f in types and name_t in types:
        tree = tree_type
        list = types
    elif name_f in orders and name_t in orders:
        tree = tree_orders
        list = orders
    elif name_t in menu and name_f in menu:
        tree = tree_menu
        list = menu
    else:
        messagebox.showinfo("Подсказка", "Данный график можно построить для данных из одной таблицы(выберите в X и Y)")
        return


    os_x =[]
    os_y = []
    x = tree.get_children()
    for i in x:
        os_x.append(tree.item(i).get('values')[list.index(name_f)])
        os_y.append(tree.item(i).get('values')[list.index(name_t)])

    fig, ax = plt.subplots()

    ax.scatter(os_x, os_y)

    ax.set_title('Диаграмма рассеивания %s и %s' % (name_f,name_t))
    ax.set_ylabel(name_t)
    ax.set_xlabel(name_f)
    fig.tight_layout()
    plt.xticks(rotation=-30, horizontalalignment='left', fontsize=7)
    plt.show()







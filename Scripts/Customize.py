from tkinter import *
from  tkinter import  colorchooser
import  os

import Scripts.default as default
from tkinter import ttk
from ttkthemes import ThemedStyle
from PIL import Image, ImageTk

def create_menu_castom(style_all, lb, root):
    """
        Автор: Ворожцов Михаил
        Цель: Создает окно кастомицзаии
        Вход: Ссылка на стиль, Label у гланого окна, root
        Выход: Отрисованное окно кастомизации

    """
    global castom_win

    # создаем окно фильтра
    castom_win = Toplevel()
    castom_win.resizable(width=False, height=False)
    can = Label(castom_win,  width = 600, height = 800, background = default.background_custom)
    can.place(x = 0, y = 0)

    #Label'ы
    label_color = LabelFrame(castom_win, text="Смена цветов", width=230, height=50)
    label_color.pack(side = TOP, pady=5, padx=10)

    label_style = LabelFrame(castom_win, text="Смена стиля", width=280, height=50)
    label_style.pack(side = TOP, pady=5, padx=10)



    #Кнопки
    #Смена цветов
    but_fil = ttk.Button(label_color, text="Цвет фильтра", width=18, command=lambda : color_filtr())
    but_fil.pack(side = TOP, pady=5, padx=10)

    but_curr = ttk.Button(label_color, text="Цвет окна кастомизации", width=18, command=lambda: color_castom(can))
    but_curr.pack(side=TOP, pady=5, padx=10)

    but_main = ttk.Button(label_color, text="Цвет основного окна", width=18, command=lambda : color_main(lb,root))
    but_main.pack(side = TOP, pady=5, padx=10)

    label_grad = LabelFrame(label_color, text="Градиент для main", width=190, height=50)
    label_grad.pack(side = TOP, pady=5, padx=10)

    combo = ttk.Combobox(label_grad,width = 25)
    colors = ["Необычный синий", "Красненький", "Полоски", "Ромбики", "Радуга", "Глубокие ромбики", "Расвет"]
    combo["values"] = colors
    combo.current(0)
    combo.pack(side = TOP, pady=5, padx=10)

    but_ok = ttk.Button(label_grad, text="Применить", width=18, command=lambda: grad_main(lb,colors.index(combo.get())+1))
    but_ok.pack(side=TOP, pady=5, padx=10)

    #Стиль
    combo_style = ttk.Combobox(label_style, width=30)
    colors_style = ["radiance", "arc", "breeze", "black", "classic", "keramik", "winnative"]
    combo_style["values"] = colors_style
    combo_style.current(0)
    combo_style.pack(side=TOP, pady=5, padx=10)

    but_style_ok = ttk.Button(label_style, text="Применить", width=21, command=lambda: change_theme(combo_style.get(),style_all))
    but_style_ok.pack(side=TOP, pady=5, padx=10)

    #default
    but_def = ttk.Button(castom_win, text="Настройки по умолчанию", width=24, command=lambda: change_on_default(lb, style_all, can))
    but_def.pack(side = TOP, pady=5, padx=10)



def color_filtr():
    """
        Автор: Ворожцов Михаил
        Цель: Меняет цвет окна фильтра
        Вход: -
        Выход: Измененые переменные в default

    """
    color = colorchooser.askcolor()
    default.background_filter = color[1]

def color_main(lb,root):
    """
        Автор: Ворожцов Михаил
        Цель: Меня цвет основго окна
        Вход: Label основного окна(фон), root
        Выход: Измененые переменные в default

    """
    color = colorchooser.askcolor()
    lb.config( image = '')
    root["background"] = color[1]

def grad_main(lb, num):
    """
        Автор: Ворожцов Михаил
        Цель: Создает фон основного окна(градиентный)
        Вход: Label основного окна(фон), номер выбранного варианта
        Выход: Измененые переменные в default

    """
    default.name_back = "%d.jpg" % num
    Library = os.getcwd()

    os.chdir(default.way)
    img = Image.open(default.name_back)
    ph = ImageTk.PhotoImage(img)
    lb.config(image = ph)
    lb.imagine = ph
    os.chdir(Library)

def change_theme(name, style_all):
    """
        Автор: Ворожцов Михаил
        Цель: Меняет тему приложения
        Вход: Название темы, ссылка на стиль
        Выход: Измененые переменные в default

    """
    default.style = name
    style_all.set_theme(default.style)

def color_castom(can):
    """
        Автор: Ворожцов Михаил
        Цель: Меняет тему в окне кастомизации
        Вход: Label у окна
        Выход: Измененые переменные в default

    """
    color = colorchooser.askcolor()
    default.background_custom = color[1]
    can.config(background = color[1])

def change_on_default(lb, style_all, can):
    """
        Автор: Ворожцов Михаил
        Цель: Возвращает стандартные значения
        Вход: Label основного окна, ссылка на стиль, Label окна кастомизации
        Выход: Измененые переменные в default

    """
    grad_main(lb,int(default.def_name_back[:1]))
    change_theme(default.def_style, style_all)
    default.background_filter = default.def_background_filter
    can.config(background=default.def_background_custom)

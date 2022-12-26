import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from tkcalendar import DateEntry
from datetime import datetime
from datetime import timedelta

#Вариант 6. Администратор гостиницы. Имеется список номеров: класс, число мест. Имеется
#список гостей: паспортные данные, даты приезда и отъезда, номер.
#Программа должна осуществлять поселение гостей: выбор подходящего номера (при наличии свободных мест), регистрация, оформление квитанции;
#оформлять документы при отъезде: выбор всех постояльцев, отъезжающих в конкретный день, освобождение мест и оформление задержки с выпиской дополнительной квитанции.
#Реализовать возможность досрочного отъезда с перерасчетом и поиск гостя по произвольному признаку.

klass1 = ("Люкс", "Бизнес", "Апартаменты", "Комфорт", "Стандарт", "Эконом")
price = {"Люкс": 50000, "Бизнес": 25000, "Апартаменты": 40000, "Комфорт": 15000, "Стандарт": 7000, "Эконом": 3000}
#klass = {"Люкс": 10, "Бизнес": 15, "Апартаменты": 5, "Комфорт": 20, "Стандарт": 30}

window = Tk()
window.title("Администратор")
window.geometry("1600x1200")




def reg_show():
    zas_fio.pack(side=LEFT, padx=10, pady=0)
    ent_fio.pack(side=LEFT, padx=110, pady=0)
    lbl_pass.pack(side=LEFT, padx=10, pady=0)
    ent_pass.pack(side=LEFT, padx=75, pady=0)
    btn_reg.pack(side=LEFT, padx=280, pady=10)
    choice_fio.pack_forget()
    list_fio.pack_forget()
    btn_refresh.pack_forget()
    lbl_klass.pack_forget()
    combo_klass.pack_forget()
    lbl_zas.pack_forget()
    cal_zas.pack_forget()
    lbl_vis.pack_forget()
    cal_vis.pack_forget()
    btn_zas.pack_forget()
def reg_btn():
    input_fio = ent_fio.get()
    ent_passport = ent_pass.get()
    if input_fio != "" and ent_passport != "":
        reg_data = {"ФИО": input_fio, "Серия и номер паспорта": ent_passport, "Класс номера": "", "Дата заселения": "", "Дата выселения": ""}  # создали переменную, включающую в себя данные, которые мы хотим добавить в уже имеющийся файл
        with open("spisok_guest.json", encoding="utf-8") as guest_r:  # Открываем файл
            data = json.load(guest_r)  # Получае все данные из файла (вообще все, да)
        data.append(reg_data)  # Добавляем данные
        with open("spisok_guest.json", "w", encoding="utf-8") as guest_w:  # Открываем файл для записи
            json.dump(data, guest_w, ensure_ascii=False, indent=2)  # Добавляем данные (все, что было ДО добавления данных + добавленные данные)
        messagebox.showinfo(title="Регистрация гостей", message="Гость был успешно зарегистрирован")
    elif input_fio == "" or ent_passport == "":
        messagebox.showerror(title="Ошибка!", message="Все поля должны быть заполнены!")
def zas_show():
    choice_fio.pack(side=LEFT, padx=10, pady=0)
    list_fio.pack(side=LEFT, padx=11, pady=0)
    btn_refresh.pack(side=LEFT, padx=270, pady=10)
    lbl_klass.pack(side=LEFT, padx=10, pady=0)
    combo_klass.pack(side=LEFT, padx=11, pady=0)
    lbl_zas.pack(side=LEFT, padx=10, pady=0)
    cal_zas.pack(side=LEFT, padx=90, pady=0)
    lbl_vis.pack(side=LEFT, padx=10, pady=0)
    cal_vis.pack(side=LEFT, padx=86, pady=0)
    btn_zas.pack(side=LEFT, padx=270, pady=10)
    zas_fio.pack_forget()
    ent_fio.pack_forget()
    lbl_pass.pack_forget()
    ent_pass.pack_forget()
    btn_reg.pack_forget()
def zaselenie():
    choice_combo = combo_klass.get()
    cal_z = cal_zas.get()
    cal_v = cal_vis.get()
    date1 = datetime.strptime(cal_z, "%d.%m.%Y")
    date2 = datetime.strptime(cal_v, "%d.%m.%Y")
    with open("spisok_guest.json", encoding="utf-8") as guest_r:
        data = json.load(guest_r)  # Получае все данные из файла (вообще все, да)
    #if choice_combo != "":
    if choice_combo != "":
        for guests in data:
            data["Класс номера"] = "choice_combo"  #Здесь я хотел изменить значения ключей из списка гостей
            #data["Дата заселения"] = cal_z  #Здесь я хотел изменить значения ключей из списка гостей
            #data["Дата выселения"] = cal_v  #Здесь я хотел изменить значения ключей из списка гостей
            with open("spisok_guest.json", "w", encoding="utf-8") as guest_w:  # Открываем файл для записи
                json.dump(data, guest_w, ensure_ascii=False, indent=2)  # Добавляем данные (все, что было ДО добавления данных + добавленные данные)
                s = date2.date() - date1.date()
                with open("spisok_nomerov.json", encoding="utf-8") as nomer_r:
                    data_2 = json.load(nomer_r)
                data_2[choice_combo] = data_2[choice_combo] - 1
                with open("spisok_nomerov.json", "w", encoding="utf-8") as nomer_w:
                    json.dump(data_2, nomer_w, ensure_ascii=False, indent=2)
                kvit = s.days * price[choice_combo]
                mes = f"Гость был успешно заселен!\nКоличество дней: {s.days}\nСумма к оплате: {kvit} рублей"
            messagebox.showinfo(title="Заселение гостей", message=mes)
    elif choice_combo == "" or cal_z == cal_v :
        messagebox.showerror(title="Ошибка!", message="Все поля должны быть заполнены! Даты заселения и выселения должны отличаться!")
def zad_show():
    choice_fio.pack(side=LEFT, padx=10, pady=0)
    list_fio.pack(side=LEFT, padx=11, pady=0)
    btn_refresh.pack(side=LEFT, padx=270, pady=10)
    lbl_zas.pack(side=LEFT, padx=10, pady=0)
    cal_zas.pack(side=LEFT, padx=90, pady=0)
    lbl_vis.pack(side=LEFT, padx=10, pady=0)
    cal_vis.pack(side=LEFT, padx=86, pady=0)
    btn_zas.pack(side=LEFT, padx=270, pady=10)
    lbl_klass.pack_forget()
    combo_klass.pack_forget()
    zas_fio.pack_forget()
    ent_fio.pack_forget()
    lbl_pass.pack_forget()
    ent_pass.pack_forget()
    btn_reg.pack_forget()
def vis_zad():
    choice_combo = combo_klass.get().capitalize()
    cal_z = cal_zas.get()
    cal_v = cal_vis.get()
    date1 = datetime.strptime(cal_z, "%d.%m.%Y")
    date2 = datetime.strptime(cal_v, "%d.%m.%Y")
    with open("spisok_guest.json", encoding="utf-8") as guest_r:
        data = json.load(guest_r)
    if choice_combo == "" or cal_z == cal_v :
        messagebox.showerror(title="Ошибка!", message="Все поля должны быть заполнены! Даты заселения и выселения должны отличаться!")
    #elif choice_fio != "":
def dos_show():
    choice_fio.pack(side=LEFT, padx=10, pady=0)
    list_fio.pack(side=LEFT, padx=11, pady=0)
    btn_refresh.pack(side=LEFT, padx=270, pady=10)
    lbl_zas.pack(side=LEFT, padx=10, pady=0)
    cal_zas.pack(side=LEFT, padx=90, pady=0)
    lbl_vis.pack(side=LEFT, padx=10, pady=0)
    cal_vis.pack(side=LEFT, padx=86, pady=0)
    btn_zas.pack(side=LEFT, padx=270, pady=10)
    lbl_klass.pack_forget()
    combo_klass.pack_forget()
    zas_fio.pack_forget()
    ent_fio.pack_forget()
    lbl_pass.pack_forget()
    ent_pass.pack_forget()
    btn_reg.pack_forget()


frame1 = Frame(window)
frame1.pack(fill=X)
lbl_zas = Label(frame1, text="Администратор гостиницы", font=("Arial", 20), fg="aquamarine", bg="blue")
lbl_zas.pack(anchor="n", padx=0, pady=10)

var = IntVar()
var.set(0)
frame2 = Frame(window)
frame2.pack(fill=X)
radio_1 = Radiobutton(frame2, text="Регистрация гостей", variable=var, value=0, font=("Arial", 16), command=reg_show)
radio_1.pack(side=LEFT, padx=50, pady=20)
radio_2 = Radiobutton(frame2, text="Заселение гостей", variable=var, value=1, font=("Arial", 16), command=zas_show)
radio_2.pack(side=LEFT, padx=50, pady=0)
radio_3 = Radiobutton(frame2, text="Выселение с задержкой", variable=var, value=2, font=("Arial", 16), command=zad_show)
radio_3.pack(side=LEFT, padx=50, pady=0)
radio_4 = Radiobutton(frame2, text="Досрочное выселение", variable=var, value=3, font=("Arial", 16), command=dos_show)
radio_4.pack(side=LEFT, padx=50, pady=0)

#ПЕРВАЯ РАДИОКНОПКА
frame3 = Frame(window)
frame3.pack(fill=X)
zas_fio = Label(frame3, text="Введите ФИО", font=("Arial", 16))
zas_fio.pack(side=LEFT, padx=10, pady=0)
zas_fio.pack_forget()
ent_fio = Entry(frame3, fg="black", bg="silver", width=45)
ent_fio.pack(side=LEFT, padx=110, pady=0)
ent_fio.pack_forget()

frame4 = Frame(window)
frame4.pack(fill=X)
lbl_pass = Label(frame4, text="Введите серию\nи номер паспорта", font=("Arial", 16))
lbl_pass.pack(side=LEFT, padx=10, pady=0)
lbl_pass.pack_forget()
ent_pass = Entry(frame4, fg="black", bg="silver", width=45)
ent_pass.pack(side=LEFT, padx=75, pady=0)
ent_pass.pack_forget()

frame5 = Frame(window)
frame5.pack(fill=X)
btn_reg = Button(frame5, text="Зарегистрировать гостя", font=("Arial", 16), width=20, bg="green", fg="white", command=reg_btn)
btn_reg.pack(side=LEFT, padx=280, pady=10)
btn_reg.pack_forget()

#ВТОРАЯ И ТРЕТЬЯ РАДИОКНОПКИ
choice_fio = Label(frame4, text="Выберите ФИО", font=("Arial", 16))
choice_fio.pack(side=LEFT, padx=10, pady=0)
choice_fio.pack_forget()

fio = []
with open("spisok_guest.json", encoding="utf-8") as guests:
    data_3 = json.load(guests)
for guest in data_3:
    fio.append(guest["ФИО"])
list_var = Variable(value=fio)
list_fio = Listbox(frame4, listvariable=list_var, width=40, bg="silver", font=("Arial", 16))
list_fio.pack(side=LEFT, padx=11, pady=0)
list_fio.pack_forget()
btn_refresh = Button(frame4, text="Обновить список", font=("Arial", 16), width=20, bg="green", fg="white")
btn_refresh.pack(side=LEFT, padx=270, pady=0)
btn_refresh.pack_forget()

lbl_klass = Label(frame5, text="Выберите класс номера", font=("Arial", 16))
lbl_klass.pack(side=LEFT, padx=10, pady=0)
lbl_klass.pack_forget()

var = StringVar()
combo_klass = ttk.Combobox(frame5, textvariable=var, width=15, font=("Arial", 16))
combo_klass["values"] = klass1
combo_klass["state"] = "readonly"
combo_klass.pack(side=LEFT, padx=11, pady=0)
combo_klass.pack_forget()

frame6 = Frame(window)
frame6.pack(fill=X)
lbl_zas = Label(frame6, text="Дата заселения", font=("Arial", 16))
lbl_zas.pack(side=LEFT, padx=10, pady=0)
lbl_zas.pack_forget()
fact_zas = "" #В третьей радиокнопке, вместо выпадающего календаря с датой заселения должна просто стоять дата, когда заселился гость(берется из БД)
lbl_factzas = Label(frame6, text=fact_zas, font=("Arial", 16))
lbl_factzas.pack(side=LEFT, padx=10, pady=0)
lbl_factzas.pack_forget()
cal_zas = DateEntry(frame6, width=12, year=2022, month=12, day=18, date_pattern="d.m.yyyy")
cal_zas.pack(side=LEFT, padx=90, pady=0)
cal_zas.pack_forget()

frame7 = Frame(window)
frame7.pack(fill=X)
lbl_vis = Label(frame7, text="Дата выселения", font=("Arial", 16))
lbl_vis.pack(side=LEFT, padx=10, pady=0)
lbl_vis.pack_forget()
cal_vis = DateEntry(frame7, width=12, year=2022, month=12, day=18, date_pattern="d.m.yyyy")
cal_vis.pack(side=LEFT, padx=86, pady=0)
cal_vis.pack_forget()

frame8 = Frame(window)
frame8.pack(fill=X)
btn_zas = Button(frame8, text="Заселить", font=("Arial", 16), width=20, bg="green", fg="white", command=zaselenie)
btn_zas.pack(side=LEFT, padx=270, pady=10)
btn_zas.pack_forget()




#2 блок







window.mainloop()
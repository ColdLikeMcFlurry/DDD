import json #Подключили библиотеку
new_data = {"ФИО": input_fio, "Класс номера": choise_combo, "Дата заселения": cal_z, "Дата выселения": calv} #создали переменную, включающую в себя данные, которые мы хотим добавить в уже имеющийся файл
with open("spisok_guest.json", encoding="utf8") as f: #Открываем файл
data = json.load(f) #Получае все данные из файла (вообще все, да)
data["spisok_guest"].append(new_data) #Добавляем данные
with open("spisok_guest.json", "w", encoding="utf8") as outfile: #Открываем файл для записи
json.dump(data, outfile, ensure_ascii=False, indent=2) #Добавляем данные (все, что было ДО добавления данных + добавленные данные)
import os
import calendar
from datetime import datetime
from datetime import timedelta

cal = calendar.Calendar()

def wi_start_date():
    x = input('Начальная дата в формате YYYY.MM.DD\n')
    y = datetime.strptime(x, '%Y.%m.%d')
    return y

def wi_stop_date():
    x = input('Дата окончания в формате YYYY.MM.DD\n')
    y = datetime.strptime(x, '%Y.%m.%d')
    return y

def main():
    month_list = [
        'Январь', 'Февраль', 'Март', 'Апрель',
        'Май', 'Июнь', 'Июль', 'Август',
        'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
        ]
    start = wi_start_date()
    stop = wi_stop_date()
    x = stop - start
    delta_days = x.days
        
    for i in range(delta_days + 1):
        obj = start + timedelta(days = i)
        current_dir = os.getcwd()
        month = month_list[int(obj.strftime('%m')) - 1]
        date_date = obj.strftime('%Y.%m.%d') + '\\' + obj.strftime('%Y.%m.%d') + ' №'
        first_dir = '1.Материалы с геодезических приборов'
        second_dir = '2.Редактируемый формат данных обработки'
        third_dir = '3.Полевые геодезические схемы'
        fourth_dir = '4.Исполнительные геодезические схемы'
        os.makedirs(current_dir + '\\' + month + '\\' + date_date + '\\' + first_dir)
        os.makedirs(current_dir + '\\' + month + '\\' + date_date + '\\' + second_dir)
        os.makedirs(current_dir + '\\' + month + '\\' + date_date + '\\' + third_dir)
        os.makedirs(current_dir + '\\' + month + '\\' + date_date + '\\' + fourth_dir)

main()

# используется для сортировки
from operator import itemgetter


class Comp:
    """Компьютер"""

    def __init__(self, id, proc, ram):
        self.id = id
        self.proc = proc
        self.ram = ram


class Disp:
    """Дисплейный класс"""

    def __init__(self, id, resol, comp_id):
        self.id = id
        self.resol = resol
        self.comp_id = comp_id

class CompDisp:

    def __init__(self, comp_id, disp_id):
        self.disp_id = disp_id
        self.comp_id = comp_id


# Компьютеры
comps = [
    Comp(1, 'intel i7', 64),
    Comp(2, 'amd ryzen 5', 32),
    Comp(3, 'intel i5', 16),

    Comp(11, 'intel i7', 128),
    Comp(22, 'amd ryzen 3', 16),
    Comp(33, 'amd ryzen 5', 16),
]

# Дисплеи
disps = [
    Disp(1, 1080, 1),
    Disp(2, 360, 2),
    Disp(3, 720, 3),
    Disp(4, 1080, 3),
    Disp(5, 2160, 3),
]

comps_disps = [
    CompDisp(1, 1),
    CompDisp(2, 2),
    CompDisp(3, 3),
    CompDisp(3, 4),
    CompDisp(3, 5),

    CompDisp(11, 1),
    CompDisp(22, 2),
    CompDisp(33, 3),
    CompDisp(33, 4),
    CompDisp(33, 5),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(e.resol, e.comp_id, d.proc, d.ram)
                   for d in comps
                   for e in disps
                   if e.comp_id == d.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.proc, d.ram, ed.comp_id, ed.disp_id)
                         for d in comps
                         for ed in comps_disps
                         if d.id == ed.comp_id]

    many_to_many = [(e.resol, e.comp_id, comp_proc, comp_ram)
                    for comp_proc, comp_ram, comp_id, disp_id in many_to_many_temp
                    for e in disps if e.id == disp_id]

    print('Задание B1')

    res_11 =[]
    for i in one_to_many:
        if i[0] > 720:
            res_11.append(i)
    print(res_11)

    print('\nЗадание B2')
    res_12 = []
    for i in comps:
        temp_disp = Disp(0,0,0)
        for j in disps:
            if j.comp_id == i.id and temp_disp.resol == 0 or j.resol < temp_disp.resol:
                temp_disp = j
        if temp_disp.resol != 0:
            res_12.append([i.id, i.proc, i.ram, temp_disp.id, temp_disp.resol])
    print(res_12)
    print('\nЗадание B3')
    res_13 = sorted(many_to_many, key=itemgetter(1))
    print(res_13)

if __name__ == '__main__':
    main()

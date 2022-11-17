# Итератор для удаления дубликатов
class Unique(object):

    def __init__(self, items, **kwargs):
        self.unic = set()
        if kwargs['ignore_case'] == True:
            for elem in items:
                self.unic.add(str(elem).lower())
        else:
            self.unic = set(items)

        self.unic = iter(self.unic)
        pass

    def __next__(self):

        return next(self.unic)

        # Нужно реализовать __next__


    def __iter__(self):
        return self


data = ['A', 'a', 'B', 'b', 'c', 'c']
d = Unique(data, ignore_case=False)

for elem in d:
    print(elem)

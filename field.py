def field(items, *args):
    assert len(args) > 0

    for i in items:
        if len(args) == 1 and args[0] in i:
            print("\'"+ i[args[0]] + "\'", end="")

        else:
            print("{", end="")
            for j in args:
                if j in i:
                    print("\'" + j + "\': " + "\'" + str(i[j]) + "\'", end="")
                    if j != args[len(args) - 1]:
                        print(", ", end="")
            print("}", end="")
        if i != items[len(items) - 1]:
            print(", ", end="")


goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
 ]
field(goods, 'title')
print("")
field(goods, 'title', 'price', 'color')
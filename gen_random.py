import random

def gen_random(num_count, begin, end):
    pass
    arr =[]
    for i in range(num_count):
        arr.append(random.randint(begin, end))
    return arr

print(gen_random(6, -5, 7))
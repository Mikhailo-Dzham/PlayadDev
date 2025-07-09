import random

def haist(start = 10) ->int: #HAlf In STep
    n = start
    while random.randint(0, 1):
        n +=1
    return n

def id_generator():
    with open('last_id.txt', 'r') as f:
        _id = str(format(int(f.read(), 16) + 1, 'x'))
        _id = '0' * (16 - len(_id)) + _id
    with open('last_id.txt', 'w') as f:
        f.write(_id)
    return _id



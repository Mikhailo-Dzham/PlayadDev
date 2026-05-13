import gen_tools as gen
from display_tools import displayer_main

COUNT = 1000_000_0

def gen_base_atribute():
    return tuple([gen.haist() for _ in range(6)])


counter = {}
for i in range(COUNT):
    a = gen_base_atribute()
    if a in counter:
        counter[a] +=1
    else:
        counter[a] = 1

# for key, value in counter.items():
#     print(f"{value} -- {key}")

displayer_main(counter, 10, 0)
print(len(counter))
import gen_tools as gen


counter = {}
for i in range(1000):
    a = gen.haist()
    if a in counter:
        counter[a] +=1
    else:
        counter[a] = 1

for i in range(10, 100):
    if i in counter:
        print(i, ' -- ', counter[i])


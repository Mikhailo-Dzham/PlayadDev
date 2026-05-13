def char_display(data):
    val = data
    print("Сумарні стати: ", sum(val[1::]), "  Талант: ", val[0] / 10)
    print("PWR: ", val[1], "STM: ", val[2], "HP: ", val[3], "INT: ", val[4], "MP: ", val[5])
    print("="*40)

def displayer_main(dictionary, n, atribute = None):
    if atribute is None:
        top_n = sorted(dictionary.items(), key=lambda item: sum(item[0][1::]), reverse=True)[:n]
    else:
        top_n = sorted(dictionary.items(), key=lambda item: item[0][atribute], reverse=True)[:n]

    for key, value in top_n:
        print(f"Тег: {key}, Кількість: {value}")
        char_display(key)
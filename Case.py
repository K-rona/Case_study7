import ru_local as ru


fuel_amount = {}
lost_clients = 0


with open('automats.txt', encoding='utf8') as f_auto:
    dict_queue = {}
    for ptr in f_auto:
        data = ptr.split()
        dict_queue[data[0]] = [(data[1]), data[2:], []]

        for item in data[2:]:
            if item not in fuel_amount:
                fuel_amount[item] = 0

n = len(dict_queue)


with open('input.txt', encoding='utf8') as f_in:
    for new_client in f_in:
        time, volume, brand = new_client.split()
        fuel_amount[brand] += int(volume)

        print(f'{ru.IN} {time} {ru.NEW_CLIENT}: {new_client[:-1]} {ru.GET_IN_LINE}')
        for i in range(n):
            print(f'{ru.AUTOMAT}{i+1} {ru.MAX_QUEUE}{dict_queue[str(n)][0]} {ru.GASOLINE_BRANDS} {dict_queue[str(n)][1]}->')


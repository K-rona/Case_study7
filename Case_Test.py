import Ru_local as ru
import random


fuel_amount = {}
clients = []
lost_clients = 0

brands = ['АИ-80', 'АИ-92', 'АИ-95', 'АИ-98']
fill_amount = random.randint(3, 7)
with open('automats.txt', 'w') as f_write:
    ptr = ''
    for i in range(1, fill_amount + 1):
        line = str(i) + ' ' + str(random.randint(1, 4)) + ' '
        brand_amount = random.randint(1, len(brands))
        for _ in range(brand_amount):
            rand_brand = random.choice(brands)
            if rand_brand not in line:
                line += rand_brand + ' '
        ptr += line + '\n'
    f_write.write(ptr)


with open('automats.txt', 'r') as f_auto:
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

        filling_time = round(int(volume) / 10)
        case = random.randint(-1, 1)
        if filling_time + case > 0:
            filling_time += case
            clients += [time, volume, brand, filling_time]

        min_que = float('inf')
        for i in range(1, fill_amount + 1):
            if brand in dict_queue[str(i)][1]:
                if len(dict_queue[str(i)][2]) < min_que and len(dict_queue[str(i)][2]) < int(dict_queue[str(i)][0]):
                    min_que = len(dict_queue[str(i)][2])

        if min_que == float('inf'):
            print(f'{ru.IN} {time} {ru.NEW_CLIENT}: {new_client} {filling_time} {ru.FILL_FAIL}')
            lost_clients += 1
        else:
            for j in range(1, fill_amount + 1):
                if brand in dict_queue[str(j)][1]:
                    if len(dict_queue[str(j)][2]) == min_que and len(dict_queue[str(j)][2]) < int(dict_queue[str(j)][0]):
                        fill_number = j
                        dict_queue[str(j)][2] += ['*']
                        print(f'{ru.IN} {time} {ru.NEW_CLIENT}: {new_client} {filling_time} {ru.GET_IN_LINE} {fill_number}')
                        break

        for k in range(1, fill_amount + 1):
            print(f'{ru.AUTOMAT}{k} {ru.MAX_QUEUE} {dict_queue[str(k)][0]} {ru.GASOLINE_BRANDS} {dict_queue[str(k)][1]}->{dict_queue[str(k)][2]}')

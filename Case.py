import ru_local as ru
import random
import math


def status_now(diveces, all_time):
    """
    Get status of gas station
    :param diveces: old dictionary with queue data
    :param all_time: passed time
    :return: updated queue dictionary
    """

    for i in range(1, n + 1):
        x = 0
        len_array = len(diveces[str(i)][3])

        while x < len_array:
            if len(diveces[str(i)][3][x]) > 0:
                time_end = diveces[str(i)][3][x][4] + diveces[str(i)][3][x][3]

                if time_end < all_time:
                    hours = str(time_end // 60)
                    minutes = str(time_end - int(hours) * 60)

                    if len(hours) < 2:
                        hours = '0' + hours
                    if len(minutes) < 2:
                        minutes = '0' + minutes

                    print(f'{ru.IN} {hours}:{minutes} {ru.CLIENT} {diveces[str(i)][3][x][0]} '
                          f'{diveces[str(i)][3][x][2]} {diveces[str(i)][3][x][1]} {ru.FILL_LUCK}')

                    diveces[str(i)][3].pop(x)
                    diveces[str(i)][2].pop(x)
                    len_array -= 1
                    x -= 1

                    for m in range(1, n + 1):
                        print(f'{ru.AUTOMAT}{m} {ru.MAX_QUEUE} {diveces[str(m)][0]} {ru.GASOLINE_BRANDS}',
                              ' '.join(diveces[str(m)][1]), '->', *diveces[str(m)][2], sep='')
            x += 1

    return diveces


if __name__ == '__main__':
    brands = ['АИ-80', 'АИ-92', 'АИ-95', 'АИ-98']
    fuel_price = {'АИ-80': 42, 'АИ-92': 51, 'АИ-95': 55, 'АИ-98': 65}

    fuel_amount = {}
    clients = []
    lost_clients = 0
    total_time = 0
    revenue = 0

    with open('automats.txt', 'r', encoding='utf8') as f_auto:
        dict_queue = {}

        for ptr in f_auto:
            data = ptr.split()
            dict_queue[data[0]] = [(data[1]), data[2:], [], []]

            for item in data[2:]:
                if item not in fuel_amount:
                    fuel_amount[item] = 0

    n = len(dict_queue)

    with open('input.txt', encoding='utf8') as f_in:
        for new_client in f_in:
            time, volume, brand = new_client.split()
            volume = int(volume)
            time_in_minutes = int(time[:2]) * 60 + int(time[3:])
            total_time += time_in_minutes - total_time

            if brand in fuel_amount:
                fuel_amount[brand] += volume
                revenue += volume * fuel_price[brand]

            filling_time = math.ceil(int(volume) / 10)
            case = random.randint(-1, 1)

            if filling_time + case > 0:
                filling_time += case

            clients = [time, volume, brand, filling_time, time_in_minutes]

            dict_queue = status_now(dict_queue, total_time)

            min_que = float('inf')
            for p in range(1, n + 1):
                if brand in dict_queue[str(p)][1]:
                    if len(dict_queue[str(p)][2]) < min_que and len(dict_queue[str(p)][2]) < int(dict_queue[str(p)][0]):
                        min_que = len(dict_queue[str(p)][2])

            if min_que == float('inf'):
                print(f'{ru.IN} {time} {ru.NEW_CLIENT}: {new_client[:-1]} {filling_time} {ru.FILL_FAIL}')
                lost_clients += 1
                fuel_amount[brand] -= volume
            else:
                for key, values in dict_queue.items():
                    if brand in values[1] and len(values[2]) == min_que and len(values[2]) < int(values[0]):
                        fill_number = key
                dict_queue[fill_number][2] += ['*']
                dict_queue[fill_number][3] += [clients]

                print(f'{ru.IN} {time} {ru.NEW_CLIENT}: {new_client[:-1]}'
                      f' {filling_time} {ru.GET_IN_LINE} {fill_number}')

            for k in range(1, n + 1):
                print(f'{ru.AUTOMAT}{k} {ru.MAX_QUEUE} {dict_queue[str(k)][0]} {ru.GASOLINE_BRANDS}',
                      ' '.join(dict_queue[str(k)][1]), '->', *dict_queue[str(k)][2], sep='')

        print()

        for t in brands:
            print(f'{ru.SOLD} {fuel_amount[t]} {ru.LITERS} {t}')
        print(f'{ru.TOTAL_REVENUE} {revenue} {ru.RUBLES}')
        print(f'{ru.MISSED} {lost_clients}')

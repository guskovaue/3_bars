import json


def load_data(filepath):
    with open(filepath, 'r') as file:
        return json.loads(file.read())


def get_name_size_dict(data):
    bar_size_dict = {}
    for bar_info in data['features']:
        bar_size_dict[bar_info['properties']['Attributes']['Name']] = bar_info['properties']['Attributes']['SeatsCount']
    return bar_size_dict


def get_biggest_bar(data):
    bar_size_dict = get_name_size_dict(data)
    biggest_size = max(bar_size_dict.values())
    biggest_size_bars = []
    for key, value in bar_size_dict.items():
        if value == biggest_size:
            biggest_size_bars.append(key)
    print('-----')
    if len(biggest_size_bars) == 1:
        print("Самый маленький бар Москвы - это {}".format(biggest_size_bars[0]))
    else:
        structure = ', '.join(list(map(lambda x: str(x), biggest_size_bars)))
        print("Первое место на звание самого маленького бара Москвы разделили: {}".format(structure))


def get_smallest_bar(data):
    bar_size_dict = get_name_size_dict(data)
    smallest_size = min(bar_size_dict.values())
    smallest_size_bars = []
    for key, value in bar_size_dict.items():
        if value == smallest_size:
            smallest_size_bars.append(key)
    print('-----')
    if len(smallest_size_bars) == 1:
        print("Самый большой бар Москвы - это {}".format(smallest_size_bars[0]))
    else:
        structure = ', '.join(list(map(lambda x: str(x), smallest_size_bars)))
        print("Первое место на звание самого большого бара Москвы разделили: {}".format(structure))


def get_closest_bar(data, x1, y1):
    min_distance = -1
    closest_bar = ''
    for bar_info in data['features']:
        x2 = bar_info['geometry']['coordinates'][0]
        y2 = bar_info['geometry']['coordinates'][1]
        distance = pow((x1 - x2) ** 2 + (y1 - y2) ** 2, 0.5)
        if distance < min_distance or min_distance == -1:
            min_distance = distance
            closest_bar = bar_info['properties']['Attributes']['Name']
    print("Ближайший к вам бар - {}".format(closest_bar))

if __name__ == '__main__':
    info = load_data('file.txt')
    get_biggest_bar(info)
    get_smallest_bar(info)

    print('-----')
    print('Введите свои координаты. Используйте в качестве десятичного разделителя точку: 41.40338')
    while True:
        try:
            longitude = float(input('Широта:'))
            latitude = float(input('Долгота:'))
        except TypeError:
            print("Координаты введены не в корректной форме. Используйте в качестве десятичного разделителя точку")
        else:
            get_closest_bar(info, longitude, latitude)
            break
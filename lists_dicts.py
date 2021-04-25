def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {'firstname': 'Alexander', 'lastname': 'Sánchez'}

    super_list = [
        {'firstname': 'Alexander', 'lastname': 'Sánchez'},
        {'firstname': 'Joel', 'lastname': 'Narváez'}
    ]

    super_dict = {
        'natural_nums': [1, 2, 3, 4, 5],
        'integer_nums': [-2, -1, 0, 1, 2],
        'floating_nums': [1.1, 7.7, 3.4]
    }

    for key, value in super_dict.items():
        print(key, '-', value)

    for list in super_list:
        for key, value in list.items():
            print(f'{key} : {value}')


if __name__ == '__main__':
    run()

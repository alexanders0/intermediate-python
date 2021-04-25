DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():

    ''' 1. Get all workers that programming in Python '''

    # List Comprehensions
    all_python_devs = [
        worker['name'] for worker in DATA if worker['language'] == 'python'
    ]

    # High order functions
    all_python_devs = list(
        filter(lambda worker: worker['language'] == 'python', DATA)
    )

    all_python_devs = list(
        map(lambda worker: worker['name'], all_python_devs)
    )

    print(f'Python devs: {all_python_devs}')

    ''' 2. Get all workers filtered by organization '''

    # List Comprehensions
    all_platzi_workers = [
        worker['name'] for worker in DATA if worker['organization'] == 'Platzi'
    ]

    # High order functions
    all_platzi_workers = list(
        filter(lambda worker: worker['organization'] == 'Platzi', DATA)
    )

    all_platzi_workers = list(
        map(lambda worker: worker['name'], all_platzi_workers)
    )

    print(f'Platzi workers: {all_platzi_workers}')

    ''' 3. Get all adult workers '''

    # High order functions
    adults = list(filter(lambda worker: worker['age'] > 18, DATA))
    adults = list(map(lambda worker: worker['name'], adults))

    # List Comprehensions
    adults = [worker['name'] for worker in DATA if worker['age'] > 18]

    print(f'Adults: {adults}')

    '''
    4. Add -old- key to each worker with True or False according to their age
    '''

    # High order functions
    # With pipe | we could add two dictionaries
    old_people = list(
        map(lambda worker: worker | {'old': worker['age'] > 70}, DATA)
    )

    # List Comprenhension
    old_people = [worker | {'old': worker['age'] > 70} for worker in DATA]

    print(f'Old people: {old_people}')


if __name__ == '__main__':
    run()

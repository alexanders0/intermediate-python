def run():

    '''
    1. Sample: Dictionary with:
    keys: 100 first natural numbers
    values: numbers to the power of 3, and non-divisible of 3
    '''

    # Without dict comprehensions
    dict = {}
    for i in range(1, 101):
        if i % 3 != 0:
            dict[i] = i**3

    # Dict comprehensions
    dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    print(dict)

    '''
    2. Challenge: dict comprehension with:
    keys: 1000 first natural numbers
    values: square root of the numbers
    '''
    square_roots = {i: round(i**0.5, 2) for i in range(1, 1001)}
    print(square_roots)


if __name__ == '__main__':
    run()

def run():

    '''
    1. Sample: List with squares of non-divisible numbers of 3
    '''

    # Without list comprehensions
    squares = []

    for i in range(1, 101):
        if i % 3 != 0:
            squares.append(i**2)

    # List comprehensions
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    print(squares)

    '''
    2. Challenge: list comprehension with multiples of 4, 6 and 9
    until 5 digits
    '''
    list = [
        i
        for i in range(1, 10000)
        if i % 4 == 0 and i % 6 == 0 and i % 9 == 0
    ]
    print(list)


if __name__ == '__main__':
    run()

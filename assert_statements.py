def divisors(num):
    return [i for i in range(1, num + 1) if num % i == 0]


def run():
    while(True):
        num = input('Enter a number: ')
        assert num.strip('-').isnumeric(), 'You must enter a number'
        assert int(num) > 0, 'You must enter a positive number'
        print(divisors(int(num)))
        print('Program ends')
        break


if __name__ == '__main__':
    run()

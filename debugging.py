def divisors(num):
    return [i for i in range(1, num + 1) if num % i == 0]


def run():
    while(True):
        try:
            num = int(input('Enter a number: '))
            if num <= 0:
                raise Exception
            print(divisors(num))
            print('Program ends')
            break
        except ValueError:
            print('You must enter a number')
        except Exception:
            print('Enter a positive number')


if __name__ == '__main__':
    run()

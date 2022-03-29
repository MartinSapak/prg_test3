def is_whole_number(number):
    if number % 1 == 0:
        return True
    else:
        return False

def is_natural_nuber(number):
    if number % 1 == 0 and number > 0:
        return True
    else:
        return False

def is_even_number(number):
    if number % 2 == 0:
        return True
    else:
        return False

def main():
    my_number = -2
    result_whole = is_whole_number(my_number)
    print(f'Is whole number: {result_whole}')
    result_natural = is_natural_nuber(my_number)
    print(f'Is natural number: {result_natural}')
    result_even = is_even_number(my_number)
    print(f'Is even number: {result_even}')

if __name__ == '__main__':
    main()
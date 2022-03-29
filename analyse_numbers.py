def is_whole_number(number):
    list_of_results_whole = []
    for i in number:
        if i % 1 == 0:
            result = [i, True]
            list_of_results_whole.append(result)
        else:
            result = [i, False]
            list_of_results_whole.append(result)
    return list_of_results_whole

def is_natural_nuber(number):
    list_of_results_natural = []
    for i in number:
        if i % 1 == 0 and i > 0:
            result = [i, True]
            list_of_results_natural.append(result)
        else:
            result = [i, False]
            list_of_results_natural.append(result)
    return list_of_results_natural

def is_even_number(number):
    list_of_results_even = []
    for i in number:
        if i % 2 == 0:
            result = [i, True]
            list_of_results_even.append(result)
        else:
            result = [i, False]
            list_of_results_even.append(result)
    return list_of_results_even

def main():
    my_number = -2
    my_numbers_list = [1, 2, 3, 5]
    result_whole = is_whole_number(my_numbers_list)
    print(f'Is whole number: {result_whole}')
    result_natural = is_natural_nuber(my_numbers_list)
    print(f'Is natural number: {result_natural}')
    result_even = is_even_number(my_numbers_list)
    print(f'Is even number: {result_even}')

if __name__ == '__main__':
    main()
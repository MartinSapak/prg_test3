def is_even_number(number):
    list_of_results = []
    for i in number:
        if i % 2 == 0:
            result = [i, True]
            list_of_results.append(result)
        else:
            result = [i, False]
            list_of_results.append(result)
    return  list_of_results

def main():
    my_list_of_numbers = [1, 2, 3, 5]
    result_even = is_even_number(my_list_of_numbers)
    print(f'Is even number: {result_even}')

if __name__ == '__main__':
    main()
def is_whole_number(number):
    if number % 1 == 0:
        return True
    else:
        return False

def main():
    my_number = 2
    result = is_whole_number(my_number)
    print(result)

if __name__ == '__main__':
    main()
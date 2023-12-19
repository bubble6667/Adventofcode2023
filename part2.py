def get_int_with_string(string):

    match string:
        case 'one':
            result = 1
        case 'two':
            result = 2
        case 'three':
            result = 3
        case 'four':
            result = 4
        case 'five':
            result = 5
        case 'six':
            result = 6
        case 'seven':
            result = 7
        case 'eight':
            result = 8
        case 'nine':
            result = 9

    return result


def find_first(list, string):
    result = ''
    for x in range(len(string)):
        if result != '':
            break
        for items in list:
            if str(items).isdigit():
                if string[x].isnumeric():
                    if items == int(string[x]):
                        result = items
                        break
            else:
                for y in range(len(items)):
                    if items[y] == string[x + y]:
                        if y + 1 == len(items):
                            result = get_int_with_string(items)
                            break
                    else:
                        break
    return result


def find_last(list, string):
    result = ''
    for x in range(len(string)):
        if result != '':
            break
        for items in list:
            if str(items).isdigit():
                if string[(len(string) - 1 - x)].isnumeric():
                    if items == int(string[(len(string) - 1 - x)]):
                        result = items
                        break
            else:
                for y in range(len(items)):
                    if items[(len(items) - 1 - y)] == string[(len(string) - 1 - x - y)]:
                        if y + 1 == len(items):
                            result = get_int_with_string(items)
                            break
                    else:
                        break
    return result


def digitizer(list, string):

    int1 = find_first(list, string)
    int2 = find_last(list, string)

    result = str(int1) + str(int2)

    return int(result)


def decode(message_file):
    list_int2 = []
    with open(message_file, 'r') as f:
        string = f.read()
        list_str = string.splitlines()
        number_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        for strings in list_str:
            list_int = []
            for i in range(len(strings)):
                try:
                    if strings[i].isnumeric():
                        print('test')
                        list_int.append(int(strings[i]))
                        break
                except ValueError as e:
                    print(e)
            for x in range(len(strings)):
                try:
                    if strings[(len(strings) - x - 1)].isnumeric():
                        print('test2')
                        list_int.append(int(strings[(len(strings) - x - 1)]))
                        break
                except ValueError as e:
                    print(e)
            for items in number_list:
                if items in strings:
                    list_int.append(items)
            print(list_int)
            list_int2.append(digitizer(list_int, strings))

        return list_int2


if __name__ == '__main__':

    print(sum(decode('input.txt')))

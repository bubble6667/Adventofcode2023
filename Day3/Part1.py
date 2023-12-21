parts_set = []


def get_numeric_char(string, col):

    col_list = []
    x = 0
    while x < len(string):
        if string[x].isnumeric():
            start_pos = x
            lenght_char = 1
            x += 1
            try:
                if string[x].isnumeric():
                    lenght_char += 1
                    x += 1
            except IndexError as e:
                print(e)
            try:
                if string[x].isnumeric():
                    lenght_char += 1
                    x += 1
            except IndexError as e:
                print(e)
            try:
                if string[x].isnumeric():
                    lenght_char += 1
                    x += 1
            except IndexError as e:
                print(e)
            col_list.append([col, start_pos, lenght_char])
            x += 1
        else:
            x += 1
    if len(col_list) == 0:
        return None
    else:
        return col_list


def get_numbers_list(game_list):

    numbers_list = []
    col = 0
    for items in game_list:
        temp_list = get_numeric_char(items, col)
        if temp_list is not None:
            numbers_list.append(temp_list)
        col += 1
    return numbers_list


def check_right(part_maps, strings):

    if (part_maps[1] + part_maps[2]) < len(strings):
        if strings[(part_maps[1] + part_maps[2])] == '.':
            return False
        else:
            return True
    elif (part_maps[1] + part_maps[2]) == len(strings):
        return False


def check_left(part_maps, strings):

    if strings[(part_maps[1] - 1)] == '.':
        return False
    else:
        return True


def check_sides(part_maps, strings):
    if part_maps[1] == 0:
        if check_right(part_maps, strings):
            return True
        else:
            return False
    elif (int(part_maps[1]) + int(part_maps[2])) == (len(strings) - 1):
        if check_left(part_maps, strings):
            return True
        else:
            return False
    else:
        if check_right(part_maps, strings) or check_left(part_maps, strings):
            return True
        else:
            return False


def check_bellow_above(part_maps, strings):
    result = False
    x = 0
    if part_maps[1] == 0:
        for x in range(part_maps[1], (part_maps[2] + 2)):
            if strings[x].isnumeric():
                pass
            elif strings[x] == '.':
                pass
            else:
                result = True
    elif (part_maps[1] + part_maps[2]) >= (len(strings) - 1):
        for x in range((part_maps[1] - 1), (part_maps[1] + part_maps[2])):
            if strings[x].isnumeric():
                pass
            elif strings[x] == '.':
                pass
            else:
                result = True
    else:
        for x in range((part_maps[1] - 1), (part_maps[2] + part_maps[1] + 1)):
            if part_maps[0] == 20:
                print(str(len(strings) - 1))
                print(part_maps)
                print(x)
                print(strings[x])
            if strings[x].isnumeric():
                pass
            elif strings[x] == '.':
                pass
            else:
                result = True
    return result


def is_part_number(part_map, game_lists):

    if part_map[0] == 0:
        if check_sides(part_map, game_lists[part_map[0]]) or check_bellow_above(part_map, game_lists[(part_map[0] + 1)]):
            print(part_map)
            parts_set.append(part_map)
    elif part_map[0] == (len(game_lists) - 1):
        if check_sides(part_map, game_lists[part_map[0]]) or check_bellow_above(part_map, game_lists[(part_map[0] - 1)]):
            print(part_map)
            parts_set.append(part_map)
    else:
        if check_sides(part_map, game_lists[part_map[0]]) or check_bellow_above(part_map, game_lists[(part_map[0] + 1)]) or check_bellow_above(part_map, game_lists[(part_map[0] - 1)]):
            print(part_map)
            parts_set.append(part_map)


def get_part_number(part_list, game_lists):
    str_temps = ''
    for x in range(part_list[1], (part_list[1] + part_list[2])):
        str_temps = str_temps + game_lists[(part_list[0])][x]
    print(str_temps)
    return int(str_temps)


if __name__ == '__main__':
    result_list = []
    with open('input.txt', 'r') as f:
        tlist = f.read()
        f.close()
    print(tlist)
    game_list = tlist.splitlines()
    item_list = get_numbers_list(game_list)
    for col in item_list:
        for items in col:
            is_part_number(items, game_list)

    for itemss in parts_set:
        print(itemss)
        result_list.append(get_part_number(itemss, game_list))
    print(sum(result_list))

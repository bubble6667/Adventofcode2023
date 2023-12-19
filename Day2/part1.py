def get_game_items(string):
    result = True
    str_list = string.split('; ')
    for items in str_list:
        game_list = items.split(', ')
        for colors in game_list:
            if 'red' in colors:
                color_value = colors.split(' ')
                if int(color_value[0]) > 12:
                    result = False
            elif 'green' in colors:
                color_value = colors.split(' ')
                if int(color_value[0]) > 13:
                    result = False
            elif 'blue' in colors:
                color_value = colors.split(' ')
                if int(color_value[0]) > 14:
                    result = False
    return result


def get_result(list):

    total = 0
    for strings in list:
        if strings[7] == '0':
            index = 100
            game_string = strings
            game_string = game_string.replace("Game 100: ", '')
            result = get_game_items(game_string)
            if result:
                total += index
        elif strings[6].isnumeric():
            index = int(str(strings[5]) + str(strings[6]))
            game_string = strings
            game_string = game_string.replace("Game " + str(index) + ": ", '')
            result = get_game_items(game_string)
            if result:
                total += index
        else:
            index = int(strings[5])
            game_string = strings
            game_string = game_string.replace("Game " + str(index) + ": ", '')
            result = get_game_items(game_string)
            if result:
                total += index
    return total


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        tempstring = f.read()
        f.close()

    list_string = tempstring.splitlines()
    print(list_string)
    print(get_result(list_string))

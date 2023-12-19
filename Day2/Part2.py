def get_game_items(string):
    result = 0
    max_red = 0
    max_green = 0
    max_blue = 0
    str_list = string.split('; ')
    for items in str_list:
        game_list = items.split(', ')
        for colors in game_list:
            if 'red' in colors:
                color_value = colors.split(' ')
                if int(color_value[0]) > max_red:
                    max_red = int(color_value[0])
            elif 'green' in colors:
                color_value = colors.split(' ')
                if int(color_value[0]) > max_green:
                    max_green = int(color_value[0])
            elif 'blue' in colors:
                color_value = colors.split(' ')
                if int(color_value[0]) > max_blue:
                    max_blue = int(color_value[0])
    return max_blue * max_red * max_green


def get_result(list):

    total = 0
    for strings in list:
        if strings[7] == '0':
            index = 100
            game_string = strings
            game_string = game_string.replace("Game 100: ", '')
            result = get_game_items(game_string)
            total += result
        elif strings[6].isnumeric():
            index = int(str(strings[5]) + str(strings[6]))
            game_string = strings
            game_string = game_string.replace("Game " + str(index) + ": ", '')
            result = get_game_items(game_string)
            total += result
        else:
            index = int(strings[5])
            game_string = strings
            game_string = game_string.replace("Game " + str(index) + ": ", '')
            result = get_game_items(game_string)
            total += result
    return total


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        tempstring = f.read()
        f.close()

    list_string = tempstring.splitlines()
    print(list_string)
    print(get_result(list_string))
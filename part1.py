import socket


def decode(message_file):

    with open(message_file, 'r') as f:
        string = f.read()
        list_str = string.splitlines()
        int1 = 0
        int2 = 0
        list_int = []
        for strings in list_str:
            for i in range(len(strings)):
                try:
                    if strings[i].isnumeric():
                        print('test')
                        int1 = int(strings[i])
                        break
                except socket.error as e:
                    print(e)
            for x in range(len(strings)):
                try:
                    if strings[(len(strings) - x - 1)].isnumeric():
                        print('test2')
                        int2 = int(strings[(len(strings) - x - 1)])
                        break
                except  socket.error  as e:
                    print(e)
            print(str(int1) + ' ' + str(int2))
            tempstr = str(int1) + str(int2)
            list_int.append(int(tempstr))
        return sum(list_int)


if __name__ == '__main__':

    print(decode('testDay1.txt'))

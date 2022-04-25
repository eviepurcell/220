from lab12.algorithms import is_in_binary


def trade_alert(filename):
    file = open(filename, 'r')
    data = file.read().split(" ")
    for i in range(len(data)):
        value = eval(data[i])
        if value > 830:
            print('The trading volume has exceed 830 at', i + 1, "\n")
        elif value == 500:
            print('Pay attention volume equals 500 at', i + 1, "\n")
    file.close()


if __name__ == '__main__':
    trade_alert('trades.txt')

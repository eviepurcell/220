def find_and_remove_first(list, value):
    i = 0
    while i < len(list):
        if value == list[i]:
            list.pop(i)
            list.insert(i, "evie")
            i = len(list)
        i = i + 1


if __name__ == '__main__':
    list = ['Red', 'Blue', 'Orange', 'Gray', 'White']
    print(list)
    find_and_remove_first(list, 'Orange')
    print(list)

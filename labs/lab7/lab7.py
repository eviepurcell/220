def weighted_average(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")
    lines = in_file.readlines()
    class_average = 0
    valid_count = 0
    for line in lines:
        split_line = line.split(": ")
        name = split_line[0]
        grades = split_line[1]
        grades = grades.split(" ")
        total = 0
        my_sum = 0
        for i in range(0, len(grades), 2):
            total += (int(grades[i]) * int(grades[i+1]))
            my_sum += int(grades[i])
        average = (total / 100)
        if my_sum == 100:
            print(name+"'s average: ", average, file = out_file)
            class_average += average
            valid_count += 1
        elif my_sum < 100:
            print(name+"'s average: Error: The weights are less than 100.", file = out_file)
        else:
            print(name+"'s average: Error: The weights are more than 100.", file = out_file)
    print("Class average: ", class_average / valid_count, file = out_file)




if __name__ == '__main__':
    weighted_average("grades.txt", "avg.txt")

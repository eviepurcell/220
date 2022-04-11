from encryption import encode
from encryption import encode_better
def number_words(in_file_name, out_file_name):
    word = open(in_file_name)
    text = word.read()
    outfile = open(out_file_name, "a")
    seperate = text.split()
    counter = 1
    for i in seperate:
        outfile.write(str(counter) + "" + i + "\n")
        counter = counter + 1
    word.close()
    outfile.close()

def hourly_wage(in_file_name, out_file_name):
    input_file = open(in_file_name)
    output_file = open(out_file_name, "a")
    read_file = input_file.read()
    mes = read_file.split("\n")
    for line in mes:
        line_split = line.split()
        wage = eval(line_split[2])
        hours = eval(line_split[3])
        pay = (wages + hours) + (1.65 + hours)
        output_file.write(line.split[0] + ' ' + line_split[1] + ' ' + pay)

    input_file.close()
    output_file.close()

def calc_check_sus(isbn):
    pass

def send_message(file_name, friend_name):
    open_file = open(file_name, "r")
    name = open_file.read()
    new_file = open(friend_name + ".txt", "a")
    new_file.write(name)

    open_file.close()
    new_file.close()

def send_uncrackable_message(file_name, friend_name, pad_file_name):
    file = open(file_name)
    text = file.read()
    key_file = open(pad_file_name)
    key = key_file.read()
    text = text.split("\n")
    for message in text:
        words = message.split()
        sentence = ""
        for i in words:
            encode_better(i, key, "friend_name.txt")

if __name__ == '__main__':
    number_words("pad.txt", "Sammy.txt")
    hourly_wage("pad.txt", "Sammy.txt")
    calc_check_sum("0-072-94652-0")
    send_message("pad.txt", "Sammy")
    send_safe_message("pad.txt", "Sammy", 4)
    send_uncrackable_message("pad.txt", "Sammy")

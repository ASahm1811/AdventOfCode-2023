from main import file

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

sum_numbers = 0

for line in file.readlines():
    chosen_number = ""

    # digits
    first_digit = ""
    last_digit = ""
    first_digit_found = False
    index_first_digit = 1000
    index_last_digit = -1000
    for i in range(len(line)):
        # first digit
        if line[i] in numbers and not first_digit_found:
            # print("first digit: {}".format(line[i]))
            first_digit = line[i]
            first_digit_found = True
            index_first_digit = i
        # last digit
        if line[i] in numbers and first_digit_found:
            # print("last digit: {}".format(line[i]))
            last_digit = line[i]
            index_last_digit = i

    print("<first digit index: {}".format(index_first_digit))
    print("last digit index: {}>".format(index_last_digit))
    print("digit number: {}{} >".format(first_digit, last_digit))

    # letters
    first_letter = ""
    last_letter = ""
    first_letter_found = False
    index_first_letter = 1000
    index_last_letter = -1000
    for j in range((len(line) - 3)+1):
        # first letter
        if line[j:j + 3] == "zer" and not first_letter_found:
            # print("first letter: {}".format("0"))
            first_letter = "0"
            first_letter_found = True
            index_first_letter = j
        if line[j:j + 3] == 'one' and not first_letter_found:
            # print("first letter: {}".format("1"))
            first_letter = "1"
            first_letter_found = True
            index_first_letter = j
        if line[j:j + 3] == "two" and not first_letter_found:
            # print("first letter: {}".format("2"))
            first_letter = "2"
            first_letter_found = True
            index_first_letter = j
        if line[j:j + 4] == "thre" and not first_letter_found:
            # print("first letter: {}".format("3"))
            first_letter = "3"
            first_letter_found = True
            index_first_letter = j
        if line[j:j + 3] == "fou" and not first_letter_found:
            # print("first letter: {}".format("4"))
            first_letter = "4"
            first_letter_found = True
            index_first_letter = j
        if line[j:j + 3] == "fiv" and not first_letter_found:
            # print("first letter: {}".format("5"))
            first_letter = "5"
            first_letter_found = True
            index_first_letter = j
        if line[j:j + 3] == "six" and not first_letter_found:
            # print("first letter: {}".format("6"))
            first_letter = "6"
            first_letter_found = True
            index_first_letter = j
        if line[j:j + 3] == "sev" and not first_letter_found:
            # print("first letter: {}".format("7"))
            first_letter = "7"
            first_letter_found = True
            index_first_letter = j
        if line[j:j + 3] == "eig" and not first_letter_found:
            # print("first letter: {}".format("8"))
            first_letter = "8"
            first_letter_found = True
            index_first_letter = j
        if line[j:j + 3] == "nin" and not first_letter_found:
            # print("first letter: {}".format("9"))
            first_letter = "9"
            first_letter_found = True
            index_first_letter = j

        # last letter
        if line[j:j + 3] == "zer" and first_letter_found:
            # print("last letter: {}".format("0"))
            last_letter = "0"
            index_last_letter = j
        if line[j:j + 3] == "one" and first_letter_found:
            # print("last letter: {}".format("1"))
            last_letter = "1"
            index_last_letter = j
        if line[j:j + 3] == "two" and first_letter_found:
            # print("last letter: {}".format("2"))
            last_letter = "2"
            index_last_letter = j
        if line[j:j + 4] == "thre" and first_letter_found:
            # print("last letter: {}".format("3"))
            last_letter = "3"
            index_last_letter = j
        if line[j:j + 3] == "fou" and first_letter_found:
            # print("last letter: {}".format("4"))
            last_letter = "4"
            index_last_letter = j
        if line[j:j + 3] == "fiv" and first_letter_found:
            # print("last letter: {}".format("5"))
            last_letter = "5"
            index_last_letter = j
        if line[j:j + 3] == "six" and first_letter_found:
            # print("last letter: {}".format("6"))
            last_letter = "6"
            index_last_letter = j
        if line[j:j + 3] == "sev" and first_letter_found:
            # print("last letter: {}".format("7"))
            last_letter = "7"
            index_last_letter = j
        if line[j:j + 3] == "eig" and first_letter_found:
            # print("last letter: {}".format("8"))
            last_letter = "8"
            index_last_letter = j
        if line[j:j + 3] == "nin" and first_letter_found:
            # print("last letter: {}".format("9"))
            last_letter = "9"
            index_last_letter = j

    print("\n<first letter index: {}".format(index_first_letter))
    print("last letter index: {}>".format(index_last_letter))
    print("letter number: {}{}".format(first_letter, last_letter))

    # choose number per line
    if index_first_digit <= index_first_letter:
        chosen_number = chosen_number + first_digit
    elif index_first_letter <= index_first_digit:
        chosen_number = chosen_number + first_letter
    if index_last_digit >= index_last_letter:
        chosen_number = chosen_number + last_digit
    elif index_last_letter >= index_last_digit:
        chosen_number = chosen_number + last_letter

    print("\n** Number: {} **\n".format(chosen_number))
    sum_numbers = sum_numbers + int(chosen_number)

print("Sum: {}".format(sum_numbers))

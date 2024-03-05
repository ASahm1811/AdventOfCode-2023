from main import lines


def calc():
    sum_results = 0
    for step in lines[0].split(','):
        current_value = 0
        for char in step:
            current_value = current_value + ord(char)
            current_value = current_value * 17
            current_value = current_value % 256
        sum_results = sum_results + current_value

    return sum_results

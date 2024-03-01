from main import lines

# found_numbers = []
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sum_numbers = 0

i = 0
while i < len(lines):
    lines[i] = '.' + lines[i].strip() + '.'
    i = i + 1

lines.insert(0, len(lines[0]) * '.')
lines.append(len(lines[0]) * '.')

dict_coord = {}
# dict_coord["100"] = [0,1]
i = 1
while i < len(lines) - 1:
    number_string = ""
    numberFound = False
    negativeFound = False

    j = 1
    while j < len(lines[i]) - 1:
        if lines[i][j] in numbers:
            number_string = number_string + lines[i][j]

        if (lines[i][j] in numbers and
                lines[i][j - 1] == "*"):
            dict_coord["default"] = [i, j - 1]
            numberFound = True
        if (lines[i][j] in numbers and
                lines[i - 1][j - 1] == "*"):
            dict_coord["default"] = [i - 1, j - 1]
            numberFound = True
        if (lines[i][j] in numbers and
                lines[i - 1][j] == "*"):
            dict_coord["default"] = [i - 1, j]
            numberFound = True
        if (lines[i][j] in numbers and
                lines[i - 1][j + 1] == "*"):
            dict_coord["default"] = [i - 1, j + 1]
            numberFound = True
        if (lines[i][j] in numbers and
                lines[i][j + 1] == "*"):
            dict_coord["default"] = [i, j + 1]
            numberFound = True
        if (lines[i][j] in numbers and
                lines[i + 1][j + 1] == "*"):
            dict_coord["default"] = [i + 1, j + 1]
            numberFound = True
        if (lines[i][j] in numbers and
                lines[i + 1][j] == "*"):
            dict_coord["default"] = [i + 1, j]
            numberFound = True
        if (lines[i][j] in numbers and
                lines[i + 1][j - 1] == "*"):
            dict_coord["default"] = [i + 1, j - 1]
            numberFound = True

        if lines[i][j] not in numbers:
            if numberFound:
                print(str(i) + ':', number_string, numberFound)
                dict_coord[number_string] = dict_coord.pop("default")
            number_string = ""
            numberFound = False

        j = j + 1

    i = i + 1

print(dict_coord)

nrs = []
coords = []

for n in dict_coord:
    nrs.append(n)
    coords.append(dict_coord[n])

print(nrs)
print(coords)

sum_gears = 0

i, j = 0, 1
while i < len(coords):
    while j < len(coords):
        if coords[i] == coords[j]:
            print(coords[i], coords[j])
            sum_gears = sum_gears + (int(nrs[i]) * int(nrs[j]))
        j = j + 1
    i = i + 1
    j = i + 1

print("Sum: ", sum_gears)

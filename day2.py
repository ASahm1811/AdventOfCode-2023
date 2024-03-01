from main import file

sum_power = 0

max_red = 0
max_green = 0
max_blue = 0

for line in file.readlines():
    print(line.split(": ")[0])
    # passed = True

    for subset in line.split(": ")[1].split("; "):
        for s in subset.split(", "):
            # print(s.split(" "))
            if (s.split(" ")[1].strip() == "red" and int(s.split(" ")[0]) >
                    max_red):
                max_red = int(s.split(" ")[0])
            if (s.split(" ")[1].strip() == "green" and int(s.split(" ")[0]) >
                    max_green):
                max_green = int(s.split(" ")[0])
            if (s.split(" ")[1].strip() == "blue" and int(s.split(" ")[0]) >
                    max_blue):
                max_blue = int(s.split(" ")[0])

    sum_power = sum_power + (max_red * max_green * max_blue)
    max_red = 0
    max_green = 0
    max_blue = 0

print(sum_power)

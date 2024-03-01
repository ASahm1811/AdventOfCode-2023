from main import lines
import math

seeds = []
seed2soil = {0: 0}
soil2fert = {0: 0}
fert2wat = {0: 0}
wat2light = {0: 0}
light2temp = {0: 0}
temp2hum = {0: 0}
hum2loc = {0: 0}
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def map_func(d, s, size, mapf):
    for i in range(size):
        mapf[s] = d
        s += 1
        d += 1

    for i in range(100):
        if i not in mapf.keys():
            mapf[i] = i


def fill_map():
    do_seed2soil = False
    do_soil2fert = False
    do_fert2wat = False
    do_wat2light = False
    do_light2temp = False
    do_temp2hum = False
    do_hum2loc = False
    for l in lines:
        if l[0:5] == "seeds":
            for s in l.split(": ")[1].strip().split(" "):
                seeds.append(int(s))

        if l[0:5] == "seed-":
            do_seed2soil = True
        if l[0:5] == "soil-":
            do_soil2fert = True
        if l[0:5] == "ferti":
            do_fert2wat = True
        if l[0:5] == "water":
            do_wat2light = True
        if l[0:5] == "light":
            do_light2temp = True
        if l[0:5] == "tempe":
            do_temp2hum = True
        if l[0:5] == "humid":
            do_hum2loc = True

        if l == "\n":
            do_seed2soil = False
            do_soil2fert = False
            do_fert2wat = False
            do_wat2light = False
            do_light2temp = False
            do_temp2hum = False
            do_hum2loc = False

        if do_seed2soil and l[0] in numbers:
            nrs = l.strip().split(" ")
            map_func(int(nrs[0]), int(nrs[1]), int(nrs[2]), seed2soil)

        if do_soil2fert and l[0] in numbers:
            nrs = l.strip().split(" ")
            map_func(int(nrs[0]), int(nrs[1]), int(nrs[2]), soil2fert)

        if do_fert2wat and l[0] in numbers:
            nrs = l.strip().split(" ")
            map_func(int(nrs[0]), int(nrs[1]), int(nrs[2]), fert2wat)

        if do_wat2light and l[0] in numbers:
            nrs = l.strip().split(" ")
            map_func(int(nrs[0]), int(nrs[1]), int(nrs[2]), wat2light)

        if do_light2temp and l[0] in numbers:
            nrs = l.strip().split(" ")
            map_func(int(nrs[0]), int(nrs[1]), int(nrs[2]), light2temp)

        if do_temp2hum and l[0] in numbers:
            nrs = l.strip().split(" ")
            map_func(int(nrs[0]), int(nrs[1]), int(nrs[2]), temp2hum)

        if do_hum2loc and l[0] in numbers:
            nrs = l.strip().split(" ")
            map_func(int(nrs[0]), int(nrs[1]), int(nrs[2]), hum2loc)


def calc():
    fill_map()
    min_nr = math.inf
    for i in seeds:
        loc_nr = hum2loc[temp2hum[light2temp[wat2light[fert2wat[soil2fert
        [seed2soil[i]]]]]]]
        if loc_nr <= min_nr:
            min_nr = loc_nr

    return min_nr


print(calc())

# print(dict(sorted(seed2soil.items())))
# print(dict(sorted(soil2fert.items())))
# print(dict(sorted(hum2loc.items())))

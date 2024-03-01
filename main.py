import os

path_input = os.path.dirname(os.path.abspath(__file__)) + "\\input.txt"
file = open(path_input, 'r')

lines = []

for line in file.readlines():
    lines.append(line)

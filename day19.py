from main import lines


def workflow(func, x, m, a, s, value, values):
    for line in lines:
        # find defined 'func' workflow
        if line.startswith(func):
            count = 0
            rules = line.replace(func, "").strip("{}")
            rules_split = rules.split(',', rules.count(',') - 1)
            # for each rule:
            for r in rules_split:
                print(func, r)
                # only one rule
                if len(rules_split) == 1:
                    # < - rule
                    if '<' in r.split(':')[0]:
                        # x
                        if r.split(':')[0].split('<')[0] == 'x':
                            if x < (int(r.split(':')[0].split('<')[1])):
                                if r.split(':')[1].split(',')[0] == 'A':
                                    value = 'A'
                                    values.append(value)
                                elif r.split(':')[1].split(',')[0] == 'R':
                                    value = 'R'
                                    values.append(value)
                                else:
                                    value = workflow(r.split(':')[1].split(',')
                                                     [0], x, m, a, s, value,
                                                     values)
                            else:
                                if r.split(':')[1].split(',')[1] == 'A':
                                    value = 'A'
                                    values.append(value)
                                elif r.split(':')[1].split(',')[1] == 'R':
                                    value = 'R'
                                    values.append(value)
                                else:
                                    value = workflow(r.split(':')[1].split(',')
                                                     [1], x, m, a, s, value,
                                                     values)
                        # m
                        if r.split(':')[0].split('<')[0] == 'm':
                            if m < (int(r.split(':')[0].split('<')[1])):
                                if r.split(':')[1].split(',')[0] == 'A':
                                    value = 'A'
                                    values.append(value)
                                elif r.split(':')[1].split(',')[0] == 'R':
                                    value = 'R'
                                    values.append(value)
                                else:
                                    value = workflow(r.split(':')[1].split(',')
                                                     [0], x, m, a, s, value,
                                                     values)
                            else:
                                if r.split(':')[1].split(',')[1] == 'A':
                                    value = 'A'
                                    values.append(value)
                                elif r.split(':')[1].split(',')[1] == 'R':
                                    value = 'R'
                                    values.append(value)
                                else:
                                    value = workflow(r.split(':')[1].split(',')
                                                     [1], x, m, a, s, value,
                                                     values)
                        # a
                        if r.split(':')[0].split('<')[0] == 'a':
                            if a < (int(r.split(':')[0].split('<')[1])):
                                if r.split(':')[1].split(',')[0] == 'A':
                                    value = 'A'
                                    values.append(value)
                                elif r.split(':')[1].split(',')[0] == 'R':
                                    value = 'R'
                                    values.append(value)
                                else:
                                    value = workflow(r.split(':')[1].split(',')
                                                     [0], x, m, a, s, value,
                                                     values)
                            else:
                                if r.split(':')[1].split(',')[1] == 'A':
                                    value = 'A'
                                    values.append(value)
                                elif r.split(':')[1].split(',')[1] == 'R':
                                    value = 'R'
                                    values.append(value)
                                else:
                                    value = workflow(r.split(':')[1].split(',')
                                                     [1], x, m, a, s, value,
                                                     values)
                        # s
                        if r.split(':')[0].split('<')[0] == 's':
                            if s < (int(r.split(':')[0].split('<')[1])):
                                if r.split(':')[1].split(',')[0] == 'A':
                                    value = 'A'
                                    values.append(value)
                                elif r.split(':')[1].split(',')[0] == 'R':
                                    value = 'R'
                                    values.append(value)
                                else:
                                    value = workflow(r.split(':')[1].split(',')
                                                     [0], x, m, a, s, value,
                                                     values)
                            else:
                                if r.split(':')[1].split(',')[1] == 'A':
                                    value = 'A'
                                    values.append(value)
                                elif r.split(':')[1].split(',')[1] == 'R':
                                    value = 'R'
                                    values.append(value)
                                else:
                                    value = workflow(r.split(':')[1].split(',')
                                                     [1], x, m, a, s, value,
                                                     values)
                    # > - rule
                    if '>' in r.split(':')[0]:
                        # x
                        if r.split(':')[0].split('>')[0] == 'x':
                            if x > (int(r.split(':')[0].split('>')[1])):
                                if r.split(':')[1].split(',')[0] == 'A':
                                    value = 'A'
                                    values.append(value)
                                elif r.split(':')[1].split(',')[0] == 'R':
                                    value = 'R'
                                    values.append(value)
                                else:
                                    value = workflow(r.split(':')[1].split(',')
                                                     [0], x, m, a, s, value,
                                                     values)
                            else:
                                if r.split(':')[1].split(',')[1] == 'A':
                                    value = 'A'
                                    values.append(value)
                                elif r.split(':')[1].split(',')[1] == 'R':
                                    value = 'R'
                                    values.append(value)
                                else:
                                    value = workflow(r.split(':')[1].split(',')
                                                     [1], x, m, a, s, value,
                                                     values)
                        # m
                        if r.split(':')[0].split('>')[0] == 'm':
                            if m > (int(r.split(':')[0].split('>')[1])):
                                if r.split(':')[1].split(',')[0] == 'A':
                                    value = 'A'
                                    values.append(value)
                                elif r.split(':')[1].split(',')[0] == 'R':
                                    value = 'R'
                                    values.append(value)
                                else:
                                    value = workflow(r.split(':')[1].split(',')
                                                     [0], x, m, a, s, value,
                                                     values)
                            else:
                                if r.split(':')[1].split(',')[1] == 'A':
                                    value = 'A'
                                    values.append(value)
                                elif r.split(':')[1].split(',')[1] == 'R':
                                    value = 'R'
                                    values.append(value)
                                else:
                                    value = workflow(r.split(':')[1].split(',')
                                                     [1], x, m, a, s, value,
                                                     values)
                        # a
                        if r.split(':')[0].split('>')[0] == 'a':
                            if a > (int(r.split(':')[0].split('>')[1])):
                                if r.split(':')[1].split(',')[0] == 'A':
                                    value = 'A'
                                    values.append(value)
                                elif r.split(':')[1].split(',')[0] == 'R':
                                    value = 'R'
                                    values.append(value)
                                else:
                                    value = workflow(r.split(':')[1].split(',')
                                                     [0], x, m, a, s, value,
                                                     values)
                            else:
                                if r.split(':')[1].split(',')[1] == 'A':
                                    value = 'A'
                                    values.append(value)
                                elif r.split(':')[1].split(',')[1] == 'R':
                                    value = 'R'
                                    values.append(value)
                                else:
                                    value = workflow(r.split(':')[1].split(',')
                                                     [1], x, m, a, s, value,
                                                     values)
                        # s
                        if r.split(':')[0].split('>')[0] == 's':
                            if s > (int(r.split(':')[0].split('>')[1])):
                                if r.split(':')[1].split(',')[0] == 'A':
                                    value = 'A'
                                    values.append(value)
                                elif r.split(':')[1].split(',')[0] == 'R':
                                    value = 'R'
                                    values.append(value)
                                else:
                                    value = workflow(r.split(':')[1].split(',')
                                                     [0], x, m, a, s, value,
                                                     values)
                            else:
                                if r.split(':')[1].split(',')[1] == 'A':
                                    value = 'A'
                                    values.append(value)
                                elif r.split(':')[1].split(',')[1] == 'R':
                                    value = 'R'
                                    values.append(value)
                                else:
                                    value = workflow(r.split(':')[1].split(',')
                                                     [1], x, m, a, s, value,
                                                     values)
                else:
                    # multiple rules
                    if count != len(rules_split) - 1:
                        count += 1
                        if '<' in r.split(':')[0]:
                            if r.split(':')[0].split('<')[0] == 'x':
                                if x < (int(r.split(':')[0].split('<')[1])):
                                    if r.split(':')[1] == 'A':
                                        value = 'A'
                                        values.append(value)
                                    elif r.split(':')[1] == 'R':
                                        value = 'R'
                                        values.append(value)
                                    else:
                                        value = workflow(r.split(':')[1], x, m,
                                                         a, s, value, values)
                            if r.split(':')[0].split('<')[0] == 'm':
                                if m < (int(r.split(':')[0].split('<')[1])):
                                    if r.split(':')[1] == 'A':
                                        value = 'A'
                                        values.append(value)
                                    elif r.split(':')[1] == 'R':
                                        value = 'R'
                                        values.append(value)
                                    else:
                                        value = workflow(r.split(':')[1], x, m,
                                                         a, s, value, values)
                            if r.split(':')[0].split('<')[0] == 'a':
                                if a < (int(r.split(':')[0].split('<')[1])):
                                    if r.split(':')[1] == 'A':
                                        value = 'A'
                                        values.append(value)
                                    elif r.split(':')[1] == 'R':
                                        value = 'R'
                                        values.append(value)
                                    else:
                                        value = workflow(r.split(':')[1], x, m,
                                                         a, s, value, values)
                            if r.split(':')[0].split('<')[0] == 's':
                                if s < (int(r.split(':')[0].split('<')[1])):
                                    if r.split(':')[1] == 'A':
                                        value = 'A'
                                        values.append(value)
                                    elif r.split(':')[1] == 'R':
                                        value = 'R'
                                        values.append(value)
                                    else:
                                        value = workflow(r.split(':')[1], x, m,
                                                         a, s, value, values)
                        if '>' in r.split(':')[0]:
                            if r.split(':')[0].split('>')[0] == 'x':
                                if x > (int(r.split(':')[0].split('>')[1])):
                                    if r.split(':')[1] == 'A':
                                        value = 'A'
                                        values.append(value)
                                    elif r.split(':')[1] == 'R':
                                        value = 'R'
                                        values.append(value)
                                    else:
                                        value = workflow(r.split(':')[1], x, m,
                                                         a, s, value, values)
                            if r.split(':')[0].split('>')[0] == 'm':
                                if m > (int(r.split(':')[0].split('>')[1])):
                                    if r.split(':')[1] == 'A':
                                        value = 'A'
                                        values.append(value)
                                    elif r.split(':')[1] == 'R':
                                        value = 'R'
                                        values.append(value)
                                    else:
                                        value = workflow(r.split(':')[1], x, m,
                                                         a, s, value, values)
                            if r.split(':')[0].split('>')[0] == 'a':
                                if a > (int(r.split(':')[0].split('>')[1])):
                                    if r.split(':')[1] == 'A':
                                        value = 'A'
                                        values.append(value)
                                    elif r.split(':')[1] == 'R':
                                        value = 'R'
                                        values.append(value)
                                    else:
                                        value = workflow(r.split(':')[1], x, m,
                                                         a, s, value, values)
                            if r.split(':')[0].split('>')[0] == 's':
                                if s > (int(r.split(':')[0].split('>')[1])):
                                    if r.split(':')[1] == 'A':
                                        value = 'A'
                                        values.append(value)
                                    elif r.split(':')[1] == 'R':
                                        value = 'R'
                                        values.append(value)
                                    else:
                                        value = workflow(r.split(':')[1], x, m,
                                                         a, s, value, values)
                    else:
                        # < - rule
                        if '<' in r.split(':')[0]:
                            # x
                            if r.split(':')[0].split('<')[0] == 'x':
                                if x < (int(r.split(':')[0].split('<')[1])):
                                    if r.split(':')[1].split(',')[0] == 'A':
                                        value = 'A'
                                        values.append(value)
                                    elif r.split(':')[1].split(',')[0] == 'R':
                                        value = 'R'
                                        values.append(value)
                                    else:
                                        value = workflow(
                                            r.split(':')[1].split(',')
                                            [0], x, m, a, s, value, values)
                                else:
                                    if r.split(':')[1].split(',')[1] == 'A':
                                        value = 'A'
                                        values.append(value)
                                    elif r.split(':')[1].split(',')[1] == 'R':
                                        value = 'R'
                                        values.append(value)
                                    else:
                                        value = workflow(
                                            r.split(':')[1].split(',')
                                            [1], x, m, a, s, value, values)
                            # m
                            if r.split(':')[0].split('<')[0] == 'm':
                                if m < (int(r.split(':')[0].split('<')[1])):
                                    if r.split(':')[1].split(',')[0] == 'A':
                                        value = 'A'
                                        values.append(value)
                                    elif r.split(':')[1].split(',')[0] == 'R':
                                        value = 'R'
                                        values.append(value)
                                    else:
                                        value = workflow(
                                            r.split(':')[1].split(',')
                                            [0], x, m, a, s, value, values)
                                else:
                                    if r.split(':')[1].split(',')[1] == 'A':
                                        value = 'A'
                                        values.append(value)
                                    elif r.split(':')[1].split(',')[1] == 'R':
                                        value = 'R'
                                        values.append(value)
                                    else:
                                        value = workflow(
                                            r.split(':')[1].split(',')
                                            [1], x, m, a, s, value, values)
                            # a
                            if r.split(':')[0].split('<')[0] == 'a':
                                if a < (int(r.split(':')[0].split('<')[1])):
                                    if r.split(':')[1].split(',')[0] == 'A':
                                        value = 'A'
                                        values.append(value)
                                    elif r.split(':')[1].split(',')[0] == 'R':
                                        value = 'R'
                                        values.append(value)
                                    else:
                                        value = workflow(
                                            r.split(':')[1].split(',')
                                            [0], x, m, a, s, value, values)
                                else:
                                    if r.split(':')[1].split(',')[1] == 'A':
                                        value = 'A'
                                        values.append(value)
                                    elif r.split(':')[1].split(',')[1] == 'R':
                                        value = 'R'
                                        values.append(value)
                                    else:
                                        value = workflow(
                                            r.split(':')[1].split(',')
                                            [1], x, m, a, s, value, values)
                            # s
                            if r.split(':')[0].split('<')[0] == 's':
                                if s < (int(r.split(':')[0].split('<')[1])):
                                    if r.split(':')[1].split(',')[0] == 'A':
                                        value = 'A'
                                        values.append(value)
                                    elif r.split(':')[1].split(',')[0] == 'R':
                                        value = 'R'
                                        values.append(value)
                                    else:
                                        value = workflow(
                                            r.split(':')[1].split(',')
                                            [0], x, m, a, s, value, values)
                                else:
                                    if r.split(':')[1].split(',')[1] == 'A':
                                        value = 'A'
                                        values.append(value)
                                    elif r.split(':')[1].split(',')[1] == 'R':
                                        value = 'R'
                                        values.append(value)
                                    else:
                                        value = workflow(
                                            r.split(':')[1].split(',')
                                            [1], x, m, a, s, value, values)
                        # > - rule
                        if '>' in r.split(':')[0]:
                            # x
                            if r.split(':')[0].split('>')[0] == 'x':
                                if x > (int(r.split(':')[0].split('>')[1])):
                                    if r.split(':')[1].split(',')[0] == 'A':
                                        value = 'A'
                                        values.append(value)
                                    elif r.split(':')[1].split(',')[0] == 'R':
                                        value = 'R'
                                        values.append(value)
                                    else:
                                        value = workflow(
                                            r.split(':')[1].split(',')
                                            [0], x, m, a, s, value, values)
                                else:
                                    if r.split(':')[1].split(',')[1] == 'A':
                                        value = 'A'
                                        values.append(value)
                                    elif r.split(':')[1].split(',')[1] == 'R':
                                        value = 'R'
                                        values.append(value)
                                    else:
                                        value = workflow(
                                            r.split(':')[1].split(',')
                                            [1], x, m, a, s, value, values)
                            # m
                            if r.split(':')[0].split('>')[0] == 'm':
                                if m > (int(r.split(':')[0].split('>')[1])):
                                    if r.split(':')[1].split(',')[0] == 'A':
                                        value = 'A'
                                        values.append(value)
                                    elif r.split(':')[1].split(',')[0] == 'R':
                                        value = 'R'
                                        values.append(value)
                                    else:
                                        value = workflow(
                                            r.split(':')[1].split(',')
                                            [0], x, m, a, s, value, values)
                                else:
                                    if r.split(':')[1].split(',')[1] == 'A':
                                        value = 'A'
                                        values.append(value)
                                    elif r.split(':')[1].split(',')[1] == 'R':
                                        value = 'R'
                                        values.append(value)
                                    else:
                                        value = workflow(
                                            r.split(':')[1].split(',')
                                            [1], x, m, a, s, value, values)
                            # a
                            if r.split(':')[0].split('>')[0] == 'a':
                                if a > (int(r.split(':')[0].split('>')[1])):
                                    if r.split(':')[1].split(',')[0] == 'A':
                                        value = 'A'
                                        values.append(value)
                                    elif r.split(':')[1].split(',')[0] == 'R':
                                        value = 'R'
                                        values.append(value)
                                    else:
                                        value = workflow(
                                            r.split(':')[1].split(',')
                                            [0], x, m, a, s, value, values)
                                else:
                                    if r.split(':')[1].split(',')[1] == 'A':
                                        value = 'A'
                                        values.append(value)
                                    elif r.split(':')[1].split(',')[1] == 'R':
                                        value = 'R'
                                        values.append(value)
                                    else:
                                        value = workflow(
                                            r.split(':')[1].split(',')
                                            [1], x, m, a, s, value, values)
                            # s
                            if r.split(':')[0].split('>')[0] == 's':
                                if s > (int(r.split(':')[0].split('>')[1])):
                                    if r.split(':')[1].split(',')[0] == 'A':
                                        value = 'A'
                                        values.append(value)
                                    elif r.split(':')[1].split(',')[0] == 'R':
                                        value = 'R'
                                        values.append(value)
                                    else:
                                        value = workflow(
                                            r.split(':')[1].split(',')
                                            [0], x, m, a, s, value, values)
                                else:
                                    if r.split(':')[1].split(',')[1] == 'A':
                                        value = 'A'
                                        values.append(value)
                                    elif r.split(':')[1].split(',')[1] == 'R':
                                        value = 'R'
                                        values.append(value)
                                    else:
                                        value = workflow(
                                            r.split(':')[1].split(',')
                                            [1], x, m, a, s, value, values)

    print(values)
    return values[0]


def calc():
    sum_total = 0
    for line in lines:
        if len(line) > 0 and line.startswith("{"):
            value = 'R'
            values = []
            ratings = line.strip("{}").split(',')
            print(ratings)
            value = workflow("in", int(ratings[0].split('=')[1]),
                             int(ratings[1].split('=')[1]),
                             int(ratings[2].split('=')[1]),
                             int(ratings[3].split('=')[1]), value, values)
            print("\nValue of {}:".format(ratings[0]), value)
            if value == 'A':
                sum_total += (int(ratings[0].split('=')[1]) +
                              int(ratings[1].split('=')[1]) +
                              int(ratings[2].split('=')[1]) +
                              int(ratings[3].split('=')[1]))
            # break

    return sum_total


print("\nSum total is: {}".format(calc()))

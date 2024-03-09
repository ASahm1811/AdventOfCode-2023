from main import lines


def workflow(func, x, m, a, s, value):
    count = 0
    for line in lines:
        # find defined 'func' workflow
        if line.startswith(func):
            rules = line.replace(func, "").strip("{}")
            rules_split = rules.split(',', rules.count(',') - 1)
            # for each rule:
            for r in rules_split:
                print(func, r)
                # only one rule
                if len(rules_split) == 1:
                    print("r")
                    #                     print(r.split(':'))
                    # < - rule
                    if '<' in r.split(':')[0]:
                        #                         print(r.split(':')[0].split('<'))
                        # x
                        if r.split(':')[0].split('<')[0] == 'x':
                            if x < (int(r.split(':')[0].split('<')[1])):
                                #                                 print(r.split(':')[1].split(',')[0])
                                if r.split(':')[1].split(',')[0] == 'A':
                                    value = 'A'
                                elif r.split(':')[1].split(',')[0] == 'R':
                                    value = 'R'
                                else:
                                    value = workflow(r.split(':')[1].split(',')
                                                     [0], x, m, a, s, value)
                            else:
                                #                                 print(r.split(':')[1].split(',')[1])
                                if r.split(':')[1].split(',')[1] == 'A':
                                    value = 'A'
                                elif r.split(':')[1].split(',')[1] == 'R':
                                    value = 'R'
                                else:
                                    value = workflow(r.split(':')[1].split(',')
                                                     [1], x, m, a, s, value)
                        # m
                        if r.split(':')[0].split('<')[0] == 'm':
                            if m < (int(r.split(':')[0].split('<')[1])):
                                #                                 print(r.split(':')[1].split(',')[0])
                                if r.split(':')[1].split(',')[0] == 'A':
                                    value = 'A'
                                elif r.split(':')[1].split(',')[0] == 'R':
                                    value = 'R'
                                else:
                                    value = workflow(r.split(':')[1].split(',')
                                                     [0], x, m, a, s, value)
                            else:
                                #                                 print(r.split(':')[1].split(',')[1])
                                if r.split(':')[1].split(',')[1] == 'A':
                                    value = 'A'
                                elif r.split(':')[1].split(',')[1] == 'R':
                                    value = 'R'
                                else:
                                    value = workflow(r.split(':')[1].split(',')
                                                     [1], x, m, a, s, value)
                        # a
                        if r.split(':')[0].split('<')[0] == 'a':
                            if a < (int(r.split(':')[0].split('<')[1])):
                                #                                 print(r.split(':')[1].split(',')[0])
                                if r.split(':')[1].split(',')[0] == 'A':
                                    value = 'A'
                                elif r.split(':')[1].split(',')[0] == 'R':
                                    value = 'R'
                                else:
                                    value = workflow(r.split(':')[1].split(',')
                                                     [0], x, m, a, s, value)
                            else:
                                #                                 print(r.split(':')[1].split(',')[1])
                                if r.split(':')[1].split(',')[1] == 'A':
                                    value = 'A'
                                elif r.split(':')[1].split(',')[1] == 'R':
                                    value = 'R'
                                else:
                                    value = workflow(r.split(':')[1].split(',')
                                                     [1], x, m, a, s, value)
                        # s
                        if r.split(':')[0].split('<')[0] == 's':
                            if s < (int(r.split(':')[0].split('<')[1])):
                                #                                 print(r.split(':')[1].split(',')[0])
                                if r.split(':')[1].split(',')[0] == 'A':
                                    value = 'A'
                                elif r.split(':')[1].split(',')[0] == 'R':
                                    value = 'R'
                                else:
                                    value = workflow(r.split(':')[1].split(',')
                                                     [0], x, m, a, s, value)
                            else:
                                #                                 print(r.split(':')[1].split(',')[1])
                                if r.split(':')[1].split(',')[1] == 'A':
                                    value = 'A'
                                elif r.split(':')[1].split(',')[1] == 'R':
                                    value = 'R'
                                else:
                                    value = workflow(r.split(':')[1].split(',')
                                                     [1], x, m, a, s, value)
                    # > - rule
                    if '>' in r.split(':')[0]:
                        #                         print(r.split(':')[0].split('>'))
                        # x
                        if r.split(':')[0].split('>')[0] == 'x':
                            if x > (int(r.split(':')[0].split('>')[1])):
                                #                                 print(r.split(':')[1].split(',')[0])
                                if r.split(':')[1].split(',')[0] == 'A':
                                    value = 'A'
                                elif r.split(':')[1].split(',')[0] == 'R':
                                    value = 'R'
                                else:
                                    value = workflow(r.split(':')[1].split(',')
                                                     [0], x, m, a, s, value)
                            else:
                                #                                 print(r.split(':')[1].split(',')[1])
                                if r.split(':')[1].split(',')[1] == 'A':
                                    value = 'A'
                                elif r.split(':')[1].split(',')[1] == 'R':
                                    value = 'R'
                                else:
                                    value = workflow(r.split(':')[1].split(',')
                                                     [1], x, m, a, s, value)
                        # m
                        if r.split(':')[0].split('>')[0] == 'm':
                            if m > (int(r.split(':')[0].split('>')[1])):
                                if r.split(':')[1].split(',')[0] == 'A':
                                    value = 'A'
                                    print("found")
                                elif r.split(':')[1].split(',')[0] == 'R':
                                    value = 'R'
                                else:
                                    value = workflow(r.split(':')[1].split(',')
                                                     [0], x, m, a, s, value)
                            else:
                                #                                 print(r.split(':')[1].split(',')[1])
                                if r.split(':')[1].split(',')[1] == 'A':
                                    value = 'A'
                                elif r.split(':')[1].split(',')[1] == 'R':
                                    value = 'R'
                                else:
                                    value = workflow(r.split(':')[1].split(',')
                                                     [1], x, m, a, s, value)
                        # a
                        if r.split(':')[0].split('>')[0] == 'a':
                            if a > (int(r.split(':')[0].split('>')[1])):
                                #                                 print(r.split(':')[1].split(',')[0])
                                if r.split(':')[1].split(',')[0] == 'A':
                                    value = 'A'
                                elif r.split(':')[1].split(',')[0] == 'R':
                                    value = 'R'
                                else:
                                    value = workflow(r.split(':')[1].split(',')
                                                     [0], x, m, a, s, value)
                            else:
                                #                                 print(r.split(':')[1].split(',')[1])
                                if r.split(':')[1].split(',')[1] == 'A':
                                    value = 'A'
                                elif r.split(':')[1].split(',')[1] == 'R':
                                    value = 'R'
                                else:
                                    value = workflow(r.split(':')[1].split(',')
                                                     [1], x, m, a, s, value)
                        # s
                        if r.split(':')[0].split('>')[0] == 's':
                            if s > (int(r.split(':')[0].split('>')[1])):
                                #                                 print(r.split(':')[1].split(',')[0])
                                if r.split(':')[1].split(',')[0] == 'A':
                                    value = 'A'
                                elif r.split(':')[1].split(',')[0] == 'R':
                                    value = 'R'
                                else:
                                    value = workflow(r.split(':')[1].split(',')
                                                     [0], x, m, a, s, value)
                            else:
                                #                                 print(r.split(':')[1].split(',')[1])
                                if r.split(':')[1].split(',')[1] == 'A':
                                    value = 'A'
                                elif r.split(':')[1].split(',')[1] == 'R':
                                    value = 'R'
                                else:
                                    value = workflow(r.split(':')[1].split(',')
                                                     [1], x, m, a, s, value)
                else:
                    # multiple rules
                    print(len(rules_split) - 1, count)
                    if count != len(rules_split) - 1:
                        count += 1
                        #                         print(r.split(':'))
                        if '<' in r.split(':')[0]:
                            #                             print(r.split(':')[0].split('<'))
                            if r.split(':')[0].split('<')[0] == 'x':
                                if x < (int(r.split(':')[0].split('<')[1])):
                                    if r.split(':')[1] == 'A':
                                        value = 'A'
                                    elif r.split(':')[1] == 'R':
                                        value = 'R'
                                    else:
                                        value = workflow(r.split(':')[1], x, m,
                                                         a, s, value)
                            if r.split(':')[0].split('<')[0] == 'm':
                                if m < (int(r.split(':')[0].split('<')[1])):
                                    if r.split(':')[1] == 'A':
                                        value = 'A'
                                    elif r.split(':')[1] == 'R':
                                        value = 'R'
                                    else:
                                        value = workflow(r.split(':')[1], x, m,
                                                         a, s, value)
                            if r.split(':')[0].split('<')[0] == 'a':
                                if a < (int(r.split(':')[0].split('<')[1])):
                                    if r.split(':')[1] == 'A':
                                        value = 'A'
                                    elif r.split(':')[1] == 'R':
                                        value = 'R'
                                    else:
                                        value = workflow(r.split(':')[1], x, m,
                                                         a, s, value)
                            if r.split(':')[0].split('<')[0] == 's':
                                if s < (int(r.split(':')[0].split('<')[1])):
                                    if r.split(':')[1] == 'A':
                                        value = 'A'
                                    elif r.split(':')[1] == 'R':
                                        value = 'R'
                                    else:
                                        value = workflow(r.split(':')[1], x, m,
                                                         a, s, value)
                        if '>' in r.split(':')[0]:
                            #                             print(r.split(':')[0].split('>'))
                            if r.split(':')[0].split('>')[0] == 'x':
                                if x > (int(r.split(':')[0].split('>')[1])):
                                    if r.split(':')[1] == 'A':
                                        value = 'A'
                                    elif r.split(':')[1] == 'R':
                                        value = 'R'
                                    else:
                                        value = workflow(r.split(':')[1], x, m,
                                                         a, s, value)
                            if r.split(':')[0].split('>')[0] == 'm':
                                if m > (int(r.split(':')[0].split('>')[1])):
                                    if r.split(':')[1] == 'A':
                                        value = 'A'
                                    elif r.split(':')[1] == 'R':
                                        value = 'R'
                                    else:
                                        value = workflow(r.split(':')[1], x, m,
                                                         a, s, value)
                            if r.split(':')[0].split('>')[0] == 'a':
                                if a > (int(r.split(':')[0].split('>')[1])):
                                    if r.split(':')[1] == 'A':
                                        value = 'A'
                                    elif r.split(':')[1] == 'R':
                                        value = 'R'
                                    else:
                                        value = workflow(r.split(':')[1], x, m,
                                                         a, s, value)
                            if r.split(':')[0].split('>')[0] == 's':
                                if s > (int(r.split(':')[0].split('>')[1])):
                                    if r.split(':')[1] == 'A':
                                        value = 'A'
                                    elif r.split(':')[1] == 'R':
                                        value = 'R'
                                    else:
                                        value = workflow(r.split(':')[1], x, m,
                                                         a, s, value)
                    else:
                        #                         print(r.split(':'))
                        # < - rule
                        if '<' in r.split(':')[0]:
                            #                             print(r.split(':')[0].split('<'))
                            # x
                            if r.split(':')[0].split('<')[0] == 'x':
                                if x < (int(r.split(':')[0].split('<')[1])):
                                    #                                     print(r.split(':')[1].split(',')[0])
                                    if r.split(':')[1].split(',')[0] == 'A':
                                        value = 'A'
                                    elif r.split(':')[1].split(',')[0] == 'R':
                                        value = 'R'
                                    else:
                                        value = workflow(
                                            r.split(':')[1].split(',')
                                            [0], x, m, a, s, value)
                                else:
                                    #                                     print(r.split(':')[1].split(',')[1])
                                    if r.split(':')[1].split(',')[1] == 'A':
                                        value = 'A'
                                    elif r.split(':')[1].split(',')[1] == 'R':
                                        value = 'R'
                                    else:
                                        value = workflow(
                                            r.split(':')[1].split(',')
                                            [1], x, m, a, s, value)
                            # m
                            if r.split(':')[0].split('<')[0] == 'm':
                                if m < (int(r.split(':')[0].split('<')[1])):
                                    if r.split(':')[1].split(',')[0] == 'A':
                                        value = 'A'
                                    elif r.split(':')[1].split(',')[0] == 'R':
                                        value = 'R'
                                    else:
                                        value = workflow(
                                            r.split(':')[1].split(',')
                                            [0], x, m, a, s, value)
                                else:
                                    print("foundx")
                                    if r.split(':')[1].split(',')[1] == 'A':
                                        value = 'A'
                                    elif r.split(':')[1].split(',')[1] == 'R':
                                        value = 'R'
                                    else:
                                        value = workflow(
                                            r.split(':')[1].split(',')
                                            [1], x, m, a, s, value)
                            # a
                            if r.split(':')[0].split('<')[0] == 'a':
                                if a < (int(r.split(':')[0].split('<')[1])):
                                    #                                     print(r.split(':')[1].split(',')[0])
                                    if r.split(':')[1].split(',')[0] == 'A':
                                        value = 'A'
                                    elif r.split(':')[1].split(',')[0] == 'R':
                                        value = 'R'
                                    else:
                                        value = workflow(
                                            r.split(':')[1].split(',')
                                            [0], x, m, a, s, value)
                                else:
                                    # print(r.split(':'), count)
                                    if r.split(':')[1].split(',')[1] == 'A':
                                        value = 'A'
                                    elif r.split(':')[1].split(',')[1] == 'R':
                                        value = 'R'
                                    else:
                                        value = workflow(
                                            r.split(':')[1].split(',')
                                            [1], x, m, a, s, value)
                            # s
                            if r.split(':')[0].split('<')[0] == 's':
                                if s < (int(r.split(':')[0].split('<')[1])):
                                    #                                     print(r.split(':')[1].split(',')[0])
                                    if r.split(':')[1].split(',')[0] == 'A':
                                        value = 'A'
                                    elif r.split(':')[1].split(',')[0] == 'R':
                                        value = 'R'
                                    else:
                                        value = workflow(
                                            r.split(':')[1].split(',')
                                            [0], x, m, a, s, value)
                                else:
                                    #                                     print(r.split(':')[1].split(',')[1])
                                    if r.split(':')[1].split(',')[1] == 'A':
                                        value = 'A'
                                    elif r.split(':')[1].split(',')[1] == 'R':
                                        value = 'R'
                                    else:
                                        value = workflow(
                                            r.split(':')[1].split(',')
                                            [1], x, m, a, s, value)
                        # > - rule
                        if '>' in r.split(':')[0]:
                            #                             print(r.split(':')[0].split('>'))
                            # x
                            if r.split(':')[0].split('>')[0] == 'x':
                                if x > (int(r.split(':')[0].split('>')[1])):
                                    #                                     print(r.split(':')[1].split(',')[0])
                                    if r.split(':')[1].split(',')[0] == 'A':
                                        value = 'A'
                                    elif r.split(':')[1].split(',')[0] == 'R':
                                        value = 'R'
                                    else:
                                        value = workflow(
                                            r.split(':')[1].split(',')
                                            [0], x, m, a, s, value)
                                else:
                                    #                                     print(r.split(':')[1].split(',')[1])
                                    if r.split(':')[1].split(',')[1] == 'A':
                                        value = 'A'
                                    elif r.split(':')[1].split(',')[1] == 'R':
                                        value = 'R'
                                    else:
                                        value = workflow(
                                            r.split(':')[1].split(',')
                                            [1], x, m, a, s, value)
                            # m
                            if r.split(':')[0].split('>')[0] == 'm':
                                if m > (int(r.split(':')[0].split('>')[1])):
                                    #                                     print(r.split(':')[1].split(',')[0])
                                    if r.split(':')[1].split(',')[0] == 'A':
                                        value = 'A'
                                    elif r.split(':')[1].split(',')[0] == 'R':
                                        value = 'R'
                                    else:
                                        value = workflow(
                                            r.split(':')[1].split(',')
                                            [0], x, m, a, s, value)
                                else:
                                    #                                     print(r.split(':')[1].split(',')[1])
                                    if r.split(':')[1].split(',')[1] == 'A':
                                        value = 'A'
                                    elif r.split(':')[1].split(',')[1] == 'R':
                                        value = 'R'
                                    else:
                                        value = workflow(
                                            r.split(':')[1].split(',')
                                            [1], x, m, a, s, value)
                            # a
                            if r.split(':')[0].split('>')[0] == 'a':
                                if a > (int(r.split(':')[0].split('>')[1])):
                                    #                                     print(r.split(':')[1].split(',')[0])
                                    if r.split(':')[1].split(',')[0] == 'A':
                                        value = 'A'
                                    elif r.split(':')[1].split(',')[0] == 'R':
                                        value = 'R'
                                    else:
                                        value = workflow(
                                            r.split(':')[1].split(',')
                                            [0], x, m, a, s, value)
                                else:
                                    #                                     print(r.split(':')[1].split(',')[1])
                                    if r.split(':')[1].split(',')[1] == 'A':
                                        value = 'A'
                                    elif r.split(':')[1].split(',')[1] == 'R':
                                        value = 'R'
                                    else:
                                        value = workflow(
                                            r.split(':')[1].split(',')
                                            [1], x, m, a, s, value)
                            # s
                            if r.split(':')[0].split('>')[0] == 's':
                                if s > (int(r.split(':')[0].split('>')[1])):
                                    #                                     print(r.split(':')[1].split(',')[0])
                                    if r.split(':')[1].split(',')[0] == 'A':
                                        value = 'A'
                                    elif r.split(':')[1].split(',')[0] == 'R':
                                        value = 'R'
                                    else:
                                        value = workflow(
                                            r.split(':')[1].split(',')
                                            [0], x, m, a, s, value)
                                else:
                                    #                                     print(r.split(':')[1].split(',')[1])
                                    if r.split(':')[1].split(',')[1] == 'A':
                                        value = 'A'
                                    elif r.split(':')[1].split(',')[1] == 'R':
                                        value = 'R'
                                    else:
                                        value = workflow(
                                            r.split(':')[1].split(',')
                                            [1], x, m, a, s, value)

    print(value)
    return value


sum_total = 0
for line in lines:
    value = 'R'
    if len(line) > 0 and line.startswith("{"):
        ratings = line.strip("{}").split(',')
        print(ratings)
        value = workflow("in", int(ratings[0].split('=')[1]),
                         int(ratings[1].split('=')[1]),
                         int(ratings[2].split('=')[1]),
                         int(ratings[3].split('=')[1]), value)
        print("\nValue of {}:".format(ratings[0]), value)
        if value == 'A':
            sum_total += (int(ratings[0].split('=')[1]) +
                          int(ratings[1].split('=')[1]) +
                          int(ratings[2].split('=')[1]) +
                          int(ratings[3].split('=')[1]))
        break

print("Sum total:", sum_total)

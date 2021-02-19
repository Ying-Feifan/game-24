import operator
import itertools


def weird_division(n, d):
    return n / d if d else 0


def ops(o, x, y):
    return {
        '+': abs(operator.add(x, y)),
        '-': abs(operator.sub(x, y)),
        '*': abs(operator.mul(x, y)),
        '/': abs(weird_division(x, y))
    }.get(o, 'default case')


def normal(n1, n2, n3, n4):
    for i in operations:
        for j in operations:
            for k in operations:
                result1 = ops(i, n1, n2)
                result2 = ops(j, result1, n3)
                result3 = ops(k, result2, n4)
                if result3 == 24:
                    print('(' + '(' + str(n1) + i + str(n2) + ')' + j + str(n3) + ')' + k + str(n4) + ' = 24')
                result4 = ops(k, n3, n4)
                result5 = ops(j, result1, result4)
                if result5 == 24:
                    print('(' + str(n1) + i + str(n2) + ')' + j + '(' + str(n3) + k + str(n4) + ')' + ' = 24')


def division(n1, n2, n3, n4):
    # BLOCK 1
    for j in operations:
        for k in operations:
            # DIVISION CASE (((AB)C)D)
            result1 = ops('/', n1, n2)
            result2 = ops(j, result1, n3)
            result3 = ops(k, result2, n4)
            if result3 == 24:
                print('(' + '(' + str(n1) + '/' + str(n2) + ')' + j + str(n3) + ')' + k + str(n4) + ' = 24')
            # DIVISION CASE ((AB)(CD))
            result4 = ops(k, n3, n4)
            result5 = ops(j, result1, result4)
            if result5 == 24:
                print('(' + str(n1) + '/' + str(n2) + ')' + j + '(' + str(n3) + k + str(n4) + ')' + ' = 24')
    # BLOCK 2
    for i in operations:
        for k in operations:
            # DIVISION CASE (((AB)C)D)
            result1 = ops(i, n1, n2)
            result2 = ops('/', result1, n3)
            result3 = ops(k, result2, n4)
            if result3 == 24:
                print('(' + '(' + str(n1) + i + str(n2) + ')' + '/' + str(n3) + ')' + k + str(n4) + ' = 24')
            # DIVISION CASE ((C(AB))D)
            result1 = ops(i, n1, n2)
            result2 = ops('/', n3, result1)
            result3 = ops(k, result2, n4)
            if result3 == 24:
                print('(' + str(n3) + '/' + '(' + str(n1) + i + str(n2) + ')' + ')' + k + str(n4) + ' = 24')
            # DIVISION CASE ((AB)(CD))
            result4 = ops(k, n3, n4)
            result5 = ops('/', result1, result4)
            if result5 == 24:
                print('(' + str(n1) + i + str(n2) + ')' + '/' + '(' + str(n3) + k + str(n4) + ')' + ' = 24')
    # BLOCK 3
    for i in operations:
        for j in operations:
            # DIVISION CASE (((AB)C)D)
            result1 = ops(i, n1, n2)
            result2 = ops(j, result1, n3)
            result3 = ops('/', result2, n4)
            if result3 == 24:
                print('(' + '(' + str(n1) + i + str(n2) + ')' + j + str(n3) + ')' + '/' + str(n4) + ' = 24')
            # DIVISION CASE (D((AB)C))
            result1 = ops(i, n1, n2)
            result2 = ops(j, result1, n3)
            result3 = ops('/', n4, result2)
            if result3 == 24:
                print(str(n4) + '/' + '(' + '(' + str(n1) + i + str(n2) + ')' + j + str(n3) + ')' + ' = 24')
            # DIVISION CASE ((AB)(CD))
            result4 = ops('/', n3, n4)
            result5 = ops(j, result1, result4)
            if result5 == 24:
                print('(' + str(n1) + i + str(n2) + ')' + j + '(' + str(n3) + '/' + str(n4) + ')' + ' = 24')
    # BLOCK 4
    for i in operations:
        # DIVISION CASE (((AB)C)D)
        result1 = ops(i, n1, n2)
        result2 = ops('/', result1, n3)
        result3 = ops('/', result2, n4)
        if result3 == 24:
            print('(' + '(' + str(n1) + i + str(n2) + ')' + '/' + str(n3) + ')' + '/' + str(n4) + ' = 24')
        # DIVISION CASE (D(C(AB)))
        result1 = ops(i, n1, n2)
        result2 = ops('/', n3, result1)
        result3 = ops('/', n4, result2)
        if result3 == 24:
            print(str(n4) + '/' + '(' + str(n3) + '/' + '(' + str(n1) + i + str(n2) + ')' + ')' + ' = 24')
        # DIVISION CASE ((C(AB))D)
        result1 = ops(i, n1, n2)
        result2 = ops('/', n3, result1)
        result3 = ops('/', result2, n4)
        if result3 == 24:
            print('(' + str(n3) + '/' + '(' + str(n1) + i + str(n2) + ')' + ')' + '/' + str(n4) + ' = 24')
        # DIVISION CASE (D((AB)C))
        result1 = ops(i, n1, n2)
        result2 = ops('/', result1, n3)
        result3 = ops('/', n4, result2)
        if result3 == 24:
            print(str(n4) + '/' + '(' + '(' + str(n1) + i + str(n2) + ')' + '/' + str(n3) + ')' + ' = 24')
        # DIVISION CASE ((AB)(CD))
        result4 = ops('/', n3, n4)
        result5 = ops('/', result1, result4)
        if result5 == 24:
            print('(' + str(n1) + i + str(n2) + ')' + '/' + '(' + str(n3) + '/' + str(n4) + ')' + ' = 24')
    # BLOCK 5
    for j in operations:
        # DIVISION CASE (((AB)C)D)
        result1 = ops('/', n1, n2)
        result2 = ops(j, result1, n3)
        result3 = ops('/', result2, n4)
        if result3 == 24:
            print('(' + '(' + str(n1) + '/' + str(n2) + ')' + j + str(n3) + ')' + '/' + str(n4) + ' = 24')
        # DIVISION CASE (D((AB)C))
        result1 = ops('/', n1, n2)
        result2 = ops(j, result1, n3)
        result3 = ops('/', n4, result2)
        if result3 == 24:
            print(str(n4) + '/' + '(' + '(' + str(n1) + '/' + str(n2) + ')' + j + str(n3) + ')' + ' = 24')
        # DIVISION CASE ((AB)(CD))
        result4 = ops('/', n3, n4)
        result5 = ops(j, result1, result4)
        if result5 == 24:
            print('(' + str(n1) + '/' + str(n2) + ')' + j + '(' + str(n3) + '/' + str(n4) + ')' + ' = 24')
    # BLOCK 6
    for k in operations:
        # DIVISION CASE (((AB)C)D)
        result1 = ops('/', n1, n2)
        result2 = ops('/', result1, n3)
        result3 = ops(k, result2, n4)
        if result3 == 24:
            print('(' + '(' + str(n1) + '/' + str(n2) + ')' + '/' + str(n3) + ')' + k + str(n4) + ' = 24')
        # DIVISION CASE ((C(AB))D)
        result1 = ops('/', n1, n2)
        result2 = ops('/', n3, result1)
        result3 = ops(k, result2, n4)
        if result3 == 24:
            print('(' + str(n3) + '/' + '(' + str(n1) + '/' + str(n2) + ')' + ')' + k + str(n4) + ' = 24')
        result4 = ops(k, n3, n4)
        result5 = ops('/', result1, result4)
        if result5 == 24:
            print('(' + str(n1) + '/' + str(n2) + ')' + '/' + '(' + str(n3) + k + str(n4) + ')' + ' = 24')
    # BLOCK 7
    # DIVISION CASE (((AB)C)D)
    result1 = ops('/', n1, n2)
    result2 = ops('/', result1, n3)
    result3 = ops('/', result2, n4)
    if result3 == 24:
        print('(' + '(' + str(n1) + '/' + str(n2) + ')' + '/' + str(n3) + ')' + '/' + str(n4) + ' = 24')
    # DIVISION CASE (D(C(AB)))
    result1 = ops('/', n1, n2)
    result2 = ops('/', n3, result1)
    result3 = ops('/', n4, result2)
    if result3 == 24:
        print(str(n4) + '/' + '(' + str(n3) + '/' + '(' + str(n1) + '/' + str(n2) + ')' + ')' + ' = 24')
    # DIVISION CASE ((C(AB))D)
    result1 = ops('/', n1, n2)
    result2 = ops('/', n3, result1)
    result3 = ops('/', result2, n4)
    if result3 == 24:
        print('(' + str(n3) + '/' + '(' + str(n1) + '/' + str(n2) + ')' + ')' + '/' + str(n4) + ' = 24')
    # DIVISION CASE (D((AB)C))
    result1 = ops('/', n1, n2)
    result2 = ops('/', result1, n3)
    result3 = ops('/', n4, result2)
    if result3 == 24:
        print(str(n4) + '/' + '(' + '(' + str(n1) + '/' + str(n2) + ')' + '/' + str(n3) + ')' + ' = 24')
    # DIVISION CASE ((AB)(CD))
    result4 = ops('/', n3, n4)
    result5 = ops('/', result1, result4)
    if result5 == 24:
        print('(' + str(n1) + '/' + str(n2) + ')' + '/' + '(' + str(n3) + '/' + str(n4) + ')' + ' = 24')


# MAIN CODE
while 0 == 0:
    # INPUT
    m1, m2, m3, m4 = input('Welcome to the game 24 solver, what were the numbers \n').split()
    m1 = float(m1)
    m2 = float(m2)
    m3 = float(m3)
    m4 = float(m4)
    # EXIT
    if m1 == 0 and m2 == 0 and m3 == 0 and m4 == 0:
        break
    operations = ['+', '-', '*']
    # NORMAL OPERATION
    print('normal operation:')
    normal(m1, m2, m3, m4)

    # FUCK DIVISION
    print('\ndivision operation:')
    array = itertools.permutations([m1, m2, m3, m4])

    for each in array:
        q1 = each[0]
        q2 = each[1]
        q3 = each[2]
        q4 = each[3]
        division(q1, q2, q3, q4)

    print('------------------------------------------------------------------------------------------------\n')

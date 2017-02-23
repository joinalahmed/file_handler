import itertools
from setuptools.package_index import unique_everseen


def checker(liter):
    check_list = list()
    for im in range(len(liter)):
        af = str(liter[im])
        mid_list = af
        for xx in range(len(mid_list)):
            for ro in range(len(mid_list)):
                if mid_list[ro] == mid_list[xx]:
                    continue
                else:
                    alp = str(xx + 1) + str(ro + 1)
                    check_list.append(alp)
            check_list = list(unique_everseen(check_list))
            check_list.sort()
    return check_list


# Compliments The Input Test-Pattern

def compliment_stuck(item):
    d = list()
    for k in range(len(item)):
        copy = list(item[k])
        for l in range(len(copy)):
            if copy[l] == str(1):
                copy[l] = str(0)
                continue
            if copy[l] == str(0):
                copy[l] = str(1)
        copy = ''.join(copy)
        d.append(copy)
    d = ''.join(d)
    return d


# Embeds alternating 1's and 0's

def main_fun(append_list):
    mid_list1 = list()
    for ins in range(len(append_list)):
        appended = str(append_list[ins])
        add0 = appended + '0'
        add1 = appended + '1'
        mid_list1.append(add0)
        mid_list1.append(add1)
    return list(unique_everseen(mid_list1))


test_pattern = ['10']

# Take Input
num_lines = int(input('ENTER NUMBER OF LINES IN CIRCUIT'))

# Check Number of Lines
if num_lines == 1:
    print('Invalid Input')
if num_lines == 2:
    print('Test Pattern for Bridging fault', test_pattern)
    test_set = test_pattern

if num_lines > 2:
    for line_num in range(3, num_lines + 1):
        test_set = []
        length_pattern = len(test_pattern)
        permutations = list()
        # Generate possible Faults
        for lines in range(1, line_num + 1):
            permutations.append(lines)
        permutations = list(itertools.permutations(permutations, 2))

        for i in range(len(permutations)):
            var1 = str(permutations[i][0])
            for j in range(1, len(permutations[i])):
                var1 += str(permutations[i][j])
            permutations[i] = var1
        permutations = list(unique_everseen(permutations))
        permutations.sort()

        test_pattern = main_fun(test_pattern)
        combs = []
        # Generate Sets from Test-Pattern
        for combination in range(length_pattern, len(test_pattern) + 1):
            pattern = [list(x) for x in itertools.combinations(test_pattern, combination)]
            combs.extend(pattern)
        # Check Faults Covered By Sets of Test-Pattern
        for combinations in range(len(combs)):
            test_result = checker(combs[combinations])
            test_result.sort()
            if str(test_result) == str(permutations):
                print(len(permutations) / 2, 'Possible')
                print(len(test_result) / 2, 'Detected')
                # If all Faults are covered, Print The Test Set
                if num_lines == line_num:
                    print('Test Pattern for Bridging fault with lines', line_num, combs[combinations])
                    test_set = combs[combinations]
                    print('this is test set', test_set)
                    ff = open('test_pattern.py', 'a')
                    ff.write(
                        str(test_set) + ' Number of test vectors ' + str(len(test_set)) + ' for number of lines ' + str(
                            num_lines) + '\n')
                    ff.write('\n')
                    temp = compliment_stuck(combs[combinations][0])
                    test_set.append(temp)
                    print('Test Pattern for Stuck-at-Fault', test_set)
                    ff.close()
                test_pattern = combs[combinations]

                break

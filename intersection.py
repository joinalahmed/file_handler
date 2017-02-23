# def zero_checker(test_set_sequence):
#    actual_value = ''
#    for value_sequence in range(len(test_set_sequence)):
#        if test_set_sequence[value_sequence] is 0:
#            if value_sequence == 0:
#                verify = test_set_sequence[value_sequence + 1]
#                verify = str(verify)
#                for make in range(len(verify)):
#                    actual_value += str(0)
#                break
#            if value_sequence > 0:
#                verify = test_set_sequence[value_sequence - 1]
#                verify = str(verify)
#                for make in range(len(verify)):
#                    actual_value += str(0)
#                break
#            break
#    test_set_sequence[value_sequence] = actual_value
#    return test_set_sequence

import itertools
from setuptools.package_index import unique_everseen

# GLOBAL VARIABLES
test_set_case1 = []
test_set_case2 = []


def test_case_generator(num_lines_main):
    # Take Input
    num_lines = num_lines_main

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

    # Check Number of Lines
    if num_lines == 1:
        print('Invalid Input')
    if num_lines == 2:
        print('Test Pattern for Bridging fault', test_pattern)

    if num_lines > 2:
        for line_num in range(3, num_lines + 1):
            # test_set_1 = []
            length_pattern = len(test_pattern)
            permutations = list()
            # Generate possible Faults
            for lines in range(1, line_num + 1):
                permutations.append(lines)
            permutations = list(itertools.permutations(permutations, 2))

            for i in range(len(permutations)):
                var123 = str(permutations[i][0])
                for j in range(1, len(permutations[i])):
                    var123 += str(permutations[i][j])
                permutations[i] = var123
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
                    # If all Faults are covered, Print The Test Set
                    if num_lines == line_num:
                        print('Test Pattern for Bridging fault with lines', line_num, combs[combinations])
                        return combs[combinations]
                    break


test_set = ['001', '011', '010', '000']
var_temp = test_set[0]
var_temp_1 = len(var_temp)
test_set_case1 = test_case_generator(var_temp_1)
print(test_set_case1)
temp_var = ''
temp_var1 = ''

# COMPLEMENT
for value in range(len(test_set_case1)):
    temp_var = ''.join(str(test_set_case1[value]))
    for value_s in range(len(temp_var)):
        if temp_var[value_s] is '1':
            temp_var1 += '0'
        if temp_var[value_s] is '0':
            temp_var1 += '1'
    test_set_case2.append(temp_var1)
    temp_var = ''
    temp_var1 = ''

# SET COMPARATOR AND UNION FINDER
compare_1 = set(test_set).intersection(test_set_case1)
compare_2 = set(test_set).intersection(test_set_case2)
var1 = set(test_set_case1)
var2 = set(test_set_case2)
if compare_1 == set():
    print(test_set_case2, '- Can be used')
else:
    print(test_set_case1, '- Can be used')

def zero_checker(test_set_sequence):
    actual_value = ''
    for value_sequence in range(len(test_set_sequence)):
        if test_set_sequence[value_sequence] is 0:
            if value_sequence == 0:
                verify = test_set_sequence[value_sequence + 1]
                verify = str(verify)
                for make in range(len(verify)):
                    actual_value += str(0)
                break
            if value_sequence > 0:
                verify = test_set_sequence[value_sequence - 1]
                verify = str(verify)
                for make in range(len(verify)):
                    actual_value += str(0)
                break
            break
    test_set_sequence[value_sequence] = actual_value
    return test_set_sequence

test_set = []
size_of_test_set_element = int(input('enter the length of bit sequence'))
for take_input in range(size_of_test_set_element):
    test_set.append(str(input('enter the elements of test_set one by one ')))
print(test_set)
if 0 in test_set:
    test_set_sequence_refer = zero_checker(test_set)
    test_set = test_set_sequence_refer

test_set_case1 = [10100000, 11000000]
if 0 in test_set_case1:
    test_set_sequence_refer = zero_checker(test_set_case1)
    test_set_case1 = test_set_sequence_refer
print(test_set_case1)

test_set_case2 = []
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
    # print('test_set_case2 : ', test_set_case2)
    temp_var = ''
    temp_var1 = ''

print(test_set_case2)
if 0 in test_set_case2:
    test_set_sequence_refer = zero_checker(test_set_case1)
    test_set_case1 = test_set_sequence_refer


# SET COMPARATOR AND UNION FINDER
compare_1 = set(test_set).intersection(test_set_case1)
compare_2 = set(test_set).intersection(test_set_case2)
var1 = set(test_set_case1)
var2 = set(test_set_case2)
if compare_1 == var1:
    print('test_set_case1 can be used')
elif compare_2 == var2:
    print('test_set_case1 can be used')
else:
    print('NO MATCH FOUND')

test_set = [100, 101, 000, 110]
test_set_case1 = [101, 100]
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
    temp_var = ''
    temp_var1 = ''

print(test_set_case2)

# SET COMPARATOR
for compare in range(len(test_set)):



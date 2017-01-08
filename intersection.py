test_set = [110, 101, 100, 111]
test_set_case1 = [101, 100]
test_set_case2 = []
temp_var = ''
temp_var1 = ''

test_set.sort()
test_set_case1.sort()
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
test_set_case2.sort()



# SET COMPARATOR
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
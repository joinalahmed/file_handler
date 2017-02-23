import re

# GLOBAL FILES AND VARIABLES
fp = open('intermediate.tfc', 'w+')
fp.close()

list_var = []
list_var1 = []

# REAL FILE TO .tfc FILE GENERATOR BLOCK
fi_le = open('1.real', 'r+')
for line in fi_le:
    if line.strip() == '.begin':
        break
    var1 = open('intermediate.tfc', 'a')
    var1.write(line)
    var1.close()
temp = open('intermediate.tfc', 'a')
temp.write('BEGIN'+'\n')
temp.close()
with open('1.real', 'r+') as file:
    for line in file:
        if line.strip() == '.begin':
            break
    for line in file:
        if line.strip() == '.end':
            break
        if '#' in line:
            continue
        list_var = re.split('\\s', line)
        del list_var[-1]
        for io in range(len(list_var)):
            list_var1.append(list_var[io])
            list_var1.append(',')
        del list_var1[-1]
        list_var1[1] = ' '
        if 'p' in list_var1:
            list_var1[0] = 'p3'
        if 'P' in list_var1:
            list_var1[0] = 'P3'
        list_var2 = ''.join(list_var1)
        my_fp = open('intermediate.tfc', 'a')
        my_fp.write(list_var2 + '\n')
        my_fp.close()
        list_var1 = []
temp2 = open('intermediate.tfc', 'a')
temp2.write('END')
temp2.close()

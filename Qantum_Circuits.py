main_li = []
main_li_1 = []
my_fp = open('mid.tfc', 'w')
my_fp.close()
with open('main1.tfc', 'r+') as file:
    for line in file:
        if line.strip() == 'BEGIN':
            break
    for line in file:
        if line.strip() == 'END':
            break
        if '#' in line:
            continue
        main_li.append(line)

val_1 = int(input('enter start level'))
val_2 = int(input('enter stop level'))
sel_val = int(input('1 or 0'))
# FORWARD SIMULATION BLOCK
if sel_val is 1:
    with open('mid.tfc', 'a') as file:
        with open('main1.tfc', 'r+') as file_1:
            for line in file_1:
                if line.strip() == 'BEGIN':
                    break
                kk = open('mid.tfc', 'a')
                kk.write(line)
                kk.close()
            file.write('BEGIN' + '\n')
        main_li_1 = main_li[val_1:val_2]
        for ii in range(len(main_li_1)):
            temp_1 = str(main_li_1[ii])
            file.write(temp_1)
        file.write('END' + '\n')

# REVERSE SIMULATION BLOCK
if sel_val is 0:
    with open('mid.tfc', 'a') as file:
        with open('main1.tfc', 'r+') as file_1:
            for line in file_1:
                if line.strip() == 'BEGIN':
                    break
                kk = open('mid.tfc', 'a')
                kk.write(line)
                kk.close()
            file.write('BEGIN' + '\n')
        main_li_1 = main_li[val_1:val_2]
        main_li_1 = main_li_1[::-1]
        for ii in range(len(main_li_1)):
            temp_1 = str(main_li_1[ii])
            file.write(temp_1)
        file.write('END' + '\n')


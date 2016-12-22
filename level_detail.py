import re
main_li = []
sub_li = []
with open('main1.txt', 'r+') as file:
    for line in file:
        var1 = re.split(',',line)
        main_li.append(var1)
    print('Total Number Of Level in Circuit :', len(main_li)-1)
    level_no = int(input('enter the level number'))
    sub_li = main_li[level_no]
    print('List Of Control Bits Are : ')
    for ii in range(len(sub_li)-1):
        print( sub_li[ii])
    print('Target Bit :')
    print(sub_li[-1])






import re
import prettytable

# GLOBAL VARIABLES AND FILES
gate1 = 'NOT GATE'
gate2 = 'C-NOT GATE'
gate3 = 'TOFFOLI GATE'
gate4 = 'FREDKIN GATE'
gate5 = 'SWAP GATE'
gate6 = 'PERES GATE'
alpha = []
alpha_1 = []
beta = []
beta_1 = []
var2 = []
count = 1
m11 = ''
my_fp = open("tt_generator.py", "w")
my_fp.close()
qw = open("main1.txt", "w")
qw.close()


# NEGATIVE CONTROL - HANDLER
def neg_ctl(charm):
    for mns in range(len(charm)):
        hu = str(charm[mns])
        if hu == ",":
            continue
        mk = len(charm)
        mk -= 1
        if mns == mk:
            break
        if "'" not in hu:
            continue
        hs = re.split("'", hu)
        hs_fin = list()
        hs_fin.append(hs[0])
        hs_fin.append(' = not ')
        hs_fin.append(hs[0])
        hs_fin.append(';')
        hss = ''.join(hs_fin)
        jk = 'if ' + hs[0] + ' == 1:'
        jk1 = ''.join(jk)
        lo = jk1 + hss
        mx = open('tt_generator.py', 'a')
        mx.write(lo + '\n')
        mx.close()


# BLOCK FOR LEVEL DETAILS
def level_detail(wander):
    print('\n', 'Total Number of Level(s) in Circuit : ', len(wander), ', Starting From 0 - ', len(wander) - 1)
    print('\n', 'Total Number of Gate(s) in Circuit : ', len(wander))
    for inp in range(len(wander)):
        wander_12 = wander[inp]
        temp1 = wander_12[0]
        temp1 = str(temp1)
        r = re.compile("([a-zA-Z]+)([0-9]+)")
        m = r.match(temp1)
        master_1 = m.group(1)
        master_2 = m.group(2)

        # NOT GATE BLOCK
        if int(master_2) == 1:
            print('\n Type of Gate used in Level-', inp, ': ', gate1)
            print('\n Number of Control Variable(s) : 0')
            print('\n Number of Target Variable(s): 1')
            print('\n Target Variable , Line Number :- ', wander_12[1])
            my_tab = prettytable.PrettyTable(['Level Number', 'Control Variable', 'Target Variables', 'Gate'])
            my_tab.add_row([inp, 0, 1, gate1])
            print(my_tab)

        # C-NOT GATE BLOCK
        if (master_1 == 't' or master_1 == 'T') and int(master_2) == 2:
            print('\n Type of Gate used in Level-', inp, ': ', gate2)
            print('\n Number of Control Variable(s) : 1')
            print('\n Number of Target Variable(s): 1')
            print('\n Control Variable , Line Number :- ', wander_12[-2])
            print('\n Target Variable , Line Number :- ', wander_12[-1])

        # TOFFOLI GATE BLOCK
        if master_1 == 't' or master_1 == 'T':
            if int(master_2) > 2:
                print('\n Type of Gate used in Level-', inp, ': ', gate3)
                del wander_12[0]
                print('\n Number of Control Variables : ', len(wander_12) - 1)
                print('\n Number of Target Variable : 1')
                for im in range(len(wander_12) - 1):
                    print('\n Control Variable, Line Number :- ', wander_12[im], '\n')
                print('\n Target Variable, Line Number :- ', wander_12[-1])

        # FREDKIN GATE BLOCK
        if (master_1 == 'f' or master_1 == 'F') and int(master_2) > 2:
            del wander_12[0]
            print('\n Type of Gate used in Level-', inp, ': ', gate4)
            print('\n Number of Control Variables : ', len(wander_12) - 2)
            print('\n Number of Target Variables : 2')
            for ill in range(len(wander_12) - 2):
                print('\n Control Variable , Line Number :- ', wander_12[ill])
            print('\n  First Target Variable , Line Number :- ', wander_12[-1])
            print('\n  Second Target Variable , Line Number :- ', wander_12[-2])

        # SWAP GATE BLOCK
        if (master_1 == 'f' or master_1 == 'F') and int(master_2) == 2:
            del wander_12[0]
            print('\n Type of Gate used in Level-', inp, ': ', gate5)
            print('\n Number of Control Variables : 0')
            print('\n Number of Target Variables : 2')
            print('\n First Control Variable , Line Number :- ', wander_12[0])
            print('\n Second Control Variable , Line Number :-  ', wander_12[1])

        # PERES GATE BLOCK
        if master_1 == 'p' or master_1 == 'P':
            if int(master_2) > 2:
                del wander_12[0]
                print(wander_12)
                print('\n Type of Gate Used in Level-', inp, ': ', gate6)


# BLOCK FOR .tfc FILE PROCESSING , EXTRACTION OF DATA
with open('main1.tfc', 'r+') as file:
    for line in file:
        if line.strip() == 'BEGIN':
            break
    for line in file:
        if line.strip() == 'END':
            break
        if '#' in line:
            continue
        line1 = re.split(',', line)
        var1 = str(line1[0])
        var1 = re.split(' ', var1)
        r_var = str(var1[0])
        r1112 = re.compile("([a-zA-Z]+)([0-9]+)")
        m123 = r1112.match(r_var)
        m11 = m123.group(1)
        for iy in range(1, len(line1)):
            var1.append(line1[iy])
        var2.append(var1)
        length = len(line1)
        line2 = line1[0]
        line2 = re.split('\\s', line2)
        line2 = list(line2)
        line1[0] = line2[1]
        length1 = len(line1)
        line3 = line1[length1 - 1]
        length2 = len(line3)
        line3 = re.split('\n', line3)
        line1[length1 - 1] = line3[0]
        line_final = list()
        for ii in range(len(line1)):
            line_final.append(line1[ii])
            line_final.append(',')
        del line_final[-1]
        line_final.insert(0, m11)
        line_final.insert(1, ',')
        line_final1 = ''.join(line_final)
        ff = open('main1.txt', 'a')
        ff.write(line_final1)
        ff.write('\n')
        ff.close()

# CONSTANT-HANDLER
with open('main1.tfc', 'r+') as input_file:
    temp_list_1 = []
    temp_list_2 = []
    for statement in input_file:
        if statement.strip() == 'BEGIN':
            break
        temp_list_1.append(statement)
    for data in range(len(temp_list_1)):
        var_a = re.split(' ', temp_list_1[data])
        if '.v' in var_a:
            alpha = var_a
            rust = str(alpha[-1])
            rust = re.split('\n', rust)
            alpha[-1] = rust[0]
            alpha_1 = str(alpha[-1])
            alpha_1 = re.split(',', alpha_1)
        if '.c' in var_a:
            beta = var_a
            rust_1 = str(beta[-1])
            rust_1 = re.split('\n', rust_1)
            beta[-1] = rust_1[0]
            beta_1 = str(beta[-1])
            beta_1 = re.split(',', beta_1)
            program_counter = -(len(beta_1))
            alpha_1 = alpha_1[program_counter:]
            with open('tt_generator.py', 'a') as file_overwrite:
                for gamma in range(len(alpha_1)):
                    temp_list_2 = str(alpha_1[gamma] + ' = ' + beta_1[gamma])
                    file_overwrite.write(temp_list_2 + '\n')

# EQUATION GENERATOR
with open('main1.txt', 'r+') as exp:
    for learn_1 in exp:
        if len(learn_1) == 1:
            if learn_1[0] == '\n':
                continue
        if learn_1[0] == '#':
            continue
        ax = learn_1
        axx = re.split(',', ax)
        mn = len(axx)
        mn -= 1
        axx1 = str(axx[mn])
        axx2 = re.split('\n', axx1)
        axx[mn] = axx2[0]
        mn1 = len(axx)
        mn2 = mn1 - 1
        axx[mn2] = axx2[0]
        learn_1 = axx
        linen = list()
        for ii in range(len(learn_1)):
            linen.append(learn_1[ii])
            linen.append(',')
        del linen[-1]
        learn_1 = linen
        # lib_id LIBRARY IDENTIFIER
        lib_id = str(learn_1[0])
        learn_1 = learn_1[2:]

        # FREDKIN GATE AND SWAP GATE LIBRARY HANDLER
        if lib_id == 'F' or lib_id == 'f':
            lk = learn_1
            # SWAP GATE HANDLER
            if len(lk) == 3:
                lk.remove(',')
                bn1 = 'temp' + ' = ' + str(lk[0])
                bn2 = str(lk[0]) + ' = ' + str(lk[1])
                bn4 = str(lk[1]) + ' = ' + 'temp'
                bn3 = open('tt_generator.py', 'a')
                bn3.write('# SWAP GATE BLOCK' + '\n')
                bn3.write(bn1 + '\n')
                bn3.write(bn2 + '\n')
                bn3.write(bn4 + '\n')
                bn3.write('\n')
                bn3.close()

            # FREDKIN GATE HANDLER
            if len(lk) >= 3:
                ins = ''
                for lh in range(len(lk)):
                    ins += str(lk[lh])
                ins = re.split(',', ins)
                for il in range(len(ins) - 2):
                    mi = str(ins[il])
                    mi = mi + ' = ' + mi
                    eqn = open('tt_generator.py', 'a')
                    eqn.write(str(mi) + '\n')
                    eqn.close()
                variable_x = list(ins[-2])
                variable_x.append(' = (')
                variable_x.append('(not (')
                variable_x_1 = list(ins[-1])
                variable_x_1.append(' = (')
                variable_x_1.append('(not (')
                if len(ins) == 3:
                    variable_x.append(ins[0] + ')')
                    variable_x.append(') and ')
                    variable_x.append(ins[1])
                    variable_x.append(') ^ ')
                    variable_x.append('(')
                    variable_x.append(ins[0])
                    variable_x.append(' and ')
                    variable_x.append(ins[-1])
                    variable_x.append(')')
                    variable_x_x = ''.join(variable_x)
                    variable_x_1.append(ins[0] + ')' + ') ')
                    variable_x_1.append('and ')
                    variable_x_1.append(ins[-1] + ') ')
                    variable_x_1.append('^ ' + '(' + ins[0] + ' and ' + ins[1] + ')')
                    wax = ''.join(variable_x_1)
                    c_open = open('tt_generator.py', 'a')
                    c_open.write(variable_x_x + '\n')
                    c_open.write(wax + '\n')
                    c_open.close()

                if len(ins) > 3:
                    tem = []
                    for ui in range(len(ins) - 1):
                        tem.append(ins[ui])
                        tem.append(' and ')
                    tem[-1] = '^ ('
                    tem.insert(0, ins[-2] + ' = (((not(')
                    tem.insert(-3, '))')
                    tem.insert(-1, ') ')
                    tem1 = []
                    for io in range(len(ins) - 2):
                        tem1.append(ins[io])
                        tem1.append(' and ')
                    tem1.append(ins[-1])
                    tem1.append('))')
                    tem = tem + tem1
                    vast = ''.join(tem)
                    vf = open('tt_generator.py', 'a')
                    vf.write(vast + '\n')
                    vf.close()
                    rt = []
                    for ik in range(len(ins) - 2):
                        rt.append(ins[ik])
                        rt.append(' and ')
                    rt.append(ins[-1])
                    rt.insert(0, ins[-1] + ' = (((not(')
                    rt.insert(-2, '))')
                    rt.append(') ^ (')
                    for zx in range(len(ins) - 2):
                        rt.append(ins[zx])
                        rt.append(' and ')
                    rt.append(ins[-2] + '))')
                    rt1 = ''.join(rt)
                    bn = open('tt_generator.py', 'a')
                    bn.write(rt1 + '\n')
                    bn.close()

        # PERES GATE LIBRARY HANDLER
        if lib_id == 'P' or lib_id == 'P':
            temp = list(learn_1[2])
            temp.append('=' + learn_1[0])
            temp.append('^' + learn_1[2])
            temp123 = ''.join(temp)
            temp = list(learn_1[4])
            temp.append('=')
            temp.append('(' + learn_1[0])
            temp.append(' and ' + learn_1[2])
            temp.append(')')
            temp.append('^' + learn_1[4])
            temp223 = ''.join(temp)
            fg = open('tt_generator.py', 'a')
            fg.write(temp123 + '\n')
            fg.write(temp223 + '\n')
            fg.close()

        # NCT AND GT LIBRARY HANDLER
        if lib_id == 'T' or lib_id == 't':
            if len(learn_1) == 1:
                benn = list(learn_1)
                benn.append('=')
                benn.append('not')
                benn.append(' ')
                benn.append(benn[0])
                benn1 = ''.join(benn)
                tenn = open('tt_generator.py', 'a')
                tenn.write(benn1 + '\n')
                tenn.close()
            if len(learn_1) == 3:
                train = list(learn_1)
                nn = len(train)
                train_1 = list(train[nn - 1])
                ty = len(train_1)
                ty -= 1
                if train_1[ty] == ' ':
                    del train_1[ty]
                train_1.append('=')
                train_1.append(train[0])
                train_1.append('')
                train_1.append('^')
                train_1.append('')
                train_1.append(train[nn - 1])
                train_2 = ''.join(train_1)
                if "'" in train_2:
                    al = list(train_2)
                    al.remove("'")
                    print(al)
                    al1 = ''.join(al)
                    train_2 = al1
                train_3 = open('tt_generator.py', 'a')
                train_3.write(train_2 + '\n')
                train_3.close()
                if "'" in str(learn_1):
                    neg_ctl(learn_1)

            if len(learn_1) > 3:
                list1 = list(learn_1)
                num = len(list1)
                insert1 = num - 1
                list2 = list1[insert1]
                list3 = list(list2)
                list3.append('=')
                list3.append('(')
                hg = len(list1)
                la_el = list1[hg - 1]
                list1.insert(0, la_el)
                list1.insert(1, '=')
                list1.insert(2, '(')
                hg1 = len(list1)
                list1[hg1 - 2] = '^'
                list1.insert(hg1 - 2, ')')
                z = 4
                ven = len(list1)
                for i in list1:
                    list1[z] = ' and '
                    z += 2
                    if z == ven - 3:
                        break
                qwerty = ''.join(list1)
                vs = ''.join(list1)
                if "'" in vs:
                    vss = re.split("'", vs)
                    vss1 = ''.join(vss)
                    qwerty = vss1
                qwerty1 = open('tt_generator.py', 'a')
                qwerty1.write(qwerty + '\n')
                qwerty1.close()
                if "'" in str(learn_1):
                    neg_ctl(learn_1)

# LEVEL(S) DETAILS FUNCTION CALLER BLOCK
# u_ip = int(input('WANT LEVEL(S) DETAILS , IF YES PRESS 1 , IF NO PRESS 0'))
# if u_ip == 1:
# level_detail(var2)

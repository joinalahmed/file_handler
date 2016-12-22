import re

gate1 = 'NOT GATE'
gate2 = 'C-NOT GATE'
gate3 = 'TOFFOLI GATE'
gate4 = 'FREDKIN GATE'
gate5 = 'PERES GATE'
var2=[]

my_fp = open('tt_generator.py ', 'w')
my_fp.close()

qw = open('main1.txt', 'w')
qw.close()

def neg_ctl(hexo):
    for mns in range(len(hexo)):
        hu = str(hexo[mns])
        if hu == ",":
            continue
        mk = len(hexo)
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


#Function to determine level detail
def level_detail(varn):
    print '\n', 'Total Number of Level(s) in Circuit : ', len(varn) , ', Starting From 0 - ',len(varn)-1
    print '\n', 'Total Number of Gate(s) in Circuit : ', len(varn)
    inp = int(input('\n Enter the specific level number for further information '))
    varn = varn[inp]
    temp1 = varn[0]
    temp1 = str(temp1)
    r = re.compile("([a-zA-Z]+)([0-9]+)")
    m = r.match(temp1)
    m1 = m.group(1)
    m2 = m.group(2)

    #NOT GATE BLOCK
    if (int(m2) == 1):
        print '\n Type of Gate used in Level-', inp, ': ', gate1
        print '\n Number of Control Variable(s) : 0'
        print '\n Number of Target Variable(s): 1'
        print '\n Target Variable , Line Number :- ', varn[1]

    #C-NOT GATE BLOCK
    if(int(m2) == 2):
        print '\n Type of Gate used in Level-', inp, ': ', gate2
        print '\n Number of Control Variable(s) : 1'
        print '\n Number of Target Variable(s): 1'
        print '\n Control Variable , Line Number :- ', varn[-2]
        print '\n Target Variable , Line Number :- ', varn[-1]

    #TOFFOLI GATE BLOCK
    if(m1 == 't'):
        if (int(m2) > 2):
            print '\n Type of Gate used in Level-',inp ,': ' , gate3
            print '\n Number of Control Variables : ', len(varn) - 1
            print '\n Number of Target Variable : 1'
            del varn[0]
            for im in range(len(varn)-1):
                print '\n Control Variable, Line Number :- ' , varn[im] , '\n'
            print '\n Target Variable, Line Number :- ' , varn[-1]

    #FREDKIN GATE BLOCK
    if(m1 == 'f' and m2 > 2):
        print 'Fredkin Gate'





with open('main1.tfc', 'r+') as file:
    for line in file:
        if line.strip() == 'BEGIN':
            break
    for line in file:
        if line.strip() == 'END':
            break
        line1 = re.split(',', line)

        # 1.1--block for level details.......
        var1 = str(line1[0])
        var1 = re.split(' ',var1)
        for iy in range(1,len(line1)):
            var1.append(line1[iy])
        var2.append(var1)
        #print('var2 final::', var2)

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
        line_final1 = ''.join(line_final)
        ff = open('main1.txt', 'a')
        ff.write(line_final1)
        ff.write('\n')
        ff.close()


with open('main1.txt', 'r+') as exp:
    for lenn in exp:
        if len(lenn) == 1:
            if lenn[0] == '\n':
                continue
        ax = lenn
        axx = re.split(',', ax)
        mn = len(axx)
        mn -= 1
        axx1 = str(axx[mn])
        axx2 = re.split('\n', axx1)
        axx[mn] = axx2[0]
        mn1 = len(axx)
        mn2 = mn1-1
        axx[mn2] = axx2[0]
        lenn = axx
        linen = list()
        for ii in range(len(lenn)):
            linen.append(lenn[ii])
            linen.append(',')
        del linen[-1]
        lenn = linen
        if len(lenn) == 1:
            benn = list(lenn)
            benn.append('=')
            benn.append('not')
            benn.append(' ')
            benn.append(benn[0])
            benn1 = ''.join(benn)
            tenn = open('tt_generator.py', 'a')
            tenn.write(benn1+'\n')
            tenn.close()
        if len(lenn) == 3:
            tren = list(lenn)
            nn = len(tren)
            tren1 = list(tren[nn-1])
            ty = len(tren1)
            ty -= 1
            if tren1[ty] == ' ':
                del tren1[ty]
            tren1.append('=')
            tren1.append(tren[0])
            tren1.append('')
            tren1.append('^')
            tren1.append('')
            tren1.append(tren[nn-1])
            tren2 = ''.join(tren1)
            if "'" in tren2:
                al = list(tren2)
                al.remove("'")
                print(al)
                al1 = ''.join(al)
                tren2 = al1
            tren3 = open('tt_generator.py', 'a')
            tren3.write(tren2+'\n')
            tren3.close()
            if "'" in str(lenn):
                neg_ctl(lenn)


        if len(lenn) > 3:
            list1 = list(lenn)
            num = len(list1)
            insert1 = num-1
            list2 = list1[insert1]
            list3 = list(list2)
            list3.append('=')
            list3.append('(')
            hg = len(list1)
            la_el = list1[hg-1]
            list1.insert(0, la_el)
            list1.insert(1, '=')
            list1.insert(2, '(')
            hg1 = len(list1)
            list1[hg1-2] = '^'
            list1.insert(hg1-2, ')')
            z = 4
            ven = len(list1)
            for i in list1:
                list1[z] = ' and '
                z += 2
                if z == ven-3:
                    break
            qwerty = ''.join(list1)
            vs = ''.join(list1)
            if "'" in vs:
                vss = re.split("'", vs)
                vss1 = ''.join(vss)
                qwerty = vss1
            qwerty1 = open('tt_generator.py', 'a')
            qwerty1.write(qwerty+'\n')
            qwerty1.close()
            if "'" in str(lenn):
                neg_ctl(lenn)


# 1--block for level detail(function)
u_ip = int(input('Want level detail if yes type 1 or 0'))
if(u_ip == 1):
    level_detail(var2)

import re
import string
#QUANTUM COST CALCULATION
def qc(gate,noInput):
    if ((gate=='t' or gate=='T') and (noInput==1 or noInput==2)):
        QC =1
        return QC
    elif ((gate=='t' or gate=='T') and noInput > 2 ):
        QC = ((2**noInput)-3)
        return QC
    elif ((gate=='f' or gate=='F') and noInput==2):
        QC=3
        return QC
    elif ((gate=='f' or gate=='F') and noInput>2):
        QC =((2 ** noInput) - 3)+2


def calQ():
    qcost =0
    for i in range(5): #len(varn) refers to no of gates present in circuit
        fo=open("main1.txt","r")
        g=fo.readline(1)#to find which gate is associated
        fo.close()
    #finds no of chracters in a line and no of inputs n
    fo = open("main1.txt", "r")
    data = fo.readline()
    words = string.split(data)
    chars = 0
    for j in words:
        chars = chars + len(j)
    if chars>=3:
        n=chars-((chars+1)/2)
    q=qc(g,n)
    qcost=qcost+q
    print ('quantum cost is' , qcost)
calQ()
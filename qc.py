li = [9,8,78,10,25,0]
print (li)
temp = 1
for i in range(len(li)):
    print ('outer loop' , li[i])
    for j in range(1,len(li)):
        print ('inner loop', li[j])
        if li[i] > li[j]:
            temp = li[i]
            li[i] = li[j]
            li[j] = temp
        else:
            temp = li[j]
            li[j] = li[i]
            li[i] = temp

var = 1
for io in range(len(li)):
    if li[io] > li[var]:
        temp = li[i]
        li[i] = li[j]
        li[j] = temp
    var += 1
    if len(li) == var:
        break


print(li)
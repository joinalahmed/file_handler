li = [9, 8, 78, 10, 25, 60]
print(li)
var1 = 1
temp_var = []
for i in range(len(li)):
    temp_var1 = li[i] + li[var1]
    temp_var.append(temp_var1)
    var1 += 1
    if var1 == len(li):
        break
print(temp_var)

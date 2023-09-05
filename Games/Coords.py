x = 505
y= 150
s =10
for i in range (s):
    line =''
    for j in range (s):
        line += str(x) + ',' + str(y) + '\t'
        y+=10
    print(line) 
    x+=10
input_str = input("Nhập X,Y: ")
diemensions=[int(x) for x in input_str.split(',')]
rowNum=diemensions[0]
colNum=diemensions[1]
multilist =[[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]=row*col
print (multilist)
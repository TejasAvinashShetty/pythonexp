import json

#float makes it 10.0 instead of 10
#max_val = float(input())
max_val = int(input())
filepudr = "square" + str(max_val)
f = open(filepudr,'r')
num = json.load(f)

f.close()
print("num",num)
'''
10
num [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

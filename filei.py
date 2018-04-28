import json





max_val = 20 #100,10
num = []
power2 = []
for i in range(max_val):
    num.append(i)
    p = i**2
    print(i,p)
    power2.append(p)


filepudr = "square" + str(max_val)

f = open(filepudr,'w')
#TypeError: dumps() takes 1 positional argument but 3 were given
#json.dumps(num,power2,f)
json.dump(num,f)
f.write('\n')
f.write('and here are the powers\n')
json.dump(power2,f)
f.close()

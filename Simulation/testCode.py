import math
# import numpy as np
a= '3'
b = '2'
c = '1'
d = ''
e = '5'
str_test = "%s,%s,%s,%s,%s" % (a,b,c,d,e)

f = str.split(str_test,',')
# f = np.array(f)
# f[f=='']=0
# print(str_test)
# print(len(str_test))
# print(f)
# print(len(f))
g=[]
for val in f:
    print(val)
    try:
        g.append(float(val))
    except:
        g.append(0)
    print(g)
h = 2+g[2]/5

print(h)

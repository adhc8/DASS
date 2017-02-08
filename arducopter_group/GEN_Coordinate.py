import random

f=open("Coordinate.txt","w")
# a=0
#
# for a in range(0,20):
y_coord=round(random.uniform(5,5.5),2)
str_coord=str(y_coord)
f.write('%s\n' % str_coord)
print(str_coord)
# a+=1


f.close()

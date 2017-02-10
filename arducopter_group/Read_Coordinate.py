import random
fName="Coordinate.txt"

y_coord=round(random.uniform(5,5.5),2)

print(type(y_coord))
str_coord=str(y_coord)
print(type(str_coord))
print(str_coord)

with open(fName, "r+") as f:
    f.write(str_coord)
    str_coordIN=f.readline(1)

    print(str_coordIN)


f.close()

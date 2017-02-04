
with open("Coordinate.txt") as f:
        content = f.readlines()
content = [x.strip('\n') for x in content]
print(content)
fl_content=[]

for item in content:
    fl_content.append(float(item))

print(fl_content)

f.close()

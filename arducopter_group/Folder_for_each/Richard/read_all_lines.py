with open("Coordinates.txt","r") as f:
	content = f.readlines()
lines = [x.strip() for x in content]
print(lines)
fl_lines = map(float,lines)
print(fl_lines)

for x in range(0,len(fl_lines)):
	print(fl_lines[x])

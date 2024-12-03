with open("AOC3.txt", "r") as file:
    data = file.read()

def regax(source):
	res=0
	for i in range(len(source)):
		a,b,c,d=0,0,0,0
		if source[i:i+4] == "mul(":
			if ")" in source[i+4:i+13] and "," in source[i+4:i+13]:
				c = source[i+4:i+13].find(",")
				d = source[i+4:i+13].find(")")
				a = int(source[i+4:i+4+c])
				b = int(source[i+5+c:i+4+d])
				res +=a*b
	return res

yey = True
ney = False
substr=[0]
for i in range(len(data)):
	if yey:
		if data[i:i+7] == "don't()":
			substr.append(i)
			yey = False
			ney = True
	if ney:
		if data[i:i+4] =="do()":
			substr.append(i)
			yey = True
			ney = False
substr.append(len(data))
data2 =""
for i in range(0,len(substr),2):
	data2 +=data[substr[i]:substr[i+1]]

print(regax(data))
print(regax(data2))
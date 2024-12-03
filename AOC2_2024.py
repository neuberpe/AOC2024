with open("test.txt", "r") as file:
    data = file.read().replace("\n", ",")
mylist = data.split(",")
res1=0

def positiv(list1):
	for j in list1:
		if j <= 0 or j > 3:
			return False
	return True

def negativ(list1):
	for j in list1:
		if j >= 0 or j < -3:
			return False
	return True

for i in mylist:
	f = list(map(int, i.split(" ")))
	part=[]
	for j in range(len(f)-1): part.append(f[j]-f[j+1])
	if positiv(part) or negativ(part):
		res1+=1
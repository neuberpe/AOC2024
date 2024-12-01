with open("AOC1.txt", "r") as file:
    data = file.read().replace("\n", ",")
mylist = data.split(",")
left, right,res1,res2 = [],[],0,0

for i in mylist:
	x=i.find("   ")
	left.append(int(i[0:x]))
	right.append(int(i[x+3:]))

left.sort()
right.sort()
for j in range(len(left)):
	res1 += abs(right[j]-left[j])
print(res1)

for k in left:
	res2 += right.count(k)*k
print(res2)


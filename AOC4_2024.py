with open("AOC4.txt", "r") as file:
    data = file.read().replace("\n", ",")
mylist = data.split(",")
xmax =len(mylist[0])
ymax =len(mylist)
res=0
word="XMAS"
rose=[[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]

for i in rose:
	for y in range(ymax):
		for x in range(xmax):
			if mylist[y][x]==word[0]:
				try:
					if mylist[y+i[1]*1][x+i[0]*1]==word[1] and x+i[0]*1 >= 0 and y+i[1]*1 >= 0:
						if mylist[y+i[1]*2][x+i[0]*2]==word[2] and x+i[0]*2 >= 0 and y+i[1]*2 >= 0:
							if mylist[y+i[1]*3][x+i[0]*3]==word[3] and x+i[0]*3 >= 0  and y+i[1]*3 >= 0:
								res+=1
				except:
					pass
print("Star 1: ",res)
res=0
for y in range (ymax-2):
	for x in range(xmax-2):
		if mylist[y+1][x+1]=="A":
			if mylist[y][x] =="S" and mylist[y+2][x+2] == "M" or mylist[y][x] =="M" and mylist[y+2][x+2] == "S":
				if mylist[y][x+2] =="S" and mylist[y+2][x] == "M" or mylist[y][x+2] =="M" and mylist[y+2][x] == "S":
					res+=1
print("Star 2: ",res)
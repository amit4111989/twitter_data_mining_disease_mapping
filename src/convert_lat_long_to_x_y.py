import math

mapWidth    = 200;
mapHeight   = 100;


file = open("user_dorm_data.csv",'r')
file2 = open("x_y.csv",'w+')
c = 0

for item in file:
	if c==0:
		c=c+1
		pass
	else:
		item = item.split(',')
		x = float(item[5])
		y = float(item[4])
		file2.write("\n%f"%(x))
		file2.write(' , ')
		file2.write("%f"%(y))










ids = []

count = 0

file = open("/Users/voldemort/normalized_data.csv","r")

for item in file:
	if count ==0:
		count = count+1
		pass
	else:
		item = item.split(',')
		if item[2].split('/')[0] == "10":
			print item[0]+','+item[1]+','+item[2]+','+item[3]+','+item[4]+','+item[5]
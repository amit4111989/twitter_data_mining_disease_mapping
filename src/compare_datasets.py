
ids = []

count = 0

file = open("/Users/voldemort/normalized_data1.csv","r")

for item in file:
	if count ==0:
		count = count+1
		pass
	else:
		item = item.split(',')
		if item[0] in ids:
			print item[0]
			pass
		else:
			ids.append(item[0])

# file2 = open("user_dorm_data.csv","r")

# id1 = []
# id2 = []
# id3 = []

# for item in file:
# 	item = item.split(",")
# 	id1.append(item[0])

# for item in file2:
# 	item = item.split(",")
# 	id2.append(item[0])

# count = 0

# for name in id2:
# 	if name in id1:
# 		pass
# 	else:
# 		id3.append(name)
# 		count = count+1

# file2 = open("user_dorm_data.csv","r")

# for item in file2:
# 	item = item.split(',')
# 	for i in id3:
# 		if i==item[0]:
# 			print item[0],",",item[1],",",item[2],",",item[3],",",item[4],",",item[5]

# print count



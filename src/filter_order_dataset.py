#-110.990089,32.154103,-110.896067,32.290116

#closer to campus

#-110.971206,32.221512,-110.930742,32.249185


file = open("normalized_data.csv","r")

count = 0

for item in file:
	if count==0:
		count = count+1
		pass
	else:
		item = item.split(',')
		print item[4] + ' ' + item[5]

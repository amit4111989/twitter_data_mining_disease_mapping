import csv

file = open('clean_dorm_data', 'r')

payload = file.read()
payload = payload.split('\n\n')
myfile = open('user_dorm_data.csv', 'wb')

a ='id, text, creation_date, creation_time, longitude, latitude'
myfile.write(a)


for data in payload:
	data_list = data.splitlines(True)
	data_list = data_list[1:]
	# a.write(data_list[0],data_list[0],)
	data_list = [data.replace('\n','') for data in data_list]
	print data_list
	if len(data_list)<4 or len(data_list)>4:
		pass
	else:
		myfile.write("\n%s,%s,%s,%s,%s,%s"%(data_list[0].split('id: ')[1],data_list[1].split('Text: ')[1].replace(',', ' '),data_list[2].split(' ')[1], data_list[2].split(' ')[2], data_list[3].split("lat/long : ")[1].split(',')[0][1:] , data_list[3].split("lat/long : ")[1].split(',')[1][:-1]))




pwd


import csv

data = open('example.csv')



csv_data=csv.reader(data)



data_lines=list(csv_data)



data_lines

data_lines[0]

len(data_lines)

for line in data_lines[:5]:
    print(line)

data_lines[10]

data_lines[10][8]

periods=[]

for line in data_lines[1:10]:
    periods.append(line[1])

periods

data_lines[10]

concanate=[]
for line in data_lines[1:10]:
    concanate.append(line[5]+" "+line[6])

concanate

file_to_output=open('to_save_file.csv',mode='w',newline='')

csv_write=csv.writer(file_to_output,delimiter=',')

csv_write.writerow(['a','b','c'])

csv_write.writerows([['1','2','3'],['4','5','6']])

file_to_output.close()

f=open('to_save_file',mode='a',newline='')

csv_write=csv.writer(f)

csv_write.writerow(['1','2','3'])

f.close

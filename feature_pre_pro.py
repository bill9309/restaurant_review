import csv
file_to_process = open('features.csv','r')
result_file = open('processed_features.csv','w')
reader = csv.reader(file_to_process)
result_file.write('feature')
for i in range(0,31):
    result_file.write(',comment_' + str(i))
result_file.write('\n')
for row in reader:
    result_file.write(row[0])
    for i in range(2,len(row)):
        result_file.write(',' + row[i])
    for i in range(len(row),31):
        result_file.write(',')
    result_file.write('\n')

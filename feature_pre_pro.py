import csv
import os
file_to_process = open('features.csv','r')
intermediate_file = open('intermediate.csv','w')
result_file = open('processed_features.csv','w')
reader = csv.reader(file_to_process)
intermediate_file.write('feature')
for i in range(0,31):
    intermediate_file.write(',comment_' + str(i))
intermediate_file.write('\n')
next(reader,None)
for row in reader:
    intermediate_file.write(row[0])
    for i in range(2,len(row)):
        intermediate_file.write(',' + row[i])
    for i in range(len(row),31):
        intermediate_file.write(',')
    intermediate_file.write('\n')
file_to_process.close()
intermediate_file.close()
read_intermediate_file = open('intermediate.csv','r')
for line in read_intermediate_file:
    in_tuple = False
    for i in range(0,len(line)):
        if line[i] == '(':
            in_tuple = True
        if line[i] == ')':
            in_tuple = False
        if in_tuple == True and line[i] == ',':
            result_file.write('#')
        else:
            result_file.write(line[i])
read_intermediate_file.close()
result_file.close()

import csv

file = open('staff.csv')

# csvreader = csv.reader(file)
#
#
# #read by line as list
# for line in csvreader:
#     print(line)

#read as dictionary

# csvreader_dictionary = csv.DictReader(file)
# for line in csvreader_dictionary:
#     print('Name: ', line['name'], "\n Position: ",
#           line['position'], "\n joining", line['joining'] ,
#           "\n Speciality: ", line['sepciality'])

# import csv
#
# with open('staff_file.csv', mode='w') as staff_file:
#     staff_writer = csv.writer(staff_file, delimiter=',')
#
#     staff_writer.writerow(['John Smith', 'Accounting', 'November'])
#     staff_writer.writerow(['Erica Meyers', 'IT', 'March'])


with open('employee_file2.csv', mode='w') as csv_file:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})

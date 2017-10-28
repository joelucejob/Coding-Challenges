import csv

with open('test.csv', 'rb') as csv_file:
    reader = csv.reader(csv_file)
    first_line = next(reader)
    for i in first_line:
        if i == 'bio':
            bio_field = i
    print bio_field
    #for row in reader:
        #print row
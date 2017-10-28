import csv
import re
import datetime

#TODO: deal with case sensitive

#Grab all lines of file and put them into a list
def get_data_in_csv_to_list(file_name):
    if file_name == None:
        return None
    with open(file_name, 'r') as file:
        file_reader = csv.reader(file)
        list = []
        for row in file_reader:
            if len(row) != 0:
                list += [row]
        return list

#Grab all lines of file and put them into a dict
def get_data_in_csv_to_dict(file_name):
    if file_name == None:
        return None
    with open(file_name, 'r') as file:
        file_reader = csv.reader(file)
        dict = {}
        for row in file_reader:
            if len(row) == 2:
                dict[row[0]] = row[1]
        return dict

#Finds the field with the name in the data set and returns the index
def get_field_index(data, cleaning_field):
    if len(data) == 0 or cleaning_field == None:
        return
    for i in range(len(data[0])):
        if data[0][i] == cleaning_field:
            return i

#swaps the data in a column with the given dictionary
def swap_data(data, swap_dict, swap_index):
    print 'Swapping data...'
    if len(data) < 2 or len(swap_dict) == 0 or swap_index == None:
        return
    for i in range(1, len(data)):
        if swap_index > (len(data[i])-1):
            continue
        if data[i][swap_index] in swap_dict:
            data[i][swap_index] = swap_dict[data[i][swap_index]]
        """
        key = data[i][swap_index]
        data[i][swap_index] = swap_dict[key]
        """
        
#removes all spaces and line breaks in specified data set
def clean_field(data, cleaning_index):
    print 'Cleaning data...'
    if len(data) < 2 or cleaning_index == None:
        return
    for i in range(1, len(data)):
        if cleaning_index > (len(data[i])-1):
            continue
        data[i][cleaning_index] = re.sub('\s+',' ', data[i][cleaning_index]).strip()

#saves the data into a csv file
def write_data_to_csv(csv_file_name, data):
    print 'Saving data...'
    with open(csv_file_name, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        writer.writerows(data)

#adds a new field column to data
def add_new_field(data, field_name):
    if len(data) == 0 or field_name == None:
        return
    data[0] += [field_name]
    for i in range(1, len(data)):
        data[i] += ['']

#checks field column for invalid offsets and modifies the data
def check_date_field(data, check_index, write_index, date_abbr, valid_days):
    if len(data) == 0 or check_index == None:
        return
    for i in range(1 , len(data)):
        #bounds checking
        if check_index > (len(data[i])-1) or write_index > (len(data[i])-1):
            continue
        #split up the string
        split = re.split('[-/, ]', data[i][check_index])
        result = convert_to_date_format(split, date_abbr, valid_days)
        if result == None:
            #TODO: is there a standard python swap method???
            data[i][check_index], data[i][write_index] = data[i][write_index], data[i][check_index]
            continue
        else:
            data[i][check_index] = result

#TODO: deal with case sensitive
#returns a string date if input is valid to be converted, else returns None
def convert_to_date_format(date, date_abbr, valid_days):
    if (len(date) != 3) and (len(date) != 4):
        return None

    #date_abbr = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06', 'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'}
    #valid_days = {'01':31, '02':29, '03':31, '04':30, '05':31, '06':30, '07':31, '08':31, '09':30, '10':31, '11':30, '12':31}

    #Only exist three formats
    #Alpha month, numeric day, numeric year
    #Numeric year, numeric month, numeric day
    #Numeric month, numeric day, numeric year

    result = []
    if is_valid_month(date[0], date_abbr, result):
        if len(result) != 0 and is_valid_day(date[1], result[-1], result, valid_days):
            if is_valid_year(date[-1], result):
                if len(result) == 3:
                    return '-'.join(result)

    result = []
    if is_valid_year(date[0], result):
        if is_valid_month(date[1], date_abbr, result):
            if len(result) != 0 and is_valid_day(date[-1], result[-1], result, valid_days):
                if len(result) == 3:
                    return '-'.join(result)
    print date
    return None

#checks if input is a valid year and adds it to the result list
def is_valid_year(year, result):
    if year == None:
        return False
    if len(year) == 4 and year.isdigit():
        result += [year]
        return True
    return False 

#checks if input is a valid month and adds it to the result list
def is_valid_month(month, date_abr, result):
    if month == None or date_abr == None:
        return False
    if month in date_abr:
        result += [date_abr[month]]
        return True
    if len(month) < 3 and month.isdigit() and int(month) < 13 and int(month) > 0:
        if len(month) == 1:
            result += ['0' + month]
        else:
            result += [month]
        return True
    return False

#checks if input is a valid day and adds it to the result list
def is_valid_day(day, month, result, valid_days):
    if month == None or day == None or valid_days == None:
        return False
    if len(day) < 3 and day.isdigit():
        if month in valid_days and int(day) <= valid_days[month] and int(day) > 0:
            if len(day) == 1:
                result += ['0' + day]
            else:
                result += [day]
            return True
    return False
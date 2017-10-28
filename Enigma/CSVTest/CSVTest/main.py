#Author: Joseph Luce
#Didn't think I really need any objects for this one so I went full procedural
#python is pretty fun, still don't think I do error checks as efficiently in Python

from tools import *
import csv

try:
    print "Starting..."

    STATE_CSV = 'state_abbreviations.csv'
    TEST_CSV = 'test.csv'
    CSV_FILE_NAME = 'solution.csv'
    CLEANING_FIELD = 'bio'
    SWAP_FIELD = 'state'
    DATE_OFFSET_FIELD = 'start_date'
    INVALID_FIELD_NAME = 'start_date_description'

    #month dictionary to numeric format
    date_abbr = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06', 'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'}
    #each month has a valid amount of days
    valid_days = {'01':31, '02':29, '03':31, '04':30, '05':31, '06':30, '07':31, '08':31, '09':30, '10':31, '11':30, '12':31}

    #grab the state abbreviations
    state_dict = get_data_in_csv_to_dict(STATE_CSV)
    #grab the test csv data
    test_data = get_data_in_csv_to_list(TEST_CSV)

    #clean spaces and new lines in bio field
    cleaning_index = get_field_index(test_data, CLEANING_FIELD)
    clean_field(test_data, cleaning_index)

    #swap the state field abbreviations
    code_swap_index = get_field_index(test_data, SWAP_FIELD)
    swap_data(test_data, state_dict, code_swap_index)

    #add a new start date desc field
    add_new_field(test_data, INVALID_FIELD_NAME)
    #check the date field and move invalid dates to the new start date field
    #change the current date field format
    date_offset_index = get_field_index(test_data, DATE_OFFSET_FIELD)
    date_desc_index = get_field_index(test_data, INVALID_FIELD_NAME)
    check_date_field(test_data, date_offset_index, date_desc_index, date_abbr, valid_days)

    #save date to a new csv file
    write_data_to_csv(CSV_FILE_NAME, test_data)

    print "Finished..."
except Exception as e:
    print str(e)

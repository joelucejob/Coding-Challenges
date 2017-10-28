from urlparse import urlparse
import os
import json

#Create a new file
def create_file(path, data):
    with open(path, 'w') as file:
        file.write(data)

#Add data into an exisiting file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

#Creates/Resets all necessary files
def create_all_files(base_url):
    queue = os.path.join('./', 'queue.txt')
    visited = os.path.join('./', 'visited.txt')
    json_path = os.path.join('./', 'solution.json')

    if os.path.isfile(queue):
        os.remove(queue)

    if os.path.isfile(visited):
        os.remove(visited)

    if os.path.isfile(json_path):
        os.remove(json_path)

    create_file(queue, base_url)
    create_file(visited, '')
    create_file(json_path, '')

#Dumps the data into a json file format
def save_data_to_json(data, json_file_name):
    print 'Saving data into json file...'
    with open(json_file_name, 'a') as outfile:
        json.dump(data, outfile, sort_keys = True, indent = 4, ensure_ascii = False)

#Grab all lines in file and put them into a set
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as file:
        for line in file:
            results.add(line.replace('\n', ''))
    return results

#For each line in a set, write it into the file
def set_to_file(links, file_name):
    with open(file_name, 'w') as file:
        for line in sorted(links):
            file.write(line + '\n')

#Parse the domain name out of url
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''

#Parse the sub domain name out of url
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
#Author: Joseph Luce
#Second attempt at python, was pretty fun, learned a lot, still need more practice :P
import threading
from Queue import Queue
from crawler import Crawler
from tools import *
import time

start_time = time.time()

print "Starting..."
START_PAGE = 'http://data-interview.enigmalabs.org/'
DOMAIN_NAME = get_domain_name(START_PAGE)

#I went with files to simulate databases, a bit slow but gets the job done
#Can easily switch to regular queues and sets, just testing python
QUEUE_FILE = 'queue.txt'
VISITED_FILE = 'visited.txt'
JSON_FILE = 'solution.json'

AMOUNT_OF_THREADS = 4
thread_queue = Queue()

#TODO: if data sets gets too large for memory, create custom methods to write to file set by set
#How to format data into json when all data isn't in a dictionary all at once??? Maybe try lists instead.
#Use a database as other alternative.
all_data = {}

def start_next_job(c):
    #queue polling
    while True:
        url = thread_queue.get()
        c.crawl_page(threading.current_thread().name, url, all_data)
        thread_queue.task_done()

def create_workers(c):
    for _ in range(AMOUNT_OF_THREADS):
        thread = threading.Thread(target=start_next_job, args = (c,))
        #makes sure threads die after main exits
        thread.daemon = True 
        thread.start()

def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        thread_queue.put(link)
    thread_queue.join()
    crawl()

def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        create_jobs()

c = Crawler(START_PAGE, DOMAIN_NAME, QUEUE_FILE, VISITED_FILE, JSON_FILE, all_data)
create_workers(c)
crawl()
save_data_to_json(all_data, JSON_FILE)
print 'Program took: %s' % (time.time() - start_time)
print "Finished..."
import urllib
from tools import *
from bs4 import BeautifulSoup
from urlparse import urljoin
import threading

print_lock, data_lock, queue_lock, visited_lock = (threading.Lock() for _ in range(4))

class Crawler():

    base_url = ''
    domain_name = ''
    queue_file = ''
    visited_file = ''
    json_file = ''
    queue = set()
    visited = set()

    def __init__(self, base_url, domain_name, queue_file_name, visited_file_name, json_file_name, all_data):
        Crawler.base_url = base_url
        Crawler.domain_name = domain_name
        Crawler.queue_file = queue_file_name
        Crawler.visited_file = visited_file_name
        self.boot()
        self.crawl_page('Initial Crawler', Crawler.base_url, all_data)

    #inital kickstart
    @staticmethod
    def boot():
        create_all_files(Crawler.base_url)
        Crawler.queue = file_to_set(Crawler.queue_file)
        Crawler.visited = file_to_set(Crawler.visited_file)

    #Starts viewing the page data
    @staticmethod
    def crawl_page(thread_name, page_url, all_data):
        try :
            with print_lock:
                print thread_name + ' visiting: ' + page_url

            with visited_lock:
                if page_url in Crawler.visited:
                    with print_lock:
                        print thread_name + ' already visited: ' + page_url
                    return
                Crawler.visited.add(page_url)
                set_to_file(Crawler.visited, Crawler.visited_file)

            opened_url = urllib.urlopen(page_url)
            soup = BeautifulSoup(opened_url.read(), 'html.parser')
            Crawler.gather_data(soup, all_data)
            all_links = Crawler.gather_links(soup)

            with queue_lock:
                Crawler.add_links_to_queue(all_links)
                Crawler.queue.remove(page_url)
                set_to_file(Crawler.queue, Crawler.queue_file)

            with print_lock:
                print thread_name + ' finished, queue size: ' + str(len(Crawler.queue)) + ' visited size: ' + str(len(Crawler.visited))
        except Exception as e:
            print str(e)

    #Gathers all the company data on the page
    @staticmethod
    def gather_data(soup, all_data):
        #return if this page doesn't contain data
        #TODO: is there a better way to do this?
        if (soup == None) or (soup.find('h4') == None) or (soup.find('span') == None):
            return
        company_name = soup.h4.span.text
        table_body = soup.tbody
        table_rows = table_body.find_all('tr')
        company_data = {}

        for tr in table_rows:
            td = tr.find_all('td')
            row = [str(i.text) for i in td]
            #TODO: fix indexing to accomodate more than two rows? Good enough for this toy problem
            if len(row) != 2:
                continue
            company_data[row[0]] = row[1]
        #save the data into our dictionary
        #As not being too familiar with json, there is a scenario where there can be duplicate company names.
        #I've tried using a list, but efforts have made the format not good for json.
        #How does one deal with duplicates when forced to use dictionary?
        #Is there some other structure I can use than a dictionary to store json data?
        with data_lock:
            all_data[str(company_name)] = company_data

    #Looks for all the links on the page
    @staticmethod
    def gather_links(soup):
        if soup == None:
            return
        #TODO: instead of adding all links seen, only add links that haven't been visited
        all_links = set()
        for link in soup.find_all('a'):
            url = urljoin(Crawler.base_url, link.get('href'))
            #print url
            all_links.add(url)
        return all_links

    #Adds all links that were found on the page to the queue
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if (url not in Crawler.queue) and (url not in Crawler.visited) and (Crawler.domain_name == get_domain_name(url)):
                Crawler.queue.add(url)
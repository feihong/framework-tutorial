"""
Decorator Recipe #2: Custom Event Binding (version 0)
"""
from threading import Thread
import time
    
class Downloader(object):
    def __init__(self, url_list):
        self.url_list = url_list
        self.done_callback = None

    def start_downloads(self):
        thread = Thread(target=self.download_all)
        thread.start()
    
    def download_all(self):
        count = 0
        start_time = time.time()
        
        for url in self.url_list:
            print 'Downloading', url
            time.sleep(0.3)
            count += 1

        end_time = time.time()
        if self.done_callback:
            self.done_callback(count, end_time - start_time)

if __name__ == '__main__':
    url_list = xrange(1, 13)
    downloader = Downloader(url_list)

    def ondone(num_downloaded, time_elapsed):
        print "Fetched", num_downloaded, "files in", time_elapsed, "seconds"

    downloader.done_callback = ondone

    downloader.start_downloads()

    print 'Waiting for the result...'

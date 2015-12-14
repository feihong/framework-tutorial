"""
Decorator Recipe #2: Custom Event Binding (version 2)

Changed the ``done`` decorator method to be able to handle multiple callback
functions.
"""
from threading import Thread
import time
    
class Downloader(object):
    def __init__(self, url_list):
        self.url_list = url_list
        self.callbacks = []

    def done(self, func):
        self.callbacks.append(func)
        return func

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
        for callback in self.callbacks:
            callback(count, end_time-start_time)

if __name__ == '__main__':
    url_list = xrange(1, 10)
    downloader = Downloader(url_list)

    @downloader.done
    def _(count, time_elapsed):
        print "Fetched", count, "files in", time_elapsed, "seconds"

    @downloader.done
    def _(count, time_elapsed):
        print '%s downloaded in %0.3f minutes' % (count, time_elapsed / 60.0)

    downloader.start_downloads()

    print 'Waiting for the result...'
    

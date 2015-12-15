Decorator Recipe: Custom Event Binding
======================================

Step 1
------
Instead of defining the callback and then binding it to the event, we want to do both at the same time:

.. sourcecode:: python

    @downloader.done
    def ondone(num_downloaded, time_elapsed):
        print "Fetched", num_downloaded, "files in", time_elapsed, "seconds"

To allow the above example to run, add a decorator method called ``done`` to class ``Downloader``.

.. sourcecode:: python

    from threading import Thread
    import time

    class Downloader(object):
        def __init__(self, url_list):
            self.url_list = url_list

        def done(self, func):
            """Add the code for this method"""

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
            self.callback(count, end_time-start_time)

    if __name__ == '__main__':
        url_list = xrange(1, 13)
        downloader = Downloader(url_list)

        @downloader.done
        def ondone(num_downloaded, time_elapsed):
            print "Fetched", num_downloaded, "files in", time_elapsed, "seconds"

    downloader.start_downloads()

    print 'Waiting for the result...'

Expected result::

    Waiting for the result...
    Downloading 1
    Downloading 2
    Downloading 3
    Downloading 4
    Downloading 5
    Downloading 6
    Downloading 7
    Downloading 8
    Downloading 9
    Downloading 10
    Downloading 11
    Downloading 12
    Fetched 12 files in 3.60899996758 seconds

Solution: :download:`solutions/downloader1.py`

.. hintlist::

  #. You need to assign the ``self.callback`` attribute.
  #. Implementing the ``done`` method requires no more than two lines of code.

:doc:`Go to next step <step2>`

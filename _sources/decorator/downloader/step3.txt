Decorator Recipe: Custom Event Binding
======================================

Step 3
------
We want the same multiple callback support, but now we'd like to implement it so that the callbacks are managed through an external class called ``EventBinder``.

Implement the ``EventBinder`` class.

.. sourcecode:: python

    from threading import Thread
    import time

    class EventBinder(object):
        """Implement the methods for this class"""

    class Downloader(object):
        def __init__(self, url_list):
            self.url_list = url_list
            self.done = EventBinder()

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
            self.done.fire(count, end_time-start_time)

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
    Fetched 9 files in 2.71900010109 seconds
    9 downloaded in 0.045 minutes

Solution: :download:`solutions/downloader3.py`

.. hintlist::

  #. ``EventBinder`` needs an attribute ``callbacks`` of type ``list``.
  #. ``EventBinder`` will need to implement the ``__call__`` magic method.
  #. The ``__call__`` magic method will be the decorator.
  #. ``EventBinder``'s ``fire`` method is responsible for invoking all of the callbacks stored in ``self.callbacks``.

:doc:`Go back <../index>`

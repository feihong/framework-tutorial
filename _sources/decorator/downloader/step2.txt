Decorator Recipe: Custom Event Binding
======================================

Step 2
------
Now we would like to support multiple callback functions:

.. sourcecode:: python

    @downloader.done
    def _(count, time_elapsed):
        print "Fetched", count, "files in", time_elapsed, "seconds"

    @downloader.done
    def _(count, time_elapsed):
        print '%s downloaded in %0.3f minutes' % (count, time_elapsed / 60.0)

Modify the methods in class ``Downloader`` to support this.

.. sourcecode:: python

    from threading import Thread
    import time

    class Downloader(object):
        """Write the methods for this class"""

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

Solution: :download:`solutions/downloader2.py`

.. hintlist::

  #. You will probably need to add a ``callbacks`` attribute, of type ``list``.
  #. Inside the ``done`` method, append the argument to ``self.callbacks``.
  #. Inside the ``download_all`` method, invoke each callback function in ``self.callbacks``.

:doc:`Go to next step <step3>`

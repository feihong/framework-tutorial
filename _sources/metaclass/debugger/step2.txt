Metaclass Recipe: Automatic Debugger Methods
============================================

Step 2
------
In this step, we will modify the ``get_debugger_func`` decorator to invoke the interactive debugger after printing the exception traceback.

Your task, once again, is to implement the ``__debugger__`` metaclass.

.. sourcecode:: python

    import inspect, traceback, sys, pdb

    def get_debugger_func(func):
        def new_func(*args):
            try:
                return func(*args)
            except Exception,e:
                traceback.print_exc()
                print '-'*80
                pdb.post_mortem(sys.exc_traceback)

        return new_func

    class __debugger__(type):
        """Define this class"""

    class Example(object):
        __metaclass__ = __debugger__

        def divide(self, v):
            # exception if v == 0
            result = 100 / v
            return result

        def interpolate(self, *args):
            # exception if len(args) != 2
            result = "%s is %s!" % args
            return result

    if __name__ == '__main__':
        e = Example()

        print e.divide(0)

        print '-'*80

        print e.interpolate('Feihong', 'very', 'cool')


Expected output::

    Traceback (most recent call last):
      File "D:\Projects\PyCon 2008 Talks\framework-tutorial\src\metaclass\debugger\solutions\debugger2.py", line 11, in new_func
        return func(*args)
      File "D:\Projects\PyCon 2008 Talks\framework-tutorial\src\metaclass\debugger\solutions\debugger2.py", line 33, in divide
        result = 100 / v
    ZeroDivisionError: integer division or modulo by zero
    --------------------------------------------------------------------------------
    > d:\projects\pycon 2008 talks\framework-tutorial\src\metaclass\debugger\solutions\debugger2.py(33)divide()
    -> result = 100 / v
    (Pdb) c
    None
    --------------------------------------------------------------------------------
    Traceback (most recent call last):
      File "D:\Projects\PyCon 2008 Talks\framework-tutorial\src\metaclass\debugger\solutions\debugger2.py", line 11, in new_func
        return func(*args)
      File "D:\Projects\PyCon 2008 Talks\framework-tutorial\src\metaclass\debugger\solutions\debugger2.py", line 38, in interpolate
        result = "%s is %s!" % args
    TypeError: not all arguments converted during string formatting
    --------------------------------------------------------------------------------
    > d:\projects\pycon 2008 talks\framework-tutorial\src\metaclass\debugger\solutions\debugger2.py(38)interpolate()
    -> result = "%s is %s!" % args
    (Pdb)


.. hintlist::

  #. The solution to this step is **very similar** to the solution from the last step.
  #. Actually, the definition of ``__debugger__`` is completely identical. This was just a trick question to see if you were paying attention.

Solution: :download:`solutions/debugger2.py`

:doc:`Go back <../index>`

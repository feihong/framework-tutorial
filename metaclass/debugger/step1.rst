Metaclass Recipe: Automatic Debugger Methods
============================================

Step 1
------
For now, let's not worry about invoking the debugger. We'll start by printing a traceback whenever an error occurs. For that, we'll use a decorator function called ``get_debugger_func``, which is already defined for you.

Your task is to define the ``__debugger__`` metaclass.

.. sourcecode:: python

    import inspect, traceback, pdb

    def get_debugger_func(func):
        def new_func(*args):
            try:
                return func(*args)
            except:
                traceback.print_exc()

        return new_func

    class __debugger__(type):
        """Define this class"""

    class Example:
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
      File "D:\Projects\PyCon 2008 Talks\framework-tutorial\src\metaclass\debugger\solutions\debugger1.py", line 9, in new_func
        return func(*args)
      File "D:\Projects\PyCon 2008 Talks\framework-tutorial\src\metaclass\debugger\solutions\debugger1.py", line 29, in divide
        result = 100 / v
    ZeroDivisionError: integer division or modulo by zero
    None
    --------------------------------------------------------------------------------
    Traceback (most recent call last):
      File "D:\Projects\PyCon 2008 Talks\framework-tutorial\src\metaclass\debugger\solutions\debugger1.py", line 9, in new_func
        return func(*args)
      File "D:\Projects\PyCon 2008 Talks\framework-tutorial\src\metaclass\debugger\solutions\debugger1.py", line 34, in interpolate
        result = "%s is %s!" % args
    TypeError: not all arguments converted during string formatting
    None
    >>>

.. hintlist::

  #. You will need to iterate through all the keys in ``classDict``.
  #. You have to test each value in ``classDict`` to see if it's a method.
  #. Remember that metaclasses cannot see methods as method objects, they only see function objects.
  #. Use the ``inspect.isfunction`` function.
  #. You need to replace each method in the target class with a method transformed by ``get_debugger_func``.

Solution: :download:`solutions/debugger1.py`

:doc:`Go to next step <step2>`

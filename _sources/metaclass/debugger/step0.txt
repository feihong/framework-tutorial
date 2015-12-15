Metaclass Recipe: Automatic Debugger Methods
============================================

Step 0
------

.. sourcecode:: python

    class Example:
        def divide(self, v):
            # exception if v == 0
            result = 100 / v
            return result

        def interpolate(self, *args):
            # exception if len(args) != 2
            result = "%s is %s!" % args
            return result

    if __name__ == '__main__':
        import pdb
        pdb.set_trace()

        e = Example()

        print e.divide(0)

        print '-'*80

        print e.interpolate('Feihong', 'very', 'cool')

Expected output::

    > d:\projects\pycon 2008 talks\framework-tutorial\src\metaclass\debugger\solutions\debugger0.py(19)<module>()
    -> e = Example()
    (Pdb) n
    > d:\projects\pycon 2008 talks\framework-tutorial\src\metaclass\debugger\solutions\debugger0.py(21)<module>()
    -> print e.divide(0)
    (Pdb) n
    ZeroDivisionError: 'integer division or modulo by zero'
    > d:\projects\pycon 2008 talks\framework-tutorial\src\metaclass\debugger\solutions\debugger0.py(21)<module>()
    -> print e.divide(0)
    (Pdb)

Solution: :download:`solutions/debugger0.py`

:doc:`Go to next step <step1>`

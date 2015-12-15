Frame Hack Recipe: Generating properties on a wrapper class
===========================================================

Step 1
------
Implement the ``properties`` function, using a frame hack. Feel free to use the ``eval`` function.

.. sourcecode:: python

    import sys
    from employee import Employee

    def properties(**kwargs):
        """Implement this function"""

    class PyEmployee(object):
        def __init__(self, **kwargs):
            self.e = Employee()
            for k, v in kwargs.items():
                setattr(self, k, v)

        properties(
            given  = 'GivenName',
            family = 'FamilyName',
            birth =  'DateOfBirth',
        )


    e = PyEmployee(given='Feihong', family='Hsu', birth='2007-11-15')

    print e.given, e.e.GetGivenName()

    e.given = 'Horatio'     # change given name through the property
    print e.given, e.e.GetGivenName()

Expected output::

    Feihong Feihong
    Horatio Horatio


.. hintlist::

  #. Remember that you can add properties to a class by modifying its frame.
  #. The frame object has a dictionary attribute called ``f_locals``, which you can modify.
  #. If you use ``eval``, you will also need to use ``lambda``.
  #. Your solution might contain the following line: ``for propname, realname in kwargs.items():``.
  #. Your solution might contain the following line: ``eval("lambda self: self.e.Get%s()" % realname),``.

Solution: :download:`solutions/wrapper1.py`

:doc:`Go to next step <step2>`

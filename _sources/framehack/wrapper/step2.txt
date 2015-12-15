Frame Hack Recipe: Generating properties on a wrapper class
===========================================================

Step 2
------
Implement the ``properties`` function, using a frame hack. This time, you are not allowed to use the ``eval`` function.

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

    e.family = 'Kodiak'
    print e.family, e.e.GetFamilyName()

    e.birth = '2009-12-23'
    print e.birth, e.e.GetDateOfBirth()

Expected output::

    Feihong Feihong
    Horatio Horatio
    Kodiak Kodiak
    2009-12-23 2009-12-23


.. hintlist::

  #. One possible strategy is to use a nested function to create the property.
  #. Your nested function might look like this::

      def get_property(name):
          def get(self):
              return getattr(self.e, 'Get'+name)()

          def set(self, value):
              getattr(self.e, 'Set'+name)(value)

          return property(get, set)

Solution: :download:`solutions/wrapper2.py`

:doc:`Go back <../index>`

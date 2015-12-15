Frame Hack Exercises
====================

.. exercise::

  Remove ``object`` as the superclass of ``PyEmployee``. How does the output change? Why does it make a difference if ``PyEmployee`` doesn't inherit from ``object``?

.. exercise::

  Change the ``properties`` function of Recipe #2 to match the code below. Does it still work as expected? Why or why not?

  .. sourcecode:: python

      def properties(**kwargs):
          framedict = sys._getframe(1).f_locals

          for propname, realname in kwargs.items():
              def get(self):
                  return getattr(self.e, 'Get'+realname)()

              def set(self, value):
                  getattr(self.e, 'Set'+realname)(value)

              framedict[propname] = property(get, set)


.. exercise::

  Implement the property generation functionality, this time using a metaclass. Make sure the following code behaves identically to our frame hack-based code:

  .. sourcecode:: python

      class __autoprops__(type):
          "Define this metaclass"

      class PyEmployee(object):
          __metaclass__ = __autoprops__

          def __init__(self, given_name, family_name, date_of_birth):
              self.e = Employee()
              self.given = given_name
              self.family = family_name
              self.birth = date_of_birth

          properties = {
              'given':  'GivenName',
              'family': 'FamilyName',
              'birth':  'DateOfBirth',
          }

.. exercise::

  [Advanced] Write two functions that print the last several frames, then run them multi-threaded 100 times and analyze the nature of frame tracing in a multi-threaded environment.  I just wanted to write down this thought before I forgot!

----

Do you want to understand frame hacks by learning from the masters themselves? Here are some Python modules that use frame hacks:

- Trellis_
- Elixir_
- Paste_
- zope.interface_

.. _Trellis: http://peak.telecommunity.com/DevCenter/Trellis
.. _Elixir: http://elixir.ematia.de/trac/wiki
.. _Paste: http://pythonpaste.org/
.. _zope.interface: http://www.zope.org/Products/ZopeInterface

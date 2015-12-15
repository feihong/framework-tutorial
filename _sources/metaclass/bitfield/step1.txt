Metaclass Recipe: Generating Bitfield Properties
================================================

Step 1
------
Finish implementing the inner function ``getproperty`` so that we can use bitprop

.. sourcecode:: python

    class __bitproperties__(type):
        def __new__(meta, classname, bases, classDict):
            for name in classDict['bit_properties']:
                def getproperty(enum):
                    # Change the code here
                    return property(lambda self: None,
                                    lambda self, value: None)

                enum = eval(name.upper())
                classDict[name] = getproperty(enum)

            return type.__new__(meta, classname, bases, classDict)

    ENABLED, SIMPLE, SUNKEN, RAISED, TRANSPARENT = 1, 2, 4, 8, 16

    class Widget(object):
        __metaclass__ = __bitproperties__
        style = 0
        bit_properties = ['enabled', 'simple', 'sunken', 'raised', 'transparent']

    w = Widget()
    w.enabled = True
    print w.style               # 1

    w.sunken = True
    print w.style               # 5

    w.transparent = True
    print w.style               # 21

    w.sunken = False
    print w.style               # 17

Expected output::

    1
    5
    21
    17


.. hintlist::

  #. The getter method for the property looks like this::

      def get(self):
          return bool(self.style & enum)

  #. The setter method for the property looks like this::

      def set(self, v):
          if v:
              self.style = self.style | enum
          else:
              self.style = self.style ^ enum

  #. Inside of ``getproperty``, you need to invoke the built-in function ``property``.

Solution: :download:`solutions/bitfield1.py`

:doc:`Go to next step <step2>`

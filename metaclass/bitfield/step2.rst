Metaclass Recipe: Generating Bitfield Properties
================================================

Step 2
------
It would be nice if we had more control over the names of the properties being generated. One way to allow would be to let you specify the properties using attributes:

.. sourcecode:: python

    class Widget(object):
        __metaclass__ = __bitproperties__
        style = 0

        enabled       = bit_property(ENABLED)
        simple_border = bit_property(SIMPLE)
        sunken_border = bit_property(SUNKEN)
        raised_border = bit_property(RAISED)
        transparent_background = bit_property(TRANSPARENT)

Implement the ``bit_property`` class and finish implementing the  ``__new__`` magic method.

.. sourcecode:: python

    class bit_property(object):
        """define this class"""

    class __bitproperties__(type):
        def __new__(meta, classname, bases, classDict):
            bitprops = (item for item in classDict.items()
                        if isinstance(item[1], bit_property))

            # Modify the classDict object here

            return type.__new__(meta, classname, bases, classDict)

    ENABLED, SIMPLE, SUNKEN, RAISED, TRANSPARENT = 1, 2, 4, 8, 16

    class Widget(object):
        __metaclass__ = __bitproperties__
        style = 0

        enabled       = bit_property(ENABLED)
        simple_border = bit_property(SIMPLE)
        sunken_border = bit_property(SUNKEN)
        raised_border = bit_property(RAISED)
        transparent_background = bit_property(TRANSPARENT)

    w = Widget()
    w.enabled = True
    print w.style               # 1

    w.sunken_border = True
    print w.style               # 5

    w.transparent_background = True
    print w.style               # 21

    w.sunken_border = False
    print w.style               # 17

Expected output::

    1
    5
    21
    17

.. hintlist::

  #. The definition of ``bit_property`` is pretty simple; all you need to provide is the ``__init__`` magic method.
  #. You can reuse the ``getproperty`` function from the previous step.
  #. One of the lines in your solution will likely be::

      classDict[name] = getproperty(bitprop.enum)

Solution: :download:`solutions/bitfield2.py`

:doc:`Go back <../index>`

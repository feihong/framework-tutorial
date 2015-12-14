Frame Hack Recipe: Ruby-Style String Interpolation
==================================================

Step 1
------
Implement the ``interpolate`` function, using a frame hack.

.. sourcecode:: python

    import sys
    from string import Template

    def interpolate(templateStr):
        """Implement this function"""

    name = 'Feihong'
    place = 'Chicago'
    print interpolate("My name is ${name}. I work in ${place}.")

Expected output::

    My name is Feihong. I work in Chicago.


.. hintlist::

  #. You can reuse some of the code from step 0.
  #. You have to use the ``sys._getframe`` function.

Solution: :download:`solutions/interpolate1.py`

:doc:`Go to next step <step2>`

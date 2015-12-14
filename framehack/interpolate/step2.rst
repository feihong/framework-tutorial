Frame Hack Recipe: Ruby-Style String Interpolation
==================================================

Step 2
------
Implement the ``interpolate`` function, using the ``getchunks`` function, which has been provided for you.

.. sourcecode:: python

    import sys, re
    from string import Template

    def getchunks(s):
        matches = list(re.finditer(r"\$\{(.*?)\}", s))

        if matches:
            pos = 0
            for match in matches:
                yield s[pos : match.start()]
                yield [match.group(1)]
                pos = match.end()
            yield s[pos:]

    def interpolate(templateStr):
        """Implement this function"""

    name = 'Guido van Rossum'
    places = 'Amsterdam', 'LA', 'New York', 'DC', 'Chicago',

    s = """My name is ${'Mr. ' + name + ', Esquire'}.

    I have visited the following cities:  ${', '.join(places)}.
    """

    print interpolate(s)


Expected output::

    My name is Mr. Guido van Rossum, Esquire.

    I have visited the following cities:  Amsterdam, LA, New York, DC, Chicago.


.. hintlist::

  #. You will have to use the built-in ``eval`` function.
  #. You should look closely at the return values of the ``getchunks`` function.
  #. You need to differentiate between chunks that need to be eval'ed and the chunks that don't need to be eval'ed.

Solution: :download:`solutions/interpolate2.py`

:doc:`Go back <../index>`   

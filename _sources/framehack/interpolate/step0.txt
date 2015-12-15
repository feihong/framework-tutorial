Frame Hack Recipe: Ruby-Style String Interpolation
==================================================

Step 0
------

.. sourcecode:: python

    from string import Template

    def interpolate(templateStr, d):
        t = Template(templateStr)
        return t.substitute(**d)

    name = 'Feihong'
    place = 'Chicago'
    print interpolate("My name is ${name}. I work in ${place}.", locals())

Expected output::

    My name is Feihong. I work in Chicago.

Solution: :download:`solutions/interpolate0.py`

:doc:`Go to next step <step1>`

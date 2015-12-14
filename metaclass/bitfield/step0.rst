Metaclass Recipe: Generating Bitfield Properties
================================================

Step 0
------

.. sourcecode:: python

    ENABLED, SIMPLE, SUNKEN, RAISED, TRANSPARENT = 1, 2, 4, 8, 16

    class Widget(object):
        style = 0

        enabled = property(
            lambda self: bool(self.style & ENABLED),
            lambda self, v: setattr(self, 'style',
                self.style | ENABLED if v else self.style ^ ENABLED),
        )
        simple = property(
            lambda self: bool(self.style & SIMPLE),
            lambda self, v: setattr(self, 'style',
                self.style | SIMPLE if v else self.style ^ SIMPLE),
        )
        sunken = property(
            lambda self: bool(self.style & SUNKEN),
            lambda self, v: setattr(self, 'style',
                self.style | SUNKEN if v else self.style ^ SUNKEN),
        )
        raised = property(
            lambda self: bool(self.style & RAISED),
            lambda self, v: setattr(self, 'style',
                self.style | RAISED if v else self.style ^ RAISED),
        )
        transparent = property(
            lambda self: bool(self.style & TRANSPARENT),
            lambda self, v: setattr(self, 'style',
                self.style | TRANSPARENT if v else self.style ^ TRANSPARENT),
        )

    w = Widget()
    w.enabled = True
    print w.style

    w.sunken = True
    print w.style

    w.transparent = True
    print w.style

    w.sunken = False
    print w.style

Expected output::

    1
    5
    21
    17

Solution: :download:`solutions/bitfield0.py`

:doc:`Go to next step <step1>`

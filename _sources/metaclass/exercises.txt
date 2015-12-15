Metaclass Exercises
===================

.. exercise::

  Try implementing Recipe #1 using a frame hack instead of a metaclass. What kind of issues do you run into? In your opinion, is this recipe more suitable to frame hacks or metaclasses?

.. exercise::

  Change the solution for Recipe #1 so that the ``__debugger__`` metaclass only transforms the target class's methods if a global variable called ``DEBUG`` is set to ``True``.

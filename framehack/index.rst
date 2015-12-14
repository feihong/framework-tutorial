===========
Frame Hacks
===========

.. contents:: :local:

Getting Started
===============

Introducing sys._getframe
-------------------------
.. sourcecode:: python

    import sys

    def one():
        two()

    def two():
        three()

    def three():
        for num in range(3):
            frame = sys._getframe(num)
            show_frame(num, frame)

    def show_frame(num, frame):
        print frame
        print "  frame     = sys._getframe(%s)" % num
        print "  function  = %s()" % frame.f_code.co_name
        print "  file/line = %s:%s" % (frame.f_code.co_filename, frame.f_lineno)

    one()

Expected output::

    <frame object at 0x606c50>
      frame     = sys._getframe(0)
      function  = three()
      file/line = stack.py:12
    <frame object at 0x180be10>
      frame     = sys._getframe(1)
      function  = two()
      file/line = stack.py:7
    <frame object at 0x608d30>
      frame     = sys._getframe(2)
      function  = one()
      file/line = stack.py:4

All frame hacks revolve around ``sys._getframe``. This special function allows us to get information from the frame of the calling function.   As you can see from above, Python creates a frame for every new call you make.  You can think of a frame object as being like an instance of a function.

Exploring frame objects
-----------------------
.. sourcecode:: python

    import sys, pdb

    def test():
        frame = sys._getframe(1)
        pdb.set_trace()

    def aFunction():
        a = 1
        b = 'hello'
        c = (12, 3.45)
        test()
        d = "This won't show up in the frame"

    aFunction()

Let's use the `Python Debugger`_ to interactively see what kinds of information the frame object stores. Attributes of the frame type are detailed in the Python `type reference`_.

.. _type reference: http://docs.python.org/lib/inspect-types.html
.. _Python Debugger: http://docs.python.org/lib/module-pdb.html

Using sys._getframe inside a class definition
-------------------------------------------------
.. sourcecode:: python

    import sys, pdb

    def test():
        frame = sys._getframe(1)
        pdb.set_trace()

    class Test(object):
        a = 1
        b = 'hello'
        c = (12, 3.45)
        test()
        d = "This won't show up in the frame"

The ``sys._getframe`` function works equally well with class frames. Once again, let's use the Python Debugger to see what kinds of information the frame object contains.

Note that the ``test`` function will not be able to access ``d`` because it is invoked before ``d`` is defined in the class.

What do we mean by "frame hack"?
================================

A frame hack is any code that inspects or modifies frame objects.

Use Cases
=========

Group related items inside a class definition (Trellis)
-------------------------------------------------------
Trellis_ is a framework that greatly simplifies event-driven programming. It provides you with functions that allow you to group the definitions of values and rules:

.. sourcecode:: python

    class TempConverter(trellis.Component):
        trellis.values(
            F = 32,
            C = 0,
        )
        trellis.rules(
            F = lambda self: self.C * 1.8 + 32,
            C = lambda self: (self.F - 32)/1.8,
        )

.. _Trellis: http://peak.telecommunity.com/DevCenter/Trellis

Trellis does not force you to use its grouping functions. You can alternatively define the ``TempConverter`` class like this:

.. sourcecode:: python

    class TempConverter(trellis.Component):
        F = trellis.value(32)
        C = trellis.value(0)

        F = trellis.rule(lambda self: self.C * 1.8 + 32)
        C = trellis.rule(lambda self: (self.F - 32)/1.8)

In this version, we lose some of the "structure" present in the original class definition. The code did get shorter (from 9 lines to 6), but at the expense of readability.

Verb-object style function call (Elixir)
----------------------------------------
.. sourcecode:: python

    class Movie(Entity):
        # ...
        belongs_to('genre', of_kind='Genre')

    class Genre(Entity):
        # ...
        name = Field(Unicode(20))

These kinds of function calls are used within class definitions. The name of the function is usually a verb and it accepts a parameter that is meant to be the "object" of the verb. They are meant to make class definitions read more like natural language. They always modify the frame of the class they are used in.

In the above code sample, the ``belongs_to`` function tells Elixir that the Movie entity is a child of the Genre entity.

For a more explicit definition, one could write the code like:

.. sourcecode:: python

    class Movie(Entity):
        genre = ManyToOne('Genre')

    class Genre(Entity):
        # ...
        name = Field(Unicode(20))

While this reveals the class attribute construction better, the relationship between ``Movie`` and ``Genre`` doesn't read as well.

Crazy monkey patching (lxml)
----------------------------

When writing doctests for code that produces XML there lies a problem in checking output.  Since XML is mostly ignorant of whitespace, your doctests become unecessarily fragile since whitespace is important.  To deal with this, the lxml_ library employs some impressive, realtime monkey patching to ignore whitespace.  Consider the following doctest:

.. sourcecode:: pycon

    >>> import lxml.html.usedoctest
    >>> import lxml.html
    >>> html = lxml.html.fromstring('''\
    ...    <html><body onload="" color="white">
    ...      <p>Hi  !</p>
    ...    </body></html>
    ... ''')
    ...
    >>> print lxml.html.tostring(html)
    <html> <body color="white" onload=""> <p>Hi    !</p> </body> </html>
    >>> print lxml.html.tostring(html)
    <html>
      <body color="white" onload="">
        <p>Hi !</p>
      </body>
    </html>

The two printed HTML strings are semantically equivalent when parsed by an HTML parser so the doctests should not fail.  However without a custom output checker they would fail since the attribute positions are switched and there is extra indentation and whitespace.

To address this the first statement, ``import lxml.html.usedoctest``, executes code that walks the frame stack backwards, locates the frame containing the doctest runner, clones its "check" function, resumes doctesting, then puts back the original check function.

Installing a custom output checker with Python 2.4's doctest is a cumbersome task.  One must instantiate several objects and pass those in to the test runner as it's created.  Most doctest based frameworks do not allow this level of customization and thus such a bold frame hack was devised.

.. _lxml: http://codespeak.net/lxml/
.. _lxml.doctestcompare: https://codespeak.net/svn/lxml/trunk/src/lxml/doctestcompare.py

Circumvent scope restrictions
-----------------------------
.. sourcecode:: python

    name = 'Feihong'
    place = 'Chicago'
    print interpolate("My name is ${name}. I work in ${place}.")

Expected output::

    My name is Feihong. I work in Chicago.

The ``interpolate`` function, implemented using a frame hack, is able to find the values for ``name`` and ``place`` by peering into the calling frame. (Assume that ``name`` and ``place`` are not global variables.)

Recipes
=======

Recipe #1: Ruby-style string interpolation
------------------------------------------
In this recipe, we'll show you how to implement Ruby-style string interpolation. You will create a function called ``interpolate`` that can evaluate a template string containing arbitrary Python expressions. For example:

.. sourcecode:: python

    from datetime import datetime

    numbers = [-3, 5, 66, 12, 76]
    startTime = datetime(2008, 1, 16, 16, 4)
    endTime = datetime(2008, 3, 13, 9, 30, 0)

    print interpolate('Took ${(endTime - startTime).seconds} seconds ' \
        'to get an average of ${sum(numbers) / len(numbers)}')

Expected output::

    Took 62760 seconds to get an average of 31

Prerequisites
`````````````
To fully understand the recipe, you'll need to know:

- `string.Template class`_
- `re.finditer function`_
- `yield statement`_

.. _string.Template class: https://docs.python.org/2/library/string.html#string.Template
.. _re.finditer function: https://docs.python.org/2/library/re.html#re.finditer
.. _yield statement: https://docs.python.org/2/reference/simple_stmts.html#the-yield-statement

Steps
`````
- :doc:`Interpolate 0 <interpolate/step0>`
- :doc:`Interpolate 1 <interpolate/step1>`
- :doc:`Interpolate 2 <interpolate/step2>`

Recipe #2: Generating properties on a wrapper class
---------------------------------------------------
Let's say that you have a C++ class that has a ton of setter and getter functions. Something like this:

.. sourcecode:: python

    class Employee
    {
        public:
            string GetGivenName();
            void SetGivenName(string value);

            string GetFamilyName();
            void SetFamilyName(string value);

            string GetDateOfBirth();
            void SetDateOfBirth(string value);

            // ad infinitum...
    };

Let's also assume that you used SWIG to create a wrapper class for ``Employee``. Now, you might like to make a nicer interface for this wrapper class by replacing each setter/getter pair with a corresponding property. This is the most straightforward way to do it:

.. sourcecode:: python

    class PyEmployee(object):
        def __init__(self, **kwargs):
            self.e = Employee()
            for k, v in kwargs.items():
                setattr(self, k, v)

        given = property(
            lambda self: self.e.GetGivenName(),
            lambda self, v: self.e.SetGivenName(v),
        )
        family = property(
            lambda self: self.e.GetFamilyName(),
            lambda self, v: self.e.SetFamilyName(v),
        )
        birth = property(
            lambda self: self.e.GetDateOfBirth(),
            lambda self, v: self.e.SetDateOfBirth(v),
        )

Pretty easy, right? But it's so much typing! What if you had a lot more getter/setter pairs to deal with? Or other wrapped classes with setter/getter pairs? You might be typing property definitions for a whole day!

Let's use a frame hack to simplify the definition of properties. Using our recipe, we'll be able to reduce the ``PyEmployee`` definition to this:

.. sourcecode:: python

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

This is not only shorter, but easier to read. And you're less likely to make a mistake typing all those lambda expressions.

Prerequisites
`````````````
- `property function`_
- `eval function`_
- `lambda expression`_
- closures_

.. _property function: https://docs.python.org/2/library/functions.html#property
.. _eval function: https://docs.python.org/2/library/functions.html#eval
.. _lambda expression: https://docs.python.org/2/tutorial/controlflow.html#lambda-expressions
.. _closures: http://www.shutupandship.com/2012/01/python-closures-explained.html

Steps
`````
- :doc:`Wrapper 0 <wrapper/step0>`
- :doc:`Wrapper 1 <wrapper/step1>`
- :doc:`Wrapper 2 <wrapper/step2>`

Frame Hack Caveats
==================

Not available everywhere
------------------------
It is important to keep in mind that frame hacks are, well, hacks. The ``sys._getframe`` function is not guaranteed to be available on every platform and implementation. For example, one implementation of Python that `does not support`_ ``sys._getframes`` is IronPython_.  And there may be complications with it in `Stackless Python`_.

.. _does not support: http://ironpython-urls.blogspot.com/2007/11/ironpython-and-python-stack-frames.html
.. _IronPython: http://codeplex.com/IronPython
.. _Stackless Python: http://www.stackless.com/

However, if you know that your library is only going to be used with CPython on a major platform (Linux, Mac, or Windows), then it's pretty safe to use frame hacks.

Messy when inheritance is involved
----------------------------------
Frame hacks that have to account for class inheritance get messy because superclasses and subclasses are always in different frames. It is is still possible to use them, because CPython's frame objects allow you to traverse the entire stack of frames. However, you'll end up writing a lot of extra code to figure out just how many frames you need to traverse.

Metaclasses are more flexible
-----------------------------
Many frame hacks scenarios, particularly those that work with classes, can be substituted by metaclasses. Metaclasses are more difficult to use, but also more powerful. We'll take a close look at metaclasses in another section of this tutorial.

:doc:`Exercises <exercises>`

:doc:`Go Back <../index>`

===========
Metaclasses
===========

.. contents:: :local:

What is a Metaclass?
====================

- A metaclass is like a decorator but for classes
- Specifically, a metaclass is a class that creates a class
- It's a class that gets invoked when it's assigned to the magic attribute ``__metaclass__``.

How Python normally creates class objects
=========================================

In Python code you create a class with the class keyword:

.. sourcecode:: pycon

    >>> class Fred(object):
    ...     hair_color = 'brown'
    ...
    >>> type(Fred)
    <type 'type'>
    >>> Fred.__name__
    'Fred'
    >>> Fred.hair_color
    'brown'

Here is an equivalent to what Python did behind the scenes:

.. sourcecode:: pycon

    >>> Fred = type('Fred', (object,), {'hair_color':'brown'})
    >>> type(Fred)
    <type 'type'>
    >>> Fred.__name__
    'Fred'
    >>> Fred.hair_color
    'brown'

Declaring ``__metaclass__`` allows you to customize class creation by overriding the default behavior of ``type()``.

Getting Started
===============

Introducing the __metaclass__ magic variable
--------------------------------------------
.. sourcecode:: python

    class __printer__(type):
        def __new__(meta, classname, bases, classDict):
            print 'Name            Type                 Value'
            print '-------------   ------------------   ---------------------------'
            for k, v in classDict.items():
                print '%-15s %-20s %r' % (k, type(v), v)

            return type.__new__(meta, classname, bases, classDict)

    class Test(object):
        __metaclass__ = __printer__
        a = 47
        b = 'raspberry'
        def c(self): pass
        d = property(lambda self: None)

Expected output::

    Name            Type                 Value
    -------------   ------------------   ---------------------------
    a               <type 'int'>         47
    __module__      <type 'str'>         '__main__'
    b               <type 'str'>         'raspberry'
    __metaclass__   <type 'type'>        <class '__main__.__test__'>
    d               <type 'property'>    <property object at 0x01A75850>
    c               <type 'function'>    <function c at 0x01A17F30>

The ``__test__`` metaclass prints out the members of its target classes. To make ``__test__`` the metaclass of ``Test``, we have to use the ``__metaclass__`` magic variable.

All metaclasses inherit from class ``type``. In most cases, you should override the ``__new__`` magic method to modify the elements of the ``classDict`` argument.  Modifying ``classDict`` has the effect of adding or modifying members of a class.

In most Python frameworks, metaclass usage is not explicit, because metaclasses are inherited by subclasses. This feature makes it easy to hide the metaclass machinery from your users. For example, Django's ``Model`` class uses a metaclass called ``ModelBase``. When you create models in Django, you inherit your model classes from ``Model`` and never have to explicitly use the ``__metaclass__`` attribute.

Distinguishing different types of class members
-----------------------------------------------
.. sourcecode:: python

    from inspect import isfunction, isdatadescriptor, isclass

    def separate_members(classDict):
        d = dict(methods=[], properties=[], other=[])

        for k, v in classDict.items():
            if isfunction(v):
                d['methods'].append(k)
            elif isdatadescriptor(v):
                d['properties'].append(k)
            elif not isclass(v):
                d['other'].append(k)

        return d

Function ``separate_members`` shows you how to distinguish between methods, properties, and all other attributes from inside the metaclass. Note that methods defined in the target class appear as functions to the metaclass, hence we use ``isfunction`` instead of ``ismethod``. Although we chose to use the ``inspect`` module for this example, it's possible to achieve equivalent functionality with the ``isinstance`` built-in function in conjunction with the ``types`` module.

Now to make use of the ``separate_members`` function we defined above:

.. sourcecode:: python

    class __printer__(type):
        def __new__(meta, classname, bases, classDict):
            d = separate_members(classDict)

            for k, v in d.items():
                print '%s:' % k
                for name in v:
                    print '- %s' % name
                print '-'*80

            return type.__new__(meta, classname, bases, classDict)

    class Test(object):
        __metaclass__ = __printer__
        a = 47
        b = 'raspberry'
        def c(self): pass
        d = property(lambda self: None)
        e = 45.67
        f = [23, 24, 25]
        g = lambda self: None
        def h(self, v): self.v = v
        i = property(c, h)

Expected output::

    other:
    - a
    - __module__
    - b
    - f
    - e
    --------------------------------------------------------------------------------
    properties:
    - d
    - i
    --------------------------------------------------------------------------------
    methods:
    - g
    - h
    - c
    --------------------------------------------------------------------------------

We make use of the ``separate_members`` function we defined in the previous section to allow metaclass ``__test__`` to print out the methods, descriptors, and other attributes of its target class.

Use Cases
=========

Generate attributes (Django)
----------------------------
.. sourcecode:: python

    from django.db import models

    class Poll(models.Model):
        question = models.CharField(maxlength=200)
        pub_date = models.DateTimeField('date published')

    class Choice(models.Model):
        poll = models.ForeignKey(Poll)
        choice = models.CharField(maxlength=200)
        votes = models.IntegerField()

This example was extracted from the `official Django tutorial`_. The ``Model`` class uses a metaclass that generates additional attributes. For example, ``Poll`` objects have attributes ``choice_set`` and ``objects`` that were generated based on the declared class attributes.

.. _official Django tutorial: http://www.djangoproject.com/documentation/tutorial01/

Modify class attributes
-----------------------
.. sourcecode:: python

    class GoBot(Robot):
        head      = Appendage()
        left_arm  = Appendage()
        right_arm = Appendage()

        cpu            = Component()
        matrix         = Component()
        flux_capacitor = Component()

    print GoBot.appendages
    print GoBot.components

Expected output::

    [Appendage<head>, Appendage<left_arm>, Appendate<right_arm>]
    [Component<cpu>, Component<matrix>, Component<flux_capacitor>]

Class ``Robot`` makes use of a metaclass (not shown) that causes all objects of type ``Appendage`` and ``Component`` to be added to the class attributes ``appendages`` and ``components``, respectively.

Transform methods and properties
--------------------------------
.. sourcecode:: python

    class Transformer(Robot):
        __metaclass__ = __timer__

        def transform(self):
            "Transform into a GM vehicle of some kind"
            #...

        def attack(self, target):
            "Attack something with robotic fury"
            #...

    t = Transformer()
    t.transform()
    t.attack(AdolfHitlerBot)

Expected output::

    Took 3.715 seconds to transform!
    Took 2.039 seconds to attack!

Class ``Transformer`` uses metaclass ``__timer__`` (not shown), which transforms each of ``Transformer``'s methods to print out the execution duration after the completion of each method.

Recipes
=======

Automatic Debugger Methods
--------------------------
This recipe shows you how you can focus your debugging on a specific class. In other words, have pdb run whenever any method of a class raises an exception.

.. sourcecode:: python

    class Example(object):
        __metaclass__ = __debugger__

        def divide(self, v):
            # exception if v == 0
            result = 100 / v
            return result

        def interpolate(self, *args):
            # exception if len(args) != 2
            result = "%s is %s!" % args
            return result

    e = Example()
    print e.divide(10)
    print e.divide(0)       # enters debugger

In this recipe, we'll explore how to transform all the methods of a class so that you automatically step into the debugger if and only if a method invocation triggers an error.

Prerequisites
`````````````
- closures_

Steps
`````
- :doc:`Debugger Step 0 <debugger/step0>`
- :doc:`Debugger Step 1 <debugger/step1>`
- :doc:`Debugger Step 2 <debugger/step2>`

Generating Bitfield Properties
------------------------------
We've all had to deal with libraries that use bitfields. It's especially common when dealing with wrapper libraries for C/C++ libraries. For this example, assume that we have a ``Widget`` class that has a bitfield attribute ``style``. After using this class for a while, you've gotten tired of having to write code like this:

.. sourcecode:: python

    w = Widget()
    w.style = ENABLED | SUNKEN | TRANSPARENT

Instead, you wish you could just write code like this:

.. sourcecode:: python

    w = Widget()
    w.enabled = True
    w.sunken = True
    w.transparent = True

The obvious way to do this would be to modify ``Widget`` to have a bunch of properties that modify the ``style`` attribute:

.. sourcecode:: python

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

If you're thinking "Gosh, it probably wasn't fun to type all that", you'd be totally right. Luckily for us, ever since Python 2.2 we've had a really good feature called metaclasses, which were created just for this kind of situation. Using a custom metaclass, we can rewrite the code like this:

.. sourcecode:: python

    class Widget(object):
        __metaclass__ = __bitproperties__
        style = 0
        bit_properties = ['enabled', 'simple', 'sunken', 'raised', 'transparent']

Here's another possible way to rewrite it, still using metaclasses:

.. sourcecode:: python

    class Widget(object):
        __metaclass__ = __bitproperties__
        style = 0

        enabled       = bit_property(ENABLED)
        simple_border = bit_property(SIMPLE)
        sunken_border = bit_property(SUNKEN)
        raised_border = bit_property(RAISED)
        transparent_background = bit_property(TRANSPARENT)

Prerequisites
`````````````
- Python's `binary bitwise operators`_
- `property function`_
- closures_

.. _binary bitwise operators: https://docs.python.org/2/reference/expressions.html?highlight=bitwise#binary-bitwise-operations

Steps
`````
- :doc:`Bitfield Step 0 <bitfield/step0>`
- :doc:`Bitfield Step 1 <bitfield/step1>`
- :doc:`Bitfield Step 2 <bitfield/step2>`

Metaclass Caveats
=================

Not as easy to use as frame hacks
---------------------------------
Sometimes what you want to do can be achieved using either a metaclass or a frame hack. How do you choose which to use? When prototyping, always go with the frame hack since it requires less effort. However, if you need your production code to be highly portable, use metaclasses. How you want your API to look is another consideration. Frame hacks add a different kind of structure to class definitions, and that may make your API look more elegant from a user's perspective.

Might generate extra classes
----------------------------
The ``__new__`` method of a metaclass returns a new ``type`` object. Because of the way that Python's import mechanism works, this may cause more than one class to be generated. In general, this shouldn't be a problem. But it may be something you want to keep in mind.

Makes a mess of your code
-------------------------
Excessive use of metaclasses can make your code harder to read and maintain. If you can achieve equivalent results using simpler approaches such as inheritance or frame hacks, use them instead.

:doc:`Exercises <exercises>`

:doc:`Go Back <../index>`

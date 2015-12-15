
=================================
Secrets of the Framework Creators
=================================

:Author: Feihong Hsu
:Contact: hsu.feihong@yahoo.com 847.219.6000
:Author: Kumar McMillan
:Contact: kumar.mcmillan@gmail.com 773.726.2397

.. contents:: :local:

Summary
=======

We Python programmers all have our favorite modules, such as Django, Elixir, Trellis, Breve, pyglet, etc. We use them because they save us time and allow us to write less code. We benefit from the day-to-day usage of these modules, but we can also benefit greatly from peeking under the hood and seeing how they do what they do. In many cases, these modules make liberal use of advanced Python features such as frames, metaclasses, magic methods, and decorators. In this tutorial we'll show you how to use these features to create compelling libraries and frameworks.

In total we'll go through 8 recipes, all culled from real-world code. As we go through the examples we'll show case studies where the same or similar technique is used in a popular module. These case studies help participants to precisely understand what problem the recipe attempts to solve. There will be a high emphasis on live coding. The authors will develop each example from scratch, stopping frequently to run the code and show what the current version is doing. Each example will be accompanied by exercises that can be attempted by more advanced programmers as they wait for novice programmers to ask questions and get answers.

Prerequisites
=============

This tutorial is targeted towards intermediate Python programmers. A lot of time will be given towards explaining and demonstrating concepts and syntax. However, the participant is supposed to know the following prior to attending this talk:

- How to use generators, list comprehensions, decorators, and the yield statement
- String interpolation. Knowing the string.Template class is helpful but not required.
- Regular expressions.
- Basic understanding of GUI concepts. Some familiarity with Tkinter is helpful but not required.
- A solid understanding of HTML and XML. It helps to know an XML processing library such as elementtree.
- Object-oriented programming in Python (inheritance, constructors, properties, etc.).
- How to use the bitwise operators ``(&, |, ^)``.
- Exception handling.
- Basic understanding of threads.

As for software, you won't need anything more than an installation of Python 2.4 or Python 2.5.

Presenter Bio
=============

Feihong Hsu
-----------

Feihong Hsu is a programmer working at Morningstar, Inc, in Chicago. He commutes daily from the wild and wolly exurbs of northwest Chicagoland. Although primarily a Python programmer, he has another, darker persona that dabbles in C#. The main crux of his job is to cajole, conflate, and massage vast quantities of financial data.

Kumar McMillan
--------------

Kumar McMillan lives in sunny Chicago, IL and works as a Senior Software Engineer at Leapfrog Online, LLC.  He uses Python to manage Leapfrog's ETL pipeline (Extracting, Transforming, and Loading data) as well as build web applications / services and automated testing strategies.  He is an active member of the open source community, maintaining several packages like fixture, wsgi_intercept, wikir, and helping out on nose, blogmaker and several others.  He writes about software from time to time on his blog, http://farmdev.com/

Presenter Experience
====================

Feihong Hsu
-----------

Feihong spent two years as a Computer Science teaching assistant at the University of Illinois at Chicago. Unlike other TAs, he had two or more lab sessions a week that were primarily planned and executed by himself. For his efforts he was awarded an Outstanding TA Award in 2003. He also spent a summer teaching an introductory programming course in JavaScript (where he was the primary instructor). He spent a school year teaching English to Chinese middle school students. Earlier this year in March he gave a talk at ChiPy entitled "Unicode for Small Children (and Children at Heart)". The slides for the talk can be found at http://feihonghsu.blogspot.com/2007/03/unicode-talk.html.

Kumar McMillan
--------------

After working on music at The School of the Art Institute of Chicago, Kumar naturally segued into self-taught computer science.  He began building websites in a little language called PHP and soon moved on to Python.  He created a consulting business in 2001 where he worked with clients like Selective Search, Inc and IBM Global Services.  In 2004, he became the third member of Leapfrog Online's technology department, working on web applications alongside Jason Pellerin and Michael Manley.  Together they built what is now a team of eight software engineers, two database administrators, and three quality assurance engineers.  Besides becoming enamored with the challenges and rewards of automated testing, Kumar has worked on several open source projects and given presentations such as "You vs. The Real World: Testing With Fixtures" (Pycon, 2007), "Python in TextMate Demo" (ChiPy, 2007), and "How To Get Started Writing OpenSocial Applications" (ChiPy, 2007).

.. admonition:: Recording:

    "I give permission to record and publish my PyCon presentation for free distribution."

Recipes
=======

The most common gotcha
----------------------

Stop! Before you attempt any of the recipes we are showing you today, check to make sure you are using new-style classes. That means your classes need to derive from object. In a lot of cases, the Python interpreter will not complain if you do not inherit from object, instead you'll just get really strange results.

Moral of the story:

Don't attempt super awesome hacks using old-style classes.

Frame Hack #1: Ruby-style string interpolation
----------------------------------------------

This is a very basic application of frames. Lets you write code like this:

::

    >>> name = 'Feihong'
    >>> place = 'Chicago'
    >>> print interpolate("My name is ${name}. I work in ${place}.")
    "My name is Feihong. I work in Chicago."

Frame Hack #1.5: Ruby-style string interpolation 2
--------------------------------------------------

It is easy to enhance the previous hack by allowing arbitrary Python expressions to be embedded in the template string. For example:

::

    >>> name = 'Feihong'
    >>> places = ['Chicago', 'Seattle', 'New York', 'LA']
    >>> print interpolate("My name is ${'Mr. ' name}. " \
                          "I have been to ${', '.join(places[:-1] + ', and ' + places[-1]}.")
    "My name is Mr. Feihong. I have been to Chicago, Seattle, New York, and LA."

Frame Hack #2: Generating properties in a wrapper class
-------------------------------------------------------

Let's say you have a C++ object that has a really annoying interface with a lot of getter and setter methods. You want to make a Pythonic wrapper that replaces those getters and setters with properties.

::

    # Pretend this was implemented in C++:
    class Employee(object):
        def __init__(self, given_name, family_name, date_of_birth):
            self.given_name = given_name
            self.family_name = family_name
            self.date_of_birth = date_of_birth

        def GetGivenName(self): return self.given_name
        def SetGivenName(self, value):  self.given_name = value
        def GetFamilyName(self): return self.family_name
        def SetFamilyName(self, value):  self.family_name = value
        def GetDateOfBirth(self): return self.date_of_birth
        def SetDateOfBirth(self, value):  self.date_of_birth = value
        # ad infinitum...

    # Let's make the property names shorter because we're lazy and don't like typing too much:
    class PyEmployee(Employee):
        properties(
            ('given', 'GivenName'),
            ('family', 'FamilyName'),
            ('birth', 'DateOfBirth'),
        )

    e = PyEmployee(given='Feihong', family='Hsu', birth='2007-11-19')
    e.given = 'Horatio'
    print e.given, e.given_name, e.GetGivenName()

.. admonition:: Notes:

    Would it be useful or confusing to make them leave out the object as the superclass of Employee? I was thinking it might be instructive, as having the code fail unexpectedly might help people remember to always inherit from object when dealing with properties.

Magic Method Hack #1: Generating hierarchical data
--------------------------------------------------
This is something that first appeared in stan, and now is seen in Breve. It allows you to use s-expressions to generate hierarchical data.

::

    dijit = Tag(open("dijitopen.txt").read(), "</body></html>")
    div = Tag("div")
    label = Tag("label")
    checkbox = Tag("input")(dojoType="dijit.form.CheckBox", type="checkbox",
                            checked="checked")
    textbox = Tag("input")(dojoType="dijit.form.TextBox", type="text")
    button = Tag("button")(dojoType="dijit.form.Button")
    datetextbox = Tag("input")(dojoType="dijit.form.DateTextBox", type="text")

    output = dijit [
        textbox(value="My hobby is collecting stamps"),
        button["Buy a stamp"],
        div [
            checkbox,
            label["Are you insane?"],
            datetextbox(value="2007-11-19"),
        ],
        div [
            button["Pause"],
            button["Play"],
            button["Stop"],
        ],
    ].tostring()

    open('output.html', 'w').write(output)

.. admonition:: Notes:

    This example is supposed to generate the HTML to render a Dijit interface (this works out well for demo purposes because the example could work without actually having to download Dojo itself, you could just reference the Amazon cached version). The code for this example turned out to be bit longer than I expected. In it you have to implement both __getitem__ and __call__. Although the example is more complicated than what you get with Breve, it illustrates that you can use this technique to generate arbitrary XML/HTML output. Extending it even further, you could use it to quickly define a transformation processor for any kind of semistructured input.

Magic Method Hack #2: Easy GUI layout
-------------------------------------

Similar to the previous example, but this time we're creating objects, not generating text. This hack also uses the sort of frame hack that is heavily used in libraries such as Elixir and Trellis.

::

    class Button(TkWrapper):
        wraps(tk.Button)

    class Label(TkWrapper):
        wraps(tk.Label)

    class HBox(TkWrapper):
        wraps(tk.Frame, is_container=True, orientation="horizontal")

    class VBox(TkWrapper):
        wraps(tk.Frame, is_container=True, orientation="vertical")

    frame = HBox() [
        Button(text='One'),
        Button(text='Two'),
        Button(text='Tree'),
        VBox() [
            Label(text='Apple'),
            Label(text='Banana'),
            Label(text='Cranberry'),
        ]
    ]
    frame.show()

.. admonition:: Notes:

    This example really involves a lot more than just __getitem__ magic method. It also uses a relatively simple frame hack. To convert the example to more usable code you'd have to implement the __getattr__ (for underlying Tkinter method access) and __call__ (so we can use the nicer tag-based API of the previous example) magic methods as well. I have some serious doubts about being able to cover all that in the given time, though.

Metaclass Hack #1: Painless bitfield properties
-----------------------------------------------

In this example, style is a bitfield attribute. We want to have a property for each possible bit of the style attribute.

::

    ENABLED, SIMPLE, SUNKEN, RAISED, TRANSPARENT = 1, 2, 4, 8, 16

    class Widget(object):
        __metaclass__ = __bitproperties__

        style = 0

        enabled = bit_property("style", ENABLED)
        simple = bit_property("style", SIMPLE)
        sunken = bit_property("style", SUNKEN)
        raised = bit_property("style", RAISED)
        transparent = bit_property("style", TRANSPARENT)

    print '-'*80

    w = Widget()
    w.enabled = True
    print w.style               # 1

    w.sunken = True
    print w.style               # 5

    w.transparent = True
    print w.style               # 21

    w.sunken = False
    print w.style               # 17

.. admonition:: Notes:

    The code here turned out longer and more complex than I expected. The reason may be that I don't understand how to work around Python's closure deficiencies well enough. I was forced to generate the code for the getter and setter as strings and then eval them. So it's a bit on the ugly side.

Metaclass Hack #2: Decorate all methods in a class
--------------------------------------------------

Both method1() and method2() print a stack trace when an error occurs, and go straight into the debugger; they do not terminate the program.

::

    DEBUG = True

    class Example:
        __metaclass__ = __debug__ if DEBUG else type

        def method1(self, v):
           result = 100 / v     # exception if v == 0
           return result

        def method2(self, *args):
           result = "%s is %s!" % args  # exception if len(args) != 2
           return result

.. admonition:: Notes:

    The way the methods will be decorated is we'll wrap the original function call inside a try block and use traceback.print_exc(file=sys.stdout) inside the except block. Then we just call pdb.set_trace() to enter the debugger.

Decorator Hack #1: Easy event binding
-------------------------------------
This style of decorator-based event binding can be found in pyglet.

::

    frame = Frame()
    frame.master.title("Event binding with decorators")
    frame.pack()

    btn = Button(frame, text="Click me!")
    btn.pack()

    @bind(btn, '<Button-1>')
    def onclick(evt):
        print 'You clicked on the button "%s"' % evt.widget['text']

    frame.mainloop()

.. admonition:: Notes:

    I got this idea from pyglet but it's somewhat different from pyglet because pyglet uses simple decorators that don't accept parameters. There is a variant of this where you allow the event callback to have different numbers of parameters by using function.func_code.co_argcount, but maybe that's making this example more complicated than it needs to be.

Decorate Hack #2: Custom event binding
--------------------------------------
Start the download off in another thread, then invoke the callback function when all files have been downloaded.

::

    downloader = Downloader(url_list)

    @downloader.done
    def ondone(num_downloaded, time_elapsed):
        print "Fetched", num_downloaded, "files in", time_elapsed, "seconds"

    downloader.start_downloads()

.. admonition:: Notes:

    This example shows how to use an object as a decorator. The actual decoration code is inside the __call__() magic method of the object. There are a few reasons why we might want to make the decorator an object instead of a function. Chief among them would be if we wanted to support different styles of event binding, for example downloader.done.register(callback) or downloader.done.deregister().

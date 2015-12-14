Introduction
============

Presenters
----------

**Feihong Hsu** lives in the wild and woolly exurbs of northwest Chicagoland. Although primarily a Python programmer, he has another, darker persona that dabbles in C#. Currently, he is between jobs and enjoying some time off. His previous job was at Morningstar Inc, where his responsibilities were to cajole, conflate, and massage vast quantities of financial data. He is the author of wxPita (a wrapper library for wxPython), and he blogs at http://feihonghsu.blogspot.com.

**Kumar McMillan** lives in sunny Chicago, IL and works as a Senior Software Engineer at Leapfrog Online, LLC. He uses Python to manage Leapfrog's ETL pipeline (Extracting, Transforming, and Loading data) as well as build web applications / services and automated testing strategies. He is an active member of the open source community, maintaining several packages like fixture, wsgi_intercept, wikir, and helping out on nose, blogmaker and several others. He writes about software from time to time on his blog, http://farmdev.com/.

Overview
--------

In this tutorial, we are going to show you how to take your Python programming to a higher level. We are not going to do this by throwing Scary Computer Science Stuff at you. There is no discussion of algorithms, runtime complexity, or data structures. We are simply going to make you aware of some advanced features of the Python programming language.

The features we will be covering are: frame hacks, magic methods, decorators, and metaclasses. We say that these features are "advanced" because they are used by only 10% of Python programmers (our unscientific estimate). That means that most of the code you see in the wild will not be using them. However, they show up a lot in popular Python frameworks, which implies that they are inordinately useful for creating abstractions. In other words, these features help you write more code upfront so that you can write less code overall. If you're just a user of a framework, you get the benefit of writing less code without having to write a large amount of code at the beginning.

This tutorial is not a comprehensive study of advanced Python techniques, and will not necessarily help you become an expert Pythonista. In fact, the presenters of this tutorial are not experts (note the lack of the words "expert", "guru", or "master" in our bios). However, even non-experts can make effective use of these features. The extra syntax you need to know is minimal, and should not give you any trouble if you have been using Python for a moderate amount of time. To ensure that you grasp the underlying concepts, we have a short, interactive tutorial corresponding to each feature.

The main difficulty, as we see it, is figuring out *when* to use these advanced features. To that end, we have included a number of use cases and recipes. The use cases include both case studies and somewhat-contrived examples that show you real-world scenarios under which a particular feature is used. The recipes help you gain programming experience on a particular feature. Only through repeated exposure to a feature will you truly "get it", but hopefully the recipes will set you on the right course.

There are eight recipes in all, two recipes for each feature. Because we have a limited amount of time, and because we do not know the average skill level of the participants, we do not know if we have a realistic shot at presenting all eight recipes. However, each recipe is designed to be relatively self-contained and includes all the information you need to complete it on your own. For example, each recipe includes several sequential "steps" that progressively build up to a complete program. Each recipe step includes hints and full solutions, in case you get stuck at any point. There is also the `Google Group`_ that the presenters have created. There you can post questions, ask for hints, and otherwise interact with the presenters as well as your fellow participants.

.. _Google Group: http://groups.google.com/group/secrets-of-the-framework-creators/


Introduction to PDB
-------------------
The ``pdb`` module provides a debugging support for Python. We are introducing ``pdb`` here because many Python programmers are not familiar with it, and we use it in a couple places in this tutorial.

One of the important things to understand is that ``pdb`` is both a program *and* a module. There are two main ways to use ``pdb``:

- Invoke the ``pdb.set_trace`` function. This is essentially the same as putting a breakpoint in your Python code.
- Run pdb as a standalone program (using the -m option of the Python interpreter). For example::

      python -m pdb program.py

Note that the first option enables debugging on a specific line, while the second enables debugging for your entire program.

Pdb is essentially a specialized Python interactive shell. It has a number of commands that are not available in the regular shell. Here are the most useful pdb commands:

h
    List all pdb commands. You can also use it to get specific details on each command.

l
    List source code. By default, it shows the current line of execution.

c
    Continue execution until a breakpoint is reached (or until the program ends).

n
    Move to the next line.

q
    Quit pdb.

To get used to pdb and what it can do, run the following code and try out the various pdb commands:

.. sourcecode:: python

    import pdb

    print 'Hello World'

    pdb.set_trace()

    sum = 0

    for i in range(5, 11):
        print i
        sum += i

    print sum

Magic Method Recipe: HTML Generation
====================================

Step 3
------
We want to go a little beyond Breve's functionality, to the point where we can define our own tags. For example:

.. sourcecode:: python

    checkbox = Tag('input', dojoType='dijit.form.CheckBox', type='checkbox')

When ``str`` is applied, the above tag produces the following HTML:

.. sourcecode:: html

    <input dojoType="dijit.form.CheckBox" type="checkbox" />

What does that give us, exactly? For one thing, it lets us more easily take advantage of Dijit_, a DHTML widget library.

.. _Dijit: http://dojotoolkit.org/projects/dijit

Implement the ``Tag`` class to support the proposed functionality. Note that the ``dijit`` function, which provides a template for Dijit-enabled pages, is already provided for you.

Implement the ``__call__`` and ``__getitem__`` magic methods.

.. sourcecode:: python

    import copy, webbrowser

    class Tag(object):
        # Implement this class

    def dijit(tag):
        return """<html><head>
    <title>Dijit Generation Example</title>
        <style type="text/css">
            @import "http://o.aolcdn.com/dojo/1.0.0/dijit/themes/tundra/tundra.css";
            @import "http://o.aolcdn.com/dojo/1.0.0/dojo/resources/dojo.css"
        </style>
        <script type="text/javascript" src="http://o.aolcdn.com/dojo/1.0.0/dojo/dojo.xd.js"
            djConfig="parseOnLoad: true"></script>
        <script type="text/javascript">
            dojo.require("dijit.form.Button");
            dojo.require("dijit.form.CheckBox");
            dojo.require("dijit.form.TextBox");
            dojo.require("dijit.form.DateTextBox");
            dojo.require("dojo.parser");
        </script>
    </head>
    <body class="tundra">%s</body></html>""" % str(tag)

    div = Tag('div')
    p = Tag('p')
    checkbox = Tag('input', dojoType='dijit.form.CheckBox', type='checkbox')
    textbox = Tag('input', dojoType='dijit.form.TextBox', type='text')
    button = Tag('button', dojoType='dijit.form.Button')
    datetextbox = Tag('input', dojoType='dijit.form.DateTextBox', type='text')

    if __name__ == '__main__':
        page = div [
            p [
                'This is a Button ',
                button['Click me!'],
            ],
            p [
                'This is a TextBox ',
                textbox(value='The cow jumped over the moon, and it exploded'),
            ],
            p [
                'This is a CheckBox ',
                checkbox(checked='checked'),
            ],
            p [
                'This is a DateTextBox ',
                datetextbox(value='1998-03-23'),
            ],
        ]

        html = dijit(page)
        print html
    ##    open('output.html', 'w').write(html)
    ##    webbrowser.open('output.html')

Expected output:

.. sourcecode:: html

    <html><head>
    <title>Dijit Generation Example</title>
        <style type="text/css">
            @import "http://o.aolcdn.com/dojo/1.0.0/dijit/themes/tundra/tundra.css";
            @import "http://o.aolcdn.com/dojo/1.0.0/dojo/resources/dojo.css"
        </style>
        <script type="text/javascript" src="http://o.aolcdn.com/dojo/1.0.0/dojo/dojo.xd.js"
            djConfig="parseOnLoad: true"></script>
        <script type="text/javascript">
            dojo.require("dijit.form.Button");
            dojo.require("dijit.form.CheckBox");
            dojo.require("dijit.form.TextBox");
            dojo.require("dijit.form.DateTextBox");
            dojo.require("dojo.parser");
        </script>
    </head>
    <body class="tundra"><div><p>This is a Button <button dojoType="dijit.form.Button">Click me!</button>
    </p>
    <p>This is a TextBox <input type="text" value="The cow jumped over the moon, and it exploded" dojoType="dijit.form.TextBox" />
    </p>
    <p>This is a CheckBox <input checked="checked" type="checkbox" dojoType="dijit.form.CheckBox" />
    </p>
    <p>This is a DateTextBox <input type="text" value="1998-03-23" dojoType="dijit.form.DateTextBox" />
    </p>
    </div>
    </body></html>


.. hintlist::

  #. You only need to make a minimal change to the previous version of the ``Tag`` class
  #. Specifically, you need to modify ``__init__``.
  #. You should change the signature of ``__init__`` to:  ``def __init__(self, name, **kwargs):``

Solution: :download:`solutions/html3.py`

:doc:`Go back <../index>`

Magic Method Exercises
======================

.. exercise::

  In Recipe #1, add a ``dump(tag, filename)`` function that generates output to a UTF-8 encoded file. (That is, it should be able to generate HTML pages that correctly display international characters.)

.. exercise::

  The calls to ``dojo.require()`` are hard coded inside the ``dijit`` function, which in general is not a good idea. Make it so that the require JavaScript section is dynamically generated based on what tags you use.

.. exercise::

  Add a ``load(filename)`` function that converts an XML file to a hierarchy of ``Tag`` objects. You should be able to process XML files like this:

  .. sourcecode:: xml

    <div>
        <p>
            This is a Button <button>Click me!</button>
        </p>
        <p>
            This is a TextBox <textbox value="The cow jumped over the moon, and it exploded" />
        </p>
        <p>
            This is a CheckBox <checkbox checked="checked" />
        </p>
        <p>
            This is a DateTextBox <datetextbox value="1998-03-23" />
        </p>
    </div>

.. exercise::

  Write a decorator for Django (or your web framework of choice) that allows you to do this::

      @dijit("view.xml")
      def view(request):
          return dict(name=request['name'], place=request['place'])

  Where ``view.xml`` is an XML template file that specifies a Dijit interface.


.. exercise::

  In Recipe #2, add a ``load(filename)`` function that converts an XML file to a ``ContainerWrapper`` object. You should be able to handle XML files like this

  .. sourcecode:: xml

    <VFrame>
        <Button text="One" />
        <Button text="Two" />
        <Button text="Tree" />

        <HFrame>
            <Button text="Apple" />
            <Button text="Banana" />
            <Button text="Cranberry" />
        </HFrame>
    </HFrame>

.. exercise::

  Implement Recipe #2 for wxPython_, PyQt_, or any other GUI framework of your choice.

.. _wxPython: http://wxpython.org
.. _PyQt: http://www.riverbankcomputing.co.uk/pyqt/

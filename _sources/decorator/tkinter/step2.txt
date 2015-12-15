Decorator Recipe: Event Binding in Tkinter
==========================================

Step 2
------
Unlike other event handling mechanisms in Tkinter, "command" callbacks do not accept the target widget.  This means that we can't do something like this:

.. sourcecode:: python

    @btn1.command
    @btn2.command
    def onclick(target):
        print 'You clicked on button <%s>' % target['text']

Modify the ``MyButton.command`` method to make the above example work correctly.

.. sourcecode:: python

    from Tkinter import *

    class MyButton(Button):
        def command(self, func):
            # Provide new logic here
            return func

    if __name__ == '__main__':
        frame = Frame()
        frame.master.title("Event binding with decorators")
        frame.pack()

        btn1 = MyButton(frame, text="One")
        btn1.pack()

        btn2 = MyButton(frame, text="Two")
        btn2.pack()

        @btn1.command
        @btn2.command
        def onclick(target):
            print 'You clicked on button <%s>' % target['text']

        frame.mainloop()

Expected output:

.. image:: tkinter-screenshot2.png


.. hintlist::

  #. You need to use a nested function (or a lambda).
  #. Remember that the 'command' callback is not allowed to take any arguments. That means you need to use a closure.
  #. Don't forget the return value!
  #. Your solution might contain the following expression: ``lambda: func(self)``.

Solution: :download:`solutions/tkinter2.py`

:doc:`Go to next step <step3>`

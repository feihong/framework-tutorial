Decorator Recipe: Event Binding in Tkinter
==========================================

Step 1
------
Subclass Tkinter's ``Button`` class and give it a decorator method.

.. sourcecode:: python

    from Tkinter import *

    class MyButton(Button):
        """Add a method to this class"""

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
        def onclick():
            print 'You clicked on a button'

        frame.mainloop()

Expected output:

.. image:: tkinter-screenshot.png


.. hintlist::

  #. Step 0 of this recipe is a big hint by itself.
  #. The name of the method is ``command``, and it needs to accept one parameter.
  #. You need to write at least two lines of code inside ``command``.
  #. Don't forget the return value.

Solution: :download:`solutions/tkinter1.py`

:doc:`Go to next step <step2>`

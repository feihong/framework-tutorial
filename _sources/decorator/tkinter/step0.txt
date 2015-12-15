Decorator Recipe: Event Binding in Tkinter
==========================================

Step 0
------
.. sourcecode:: python

    from Tkinter import *

    def onclick():
        print 'You clicked on a button'

    if __name__ == '__main__':
        frame = Frame()
        frame.master.title("Event binding with decorators")
        frame.pack()

        btn1 = Button(frame, text="One")
        btn1.pack()

        btn2 = Button(frame, text="Two")
        btn2.pack()

        btn1['command'] = onclick
        btn2['command'] = onclick

        frame.mainloop()

Expected output:

.. image:: tkinter-screenshot.png

Solution: :download:`solutions/tkinter0.py`

:doc:`Go to next step <step1>`

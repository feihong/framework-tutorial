Magic Method Recipe: Building Tkinter Interfaces
================================================

Step 0
------

.. sourcecode:: python

    from Tkinter import *

    root = Tk()
    root.title('A Tkinter Example')

    frame = Frame()
    frame.pack()

    Button(frame, text='One').pack(side=TOP, pady=5)
    Button(frame, text='Two').pack(side=TOP, pady=5)
    Button(frame, text='Three').pack(side=TOP, pady=5)

    frame2 = Frame(frame)
    frame2.pack(side=TOP, pady=5)

    Button(frame2, text='Apple').pack(padx=5, side=LEFT)
    Button(frame2, text='Banana').pack(padx=5, side=LEFT)
    Button(frame2, text='Cranberry').pack(padx=5, side=LEFT)

    Button(frame, text='Durian').pack(pady=5, side=BOTTOM)

    root.mainloop()

Expected output:

.. image:: tkinter-screenshot.png

Solution: :download:`solutions/tkinter0.py`

:doc:`Go to next step <step1>`

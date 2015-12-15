Magic Method Recipe: Building Tkinter Interfaces
================================================

Step 2
------
We still have not succeeded at making Tkinter layout not suck. That is because we still have to specify which side to pack each widget. Instead, it would be nice to have widget containers that know which side to pack their child widgets on:

.. sourcecode:: python

    # Pack everything from the top
    frame = VFrame [
        Button(text='One'),
        Button(text='Two'),
        Button(text='Tree'),
    ]

Implement the ``ContainerWrapper`` class to accomodate this functionality.

.. sourcecode:: python

    import copy, Tkinter as tk

    class TkWrapper(object):
        def __init__(self, cls):
            self.cls = cls
            self.args = {}

        def create_widget(self, parent):
            widget = self.cls(parent)
            for name, value in self.args.items():
                widget[name] = value
            return widget

        def __call__(self, **kwargs):
            wrapper = copy.deepcopy(self)
            wrapper.args.update(kwargs)
            return wrapper

    class ContainerWrapper(TkWrapper):
        """Implement this class"""

    Button = TkWrapper(tk.Button)
    Label = TkWrapper(tk.Label)
    HFrame = ContainerWrapper(tk.Frame, tk.LEFT)
    VFrame = ContainerWrapper(tk.Frame, tk.TOP)

    if __name__ == '__main__':
        frame = VFrame [
            Button(text='One'),
            Button(text='Two'),
            Button(text='Tree'),

            HFrame [
                Button(text='Apple'),
                Button(text='Banana'),
                Button(text='Cranberry'),
            ],

            Button(text='Durian')
        ]

        frame.show('A Cool Tkinter Example')

Expected output:

.. image:: tkinter-screenshot.png


.. hintlist::

  #. You can reuse a lot of code from the solution to the previous step.
  #. You will use the following line in your solution:  ``def __init__(self, cls, side):``.
  #. This is what your ``__init__`` method should look like::

      def __init__(self, cls, side):
          super(ContainerWrapper, self).__init__(cls)
          self.side = side
          self.children = []

  #. The ``create_widget`` method needs to take advantage of the ``self.side`` attribute.
  #. You will use the following line in your solution: ``childwidget.pack(side=self.side, padx=5, pady=5)``.

Solution: :download:`solutions/tkinter2.py`

:doc:`Go back <../index>`

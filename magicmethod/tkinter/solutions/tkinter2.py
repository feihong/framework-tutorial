"""
Magic Method #2: Easy GUI Layout (version 2)

Made changes to ``ContainerWrapper`` that allows you to forego the ``side``
constructor argument.
"""
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
    def __init__(self, cls, side):
        super(ContainerWrapper, self).__init__(cls)
        self.side = side
        self.children = []

    def __getitem__(self, children):
        wrapper = copy.deepcopy(self)
        if not isinstance(children, tuple):
            children = (children,)
        wrapper.children = children
        return wrapper

    def create_widget(self, parent):
        widget = super(ContainerWrapper, self).create_widget(parent)
        for child in self.children:
            childwidget = child.create_widget(widget)
            childwidget.pack(side=self.side, padx=5, pady=5)                
        return widget
        
    def show(self, title='window'):
        root = tk.Tk()
        root.title(title)

        frame = self.create_widget(root)
        frame.pack()
            
        root.mainloop()
    
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

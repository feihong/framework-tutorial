"""
Magic Method #2: Easy GUI Layout (version 1)
"""
import copy
import Tkinter as tk
from Tkinter import TOP, LEFT, BOTTOM, RIGHT

class TkWrapper(object):
    def __init__(self, cls):
        self.cls = cls
        self.args = {}

    def create_widget(self, parent):
        widget = self.cls(parent)
        for name, value in self.args.items():
            if name is not 'side':
                widget[name] = value                
        return widget

    def __call__(self, **kwargs):
        wrapper = copy.deepcopy(self)
        wrapper.args.update(kwargs)
        return wrapper

class ContainerWrapper(TkWrapper):
    def __init__(self, cls):
        super(ContainerWrapper, self).__init__(cls)
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
            childwidget.pack(side=child.args['side'], padx=5, pady=5)                
        return widget

    def show(self, title='window'):
        root = tk.Tk()
        root.title(title)

        frame = self.create_widget(root)
        frame.pack()
            
        root.mainloop()
    
Button = TkWrapper(tk.Button)
Label = TkWrapper(tk.Label)
Frame = ContainerWrapper(tk.Frame)

if __name__ == '__main__':
    frame = Frame [
        Button(text='One', side=TOP),
        Button(text='Two', side=TOP),
        Button(text='Tree', side=TOP),

        Frame(side=TOP) [
            Button(text='Apple', side=LEFT),
            Button(text='Banana', side=LEFT),
            Button(text='Cranberry', side=LEFT),
        ],
        
        Button(text='Durian', side=BOTTOM),
    ]
    
    frame.show('A Cool Tkinter Example')

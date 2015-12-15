"""
Decorator Recipe #1: Easy Event Binding (version 3)

Created a decorator called ``bind``, which accepts two arguments: the first
argument is a widget object, the second is event descriptor string. This
decorator is for binding callbacks to arbitrary widget events.
"""
from Tkinter import *

def bind(widget, event):
    def decorator(func):
        widget.bind(event, func)
        return func

    return decorator

if __name__ == '__main__':
    frame = Frame()                    
    frame.master.title("Event binding with decorators")
    frame.pack()

    lb = Listbox(frame, name='lb')
    for s in ['One', 'Two', 'Three', 'Four']:
        lb.insert(END, s)
    lb.pack()
    
    @bind(lb, '<<ListboxSelect>>')
    def onselect(evt):
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        print 'You selected item %d: "%s"' % (index, value)

    frame.mainloop()                  

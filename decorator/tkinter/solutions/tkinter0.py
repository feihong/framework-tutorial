"""
Decorator Recipe #1: Easy Event Binding (version 0)
"""
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

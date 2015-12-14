"""
Frame Hack Recipe #1: Ruby-style string interpolation (version 1)
"""
import sys
from string import Template

def interpolate(templateStr):
    frame = sys._getframe(1)
    framedict = frame.f_locals

    t = Template(templateStr)
    return t.substitute(**framedict)
    
name = 'Feihong'
place = 'Chicago'
print interpolate("My name is ${name}. I work in ${place}.")

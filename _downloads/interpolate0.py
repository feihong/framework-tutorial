"""
Frame Hack Recipe #1: Ruby-style string interpolation (version 0)
"""
from string import Template

def interpolate(templateStr, d):
    t = Template(templateStr)
    return t.substitute(**d)
    
name = 'Feihong'
place = 'Chicago'
print interpolate("My name is ${name}. I work in ${place}.", locals())

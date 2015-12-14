"""
Frame Hack Recipe #1: Ruby-style string interpolation (version 2)

Changed the ``interpolate`` function so that it correctly handles
arbitrary Python expressions inside the interpolation slots.
"""
import sys, re
from string import Template

def getchunks(s):
    matches = list(re.finditer(r"\$\{(.*?)\}", s))

    if matches:
        pos = 0
        for match in matches:
            yield s[pos : match.start()]
            yield [match.group(1)]
            pos = match.end()
        yield s[pos:]

def interpolate(templateStr):
    framedict = sys._getframe(1).f_locals

    result = ''
    for chunk in getchunks(templateStr):
        if isinstance(chunk, list):
            result += str(eval(chunk[0]))
        else:
            result += chunk
            
    return result
    
name = 'Guido van Rossum'
places = 'Amsterdam', 'LA', 'New York', 'DC', 'Chicago',

s = """My name is ${'Mr. ' + name + ', Esquire'}.

I have visited the following cities:  ${', '.join(places)}.
"""

print interpolate(s)


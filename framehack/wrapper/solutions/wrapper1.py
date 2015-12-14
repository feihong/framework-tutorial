"""
Frame Hack Recipe #2: Generating properties in a wrapper class (version 1)
"""
import sys
from employee import Employee

def properties(**kwargs):
    framedict = sys._getframe(1).f_locals

    for propname, realname in kwargs.items():
        framedict[propname] = property(
            eval("lambda self: self.e.Get%s()" % realname),
            eval("lambda self, value: self.e.Set%s(value)" % realname)
        )

class PyEmployee(object):
    def __init__(self, **kwargs):
        self.e = Employee()
        for k, v in kwargs.items():
            setattr(self, k, v)
            
    properties(
        given  = 'GivenName',
        family = 'FamilyName',
        birth =  'DateOfBirth',
    )


e = PyEmployee(given='Feihong', family='Hsu', birth='2007-11-15')

print e.given, e.e.GetGivenName()

e.given = 'Horatio'     # change given name through the property
print e.given, e.e.GetGivenName()

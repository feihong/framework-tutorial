"""
Frame Hack Recipe #2: Generating properties in a wrapper class (version 2)

Changed the ``properties`` function so that it doesn't use ``eval`` anymore.
"""
import sys
from employee import Employee

def properties(**kwargs):
    framedict = sys._getframe(1).f_locals

    for propname, realname in kwargs.items():
        def get_property(name):
            def get(self):
                return getattr(self.e, 'Get'+name)()
            
            def set(self, value):
                getattr(self.e, 'Set'+name)(value)

            return property(get, set)
        
        framedict[propname] = get_property(realname)

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

e.family = 'Kodiak'
print e.family, e.e.GetFamilyName()

e.birth = '2009-12-23'
print e.birth, e.e.GetDateOfBirth()


"""
Frame Hack Recipe #2: Generating properties in a wrapper class (version 0)
"""
from employee import Employee

class PyEmployee(object):
    def __init__(self, **kwargs):
        self.e = Employee()
        for k, v in kwargs.items():
            setattr(self, k, v)

    given = property(
        lambda self: self.e.GetGivenName(),
        lambda self, v: self.e.SetGivenName(v),
    )
    family = property(
        lambda self: self.e.GetFamilyName(),
        lambda self, v: self.e.SetFamilyName(v),
    )
    birth = property(
        lambda self: self.e.GetDateOfBirth(),
        lambda self, v: self.e.SetDateOfBirth(v),
    )

e = PyEmployee(given='Feihong', family='Hsu', birth='2007-11-15')

print e.given, e.e.GetGivenName()

e.given = 'Horatio'     # change given name through the property
print e.given, e.e.GetGivenName()

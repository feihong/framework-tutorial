"""
Metaclass Recipe #1: Painless bitfield properties (version 1)
"""

class __bitproperties__(type):
    def __new__(meta, classname, bases, classDict):
        for name in classDict['bit_properties']:
            def getproperty(enum):
                def get(self):
                    return bool(self.style & enum)

                def set(self, v):
                    if v:
                        self.style = self.style | enum
                    else:
                        self.style = self.style & ~enum

                return property(get, set)

            enum = eval(name.upper())
            classDict[name] = getproperty(enum)

        return type.__new__(meta, classname, bases, classDict)

ENABLED, SIMPLE, SUNKEN, RAISED, TRANSPARENT = 1, 2, 4, 8, 16

class Widget(object):
    __metaclass__ = __bitproperties__
    style = 0
    bit_properties = ['enabled', 'simple', 'sunken', 'raised', 'transparent']

w = Widget()
w.enabled = True
print w.style               # 1

w.sunken = True
print w.style               # 5

w.transparent = True
print w.style               # 21

w.sunken = False
print w.style               # 17

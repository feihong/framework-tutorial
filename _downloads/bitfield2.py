"""
Metaclass Recipe #1: Painless bitfield properties (version 2)

Changed so that you can specify your bit properties as members of the class.
"""
class bit_property(object):
    def __init__(self, enum):
        self.enum = enum

class __bitproperties__(type):
    def __new__(meta, classname, bases, classDict):
        bitprops = (item for item in classDict.items()
                    if isinstance(item[1], bit_property))

        for name, bitprop in bitprops:
            def getproperty(enum):
                def get(self):
                    return bool(self.style & enum)

                def set(self, v):
                    if v:
                        self.style = self.style | enum
                    else:
                        self.style = self.style & ~enum

                return property(get, set)

            classDict[name] = getproperty(bitprop.enum)

        return type.__new__(meta, classname, bases, classDict)

ENABLED, SIMPLE, SUNKEN, RAISED, TRANSPARENT = 1, 2, 4, 8, 16

class Widget(object):
    __metaclass__ = __bitproperties__
    style = 0

    enabled       = bit_property(ENABLED)
    simple_border = bit_property(SIMPLE)
    sunken_border = bit_property(SUNKEN)
    raised_border = bit_property(RAISED)
    transparent_background = bit_property(TRANSPARENT)

w = Widget()
w.enabled = True
print w.style               # 1

w.sunken_border = True
print w.style               # 5

w.transparent_background = True
print w.style               # 21

w.sunken_border = False
print w.style               # 17

"""
Metaclass Recipe #2: Debugger Methods (version 2)

Changed ``get__func`` step into pdb whenever an error occurs.
"""
import inspect, traceback, sys, pdb

def get_debugger_func(func):
    def new_func(*args):
        try:
            return func(*args)
        except Exception,e:
            traceback.print_exc()
            print '-'*80
            pdb.post_mortem(sys.exc_traceback)

    return new_func

class __debugger__(type):
    def __new__(meta, classname, bases, classDict):
        for name in classDict:
            obj = classDict[name]
            if inspect.isfunction(obj):
                classDict[name] = get_debugger_func(obj)

        return type.__new__(meta, classname, bases, classDict)

class Example(object):
    __metaclass__ = __debugger__

    def divide(self, v):
        # exception if v == 0
        result = 100 / v     
        return result

    def interpolate(self, *args):
        # exception if len(args) != 2
        result = "%s is %s!" % args  
        return result

if __name__ == '__main__':
    e = Example()

    print e.divide(0)

    print '-'*80
    
    print e.interpolate('Feihong', 'very', 'cool')

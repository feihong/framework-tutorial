"""
Metaclass Recipe #2: Debugger Methods (version 0)
"""
class Example:
    def divide(self, v):
        # exception if v == 0
        result = 100 / v     
        return result

    def interpolate(self, *args):
        # exception if len(args) != 2
        result = "%s is %s!" % args  
        return result

if __name__ == '__main__':
    import pdb
    pdb.set_trace()
    
    e = Example()

    print e.divide(0)

    print '-'*80
    
    print e.interpolate('Feihong', 'very', 'cool')

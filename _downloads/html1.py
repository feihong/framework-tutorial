"""
Magic Method Hack #1: Generating HTML (version 1)
"""
import copy

class Tag(object):
    def __init__(self, name):
        self.name = name
        self.attrs = {}
        self.children = []

    def items(self, **kwargs):
        tag = copy.deepcopy(self)
        tag.attrs.update(kwargs)
        return tag

    def append(self, *children):
        tag = copy.deepcopy(self)
        tag.children.extend(children)
        return tag

    def __str__(self):
        result = '<' + self.name
        if self.attrs:
            result += ' '
            result += ' '.join('%s="%s"' % item for item in self.attrs.items())
        if self.children:
            result += '>'
            result += ''.join(str(c) for c in self.children)
            result += '</%s>\n' % self.name
        else:
            result += ' />\n'
        return result
    
div = Tag('div')
img = Tag('img')
h1 = Tag('h1')
p = Tag('p')
a = Tag('a')

if __name__ == '__main__':
    print img.items(src='http://www.google.com/intl/en_ALL/images/logo.gif')

    e = div.items(id='address').append(
        p.items(id='line1').append('1313 Grisly Drive'),
        p.items(id='line2').append('Horrorville, IL 66666'),
    )
    print e
    

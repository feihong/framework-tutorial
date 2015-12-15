Magic Method Recipe: HTML Generation
====================================

Step 1
------
Here, we present an attempt at generating HTML using pure Python data structures. It is not very elegant, but gets the job done.

Read and understand what the following code is doing.

.. sourcecode:: python

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

Expected output:

.. sourcecode:: html

    <img src="http://www.google.com/intl/en_ALL/images/logo.gif" />

    <div id="address"><p id="line1">1313 Grisly Drive</p>
    <p id="line2">Horrorville, IL 66666</p>
    </div>

Solution: :download:`solutions/html1.py`

:doc:`Go to next step <step2>`

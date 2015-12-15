Magic Method Recipe: HTML Generation
====================================

Step 2
------
Using the ``item`` and ``append`` functions makes for some ugly, verbose code. This time, you will implement the same functionality, except that this time you will take advantage of Python's operators:

.. sourcecode:: python

    e = div(id='address') [
        p(id='line1') [ '1313 Grisly Drive' ],
        p(id='line2') [ 'Horrorville, IL 66666' ],
    ]

Implement the ``__call__`` and ``__getitem__`` magic methods.

.. sourcecode:: python

    import copy

    class Tag(object):
        def __init__(self, name):
            self.name = name
            self.attrs = {}
            self.children = []

        def __call__(self, **kwargs):
            # Implement this method

        def __getitem__(self, children):
            # Implement this method

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
        print img(src='http://www.google.com/intl/en_ALL/images/logo.gif')

        e = div(id='address') [
            p(id='line1') [ '1313 Grisly Drive' ],
            p(id='line2') [ 'Horrorville, IL 66666' ],
        ]
        print e

Expected output:

.. sourcecode:: html

    <img src="http://www.google.com/intl/en_ALL/images/logo.gif" />

    <div id="address"><p id="line1">1313 Grisly Drive</p>
    <p id="line2">Horrorville, IL 66666</p>
    </div>


.. hintlist::

  #. The implementation of ``__getitem__`` should not be identical to that of ``append``.
  #. Trying to do something like this will NOT work::

      def __getitem__(self, *children):
          tag = copy.deepcopy(self)
          tag.children.extend(children)
          return tag

  #. Inside ``__getitem__``, you need to do two different actions, depending on whether the ``children`` argument is a tuple or not.
  #. If it is a tuple, use ``list.extend``; if it is not a tuple, use ``list.append``.

Solution: :download:`solutions/html2.py`

:doc:`Go to next step <step3>`

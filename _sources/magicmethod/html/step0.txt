Magic Method Recipe: HTML Generation
====================================

Step 0
------

.. sourcecode:: python

    from string import Template

    greeting = 'Salutations'
    name = 'Abdullah'
    imgSrc = 'http://www.google.com/intl/en_ALL/images/logo.gif'
    link = 'http://feihonghsu.blogspot.com'

    template = Template("""\
    <div>
        <h1>
            ${greeting}, ${name}!
        </h1>

        <p>
            This is an image <img src="${imgSrc}" />
        </p>

        <p>
            Try clicking on the <a href="${link}">link</a> right now.
        </p>
    </div>""")

    html = template.substitute(**locals())
    print html

Expected output:

.. sourcecode:: html

    <div>
        <h1>
            Salutations, Abdullah!
        </h1>

        <p>
            This is an image <img src="http://www.google.com/intl/en_ALL/images/logo.gif" />
        </p>

        <p>
            Try clicking on the <a href="http://feihonghsu.blogspot.com">link</a> right now.
        </p>
    </div>

Solution: :download:`solutions/html0.py`

:doc:`Go to next step <step1>`    

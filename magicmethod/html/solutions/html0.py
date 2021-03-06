"""
Magic Method Hack #1: Generating HTML (version 0)
"""
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

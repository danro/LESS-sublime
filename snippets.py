import json
import sys
import urllib.request

template = """<snippet>
<content><![CDATA[
{snippet}
]]></content>
<tabTrigger>{trigger}</tabTrigger>
<description>{category}</description>
<scope>source.css.scss</scope>
</snippet>
"""

less_data = urllib.request.urlopen('https://raw.githubusercontent.com/less/less-docs/master/content/functions/data/functions.json')
data = json.load(less_data)

for group in data:
    descr = 'less ' + group.partition('-functions')[0]
    g = data.get(group)
    for function in g:
        name = function.get('name')
        example = function.get('example')

        snippet = open('Snippets/' + name + '.sublime-snippet', 'w')
        snippet.write(template.format(
            snippet=example,
            trigger=name,
            category=descr
            ))
        snippet.close()

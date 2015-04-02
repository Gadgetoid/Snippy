<!--JSON:{
	"tags": [
		"test",
		"example",
		"experiment"
	]
}-->
#Markson Code Example

This is a complete implementation of a Markson parser, in a Markson file.

Markson is a fusion of JSON and Markdown, using the structured data of JSON to embed data which can further describe
the markdown file in a much more structured and naturally easy to parse fashion.


```python
import json
import markdown
import re

def load(file):
	'''
	Loads and parses JSON-embedded Markdown file, chopping out and
	parsing any JSON contained therein.

	Returns an object that includes the JSON data, and the parsed HTML.
	'''
	markson = open(file).read()

	_data = re.search(re.compile(r'<!--JSON:(.*)-->', re.DOTALL),markson)

	_markdown = re.sub(re.compile(r'<!--JSON:(.*)-->', re.DOTALL),'',markson)
	_html = markdown.markdown(_markdown)

	if _data != None:
		_data = re.search('\{(.*)\}',_data.group(0),re.DOTALL).group(0)
		_data = json.loads(_data)

	return {'data':_data, 'html':_html}
```

JSON is embedded using a comment like the one below:


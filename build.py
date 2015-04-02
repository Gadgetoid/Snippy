#!/usr/bin/env python
import markson, os, time, sys, glob

base_url = "/snippy/"
resource_url = "/resources/"
src = "/src/"

snippets = glob.glob("src/snippets/*.md")

for file_path in snippets:
	loaded_file = markson.load(file_path)
	url = markson.slugify(loaded_file['data']['title'])
	print(url,loaded_file)
	print('')


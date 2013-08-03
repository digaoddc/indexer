
import re
import os
import sys

try:
    if not os.path.exists(sys.argv[1]):
	    sys.stderr.write('ERROR: File %s was not found!' % sys.argv[1])
	    sys.exit(1)
except IndexError:
    print 'Type the filename after index.py'  


def format_line(line, number):
	return line.rstrip()

def open_file():
	return open( sys.argv[1], "r+" )

def get_indexes():
	comments = []
	f = open_file()
	regex = re.compile('\/\/\s\=\=\s([\s\S]+)')
	count = 1

	for line in f:	
		res = regex.match(line)
		if res:
			comments.append({"text" : format_line(res.group(1), 
				count),"line" : count})
		count += 1
	f.close()
	return comments

def format_line_output(text,line):
	return "// "+text+" at line "+str(line)+"\n"

def markup(indexes):
	original_file_content = ""
	with open_file() as f:
	    original_file_content = f.read()
	with open( sys.argv[1], "wb+" ) as f:
		for i in indexes:
			f.write(format_line_output(i['text'], i['line']))
		f.write("\n\n")
		f.write(original_file_content)

def clear():
	#clear previous indexes
	pass

clear()
markup(get_indexes())
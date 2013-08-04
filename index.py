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
			comments.append({"text" : format_line(res.group(1), count)})
		count += 1
	f.close()
	return comments
 
def format_line_output(text,index):
	menuOpt = "0" + str(index) if index < 10 else str(index)
	return "  * " + menuOpt + ". " + text + "\n"
 
def markup(indexes):
	original_file_content = headerContent = headerTop = headerFooter = ""

	with open_file() as f:
	    original_file_content = f.read()


	with open( sys.argv[1], "wb+" ) as f:


		headerTop = "/**\n  * ========= TABLE OF CONTENTS =========\n  * \n"

		for idx,i in enumerate(indexes):

			headerContent += format_line_output(i['text'],idx+1)

		headerFooter = "  *\n  */\n\n"

		try:
			f.write(headerTop)
			f.write(headerContent)
			f.write(headerFooter)
			f.write(original_file_content)
			print 'CSS Indexed! :)'
		except :
			sys.stderr.write('Something went Wrong :(')
			# ? WILL THIS WORK ?
			f.write(original_file_content)


 
def clear():
	#clear previous indexes
	pass
 
clear()
markup(get_indexes())
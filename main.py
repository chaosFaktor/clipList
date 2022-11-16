import modules.flagloader as flagloader
import modules.ANSIcolour as ansi

import pyperclip as clp
import sys
import time



conf = flagloader.config()
conf.load()
print(conf.include)
print(conf.output)

def append_to_file(txt):
	print(ansi.BOLD+('new text detected!  »  ' + newTxt) + ansi.RESET)
	open('./out', 'a').write(txt)



oldTxt = ''
newTxt = ' '
while True:
	try:
		newTxt = str(clp.paste())
	except KeyboardInterrupt:
		print(ansi.RED+'Interrupted by user'+ansi.RESET)
		quit()
	except:
		print(ansi.Bold.RED+'could not get clipboard content!'+ansi.RESET)
	if newTxt != oldTxt and len(newTxt)>1:
		try:
			append_to_file(newTxt+'\n')
		except:
			print(ansi.Bold.RED+'could not write text to file'+ansi.RESET)
		oldTxt = newTxt

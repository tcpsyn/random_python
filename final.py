#!/usr/local/bin/python3

""" Final project"""

import sys
import re

def readfile(input_file):
	try:
		f=open(input_file,'r')
		data=f.readlines()
		f.close()
		return data
	except:
		print('Unable to open {0} for reading'.format(input_file))
		sys.exit(1)

def parsedata(data):
	wordlens={}
	for line in data:
		for word in line.split():
			regex=re.compile('[^A-Za-z]')
			word=regex.sub('',word)
			wordlen=len(word)
			
			if wordlen not in wordlens:
				if wordlen != 0:
					wordlens[wordlen]=1
			else:
				wordlens[wordlen] += 1
	return wordlens	

def displayresult(wordlens):
	print("Length Count")
	for k,v in wordlens.items():
		print('{0} {1}'.format(k,v))

if __name__ == '__main__':
	source_data=readfile(sys.argv[1])
	wordlens=parsedata(source_data)
	displayresult(wordlens)

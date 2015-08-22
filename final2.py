#!/usr/local/bin/python3

""" Final project"""

import sys
import re
import operator

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

def print_row(label, numwords, data):
	string=""
	for x in range(1, numwords):
		if x in data:
			string=string + data[x]
		else:
			string=string + "   "

	print('{0:<{col1}} - | {1}'.format(label, string, col1=3))

def merge_dicts(data):
	newdata={}
	for x in data:
		for k,v in x.items():
			newdata[k]=v
	return newdata

def displayhistogram(wordlens):
	sortedwords=sorted(wordlens.items(), key=operator.itemgetter(1), reverse=True)
	largest_word_len=max(sortedwords[1])
	numwords=len(wordlens) + 1
	agglengths=[]

	print('{0:<{col1}} - | {1}'.format('Len','Number of letters', col1=3))
	print('{0}'.format('-+' * 40))
	olddata=[]
	for x in reversed(range(0,largest_word_len + 20,20)):
		data={}
		for k,v in wordlens.items():
			if v >= x and v <= x+20:
				data[k]="***"
				olddata.append(data)
		data=merge_dicts(olddata)
		if x >= 20:
			print_row(x,numwords,data)

	print('{0}'.format('-+' * 40))
	footer=' '.join(str(x) for x in range(1, numwords ))
	print('{0:<{col1}} - | {1}'.format('0',footer, col1=3))

if __name__ == '__main__':

	if len(sys.argv) < 2:
		print("You must supply an argument")
		print("Usage: ./python2.py declaration.txt")
	else:
		source_data=readfile(sys.argv[1])
		wordlens=parsedata(source_data)
		#displayresult(wordlens)
		displayhistogram(wordlens)

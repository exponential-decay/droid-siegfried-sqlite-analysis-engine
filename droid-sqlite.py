# -*- coding: utf-8 -*-

from __future__ import division
import argparse
import sys
import sqlite3
import csv
import re
from urlparse import urlparse

def countFilesQuery(c):
	countfiles = "SELECT COUNT(NAME) FROM droid WHERE TYPE='File' OR TYPE='Container'"
	c.execute(countfiles)
	count = c.fetchone()[0]
	print "Number of Files in collection: " + str(count)
	return count

# Container objects known by DROID...
def countContainerObjects(c):
	countfiles = "SELECT COUNT(NAME) FROM droid WHERE TYPE='Container'"
	c.execute(countfiles)
	count = c.fetchone()[0]
	print "Number of Container objects in collection: " + str(count)
	
	countfiles = "SELECT DISTINCT EXT FROM droid WHERE TYPE='Container'"
	c.execute(countfiles)
	test = c.fetchall()
	for t in test:
		print t[0]
	
	return count
	
def countFilesInContainerObjects(c):
	countfiles = "SELECT COUNT(NAME) FROM droid WHERE URI_SCHEME!='file' AND (TYPE='File' OR TYPE='Container')"
	c.execute(countfiles)
	count = c.fetchone()[0]
	print "Number of Files inside container objects: " + str(count)
	return count

def countFoldersQuery(c):
	countfiles = "SELECT COUNT(NAME) FROM droid WHERE TYPE='Folder'"
	c.execute(countfiles)
	count = c.fetchone()
	print "Number of Folders in collection: " + str(count[0])
	return count

def countIdentifiedQuery(c):
	allcount = countFilesQuery(c)
	countfiles = "SELECT COUNT(NAME) FROM droid WHERE (TYPE='File' OR TYPE='Container') AND METHOD='Signature'"
	c.execute(countfiles)
	count = c.fetchone()[0]
	print "Number of Identified Files in collectionxx: " + str(count)
	
	if allcount > 0:
		percentage = (count/allcount)*100
		print "Percentage of the collection identified: " + '%.1f' % round(percentage, 1) + "%"
	else:
		print "Zero files" 
	return count

def countTotalUnidentifiedQuery(c):
	allcount = countFilesQuery(c)
	countfiles = "SELECT COUNT(NAME) FROM droid WHERE TYPE='File' OR TYPE='Container' AND (METHOD='no value' OR METHOD='Extension')"
	c.execute(countfiles)
	count = c.fetchone()[0]
	print "Number of Unidentified Files in collection (ext only and zero ID method): " + str(count)
	
	if allcount > 0:
		percentage = (count/allcount)*100
		print "Percentage of the collection unidentified: " + '%.1f' % round(percentage, 1) + "%"
	else:
		print "Zero files" 
	return count
	
def countZeroIDMethod(c):
	countfiles = "SELECT COUNT(NAME) FROM droid WHERE TYPE='File' OR TYPE='Container' AND METHOD='no value'"
	c.execute(countfiles)
	count = c.fetchone()[0]
	print "Number of Unidentified files (zero ID method): " + str(count)
	return count

def countExtensionIDOnly(c):
	countfiles = "SELECT COUNT(NAME) FROM droid WHERE TYPE='File' OR TYPE='Container' AND METHOD='Extension'"
	c.execute(countfiles)
	count = c.fetchone()[0]
	print "Number of Extension only identifications: " + str(count)
	return count

# PUIDS for files identified by DROID using binary matching techniques
def countSignaturePUIDS(c):
	countfiles = "SELECT COUNT(DISTINCT PUID) FROM droid WHERE (TYPE='File' OR TYPE='Container') AND (METHOD='Signature' OR METHOD='Container')"
	c.execute(countfiles)
	count = c.fetchone()[0]
	print "Number of unique 'signature' PUIDs: " + str(count)
	
	countfiles = "SELECT DISTINCT PUID FROM droid WHERE (TYPE='File' OR TYPE='Container') AND (METHOD='Signature' OR METHOD='Container')"
	c.execute(countfiles)
	test = c.fetchall()
	for t in test:
		print t[0]
	
	return count
	
def countExtensionPUIDS(c):
	countfiles = "SELECT COUNT(DISTINCT PUID) FROM droid WHERE TYPE='File' OR TYPE='Container' AND METHOD='Extension'"
	c.execute(countfiles)
	count = c.fetchone()[0]
	print "Number of unique 'extension' PUIDs: " + str(count)
	
	countfiles = "SELECT DISTINCT PUID FROM droid WHERE TYPE='File' OR TYPE='Container' AND METHOD='Extension'"
	c.execute(countfiles)
	test = c.fetchall()
	for t in test:
		print t[0]
	
	return count

def countExtensions(c):
	countfiles = "SELECT COUNT(DISTINCT EXT) FROM droid WHERE TYPE='File' OR TYPE='Container'"
	c.execute(countfiles)
	count = c.fetchone()[0]
	print "Number of unique extensions: " + str(count)
	
	countfiles = "SELECT DISTINCT EXT FROM droid WHERE TYPE='File' OR TYPE='Container'"
	c.execute(countfiles)
	test = c.fetchall()
	for t in test:
		print t[0]

	return count

def identifiedPUIDFrequency(c):
	test = "SELECT PUID, COUNT(*) AS total FROM droid WHERE (TYPE='File' OR TYPE='Container') AND (METHOD='Signature' OR METHOD='Container') GROUP BY PUID ORDER BY TOTAL DESC"
	c.execute(test)
	test = c.fetchall()
	return test

def allExtensionsFrequency(c):
	test = "SELECT EXT, COUNT(*) AS total FROM droid WHERE (TYPE='File' OR TYPE='Container') GROUP BY EXT ORDER BY TOTAL DESC"
	c.execute(test)
	test = c.fetchall()
	return test

def listTopTwenty(freqTuple, matchTotal, total, text):
	x = 0
	index = "null"
	for i,t in enumerate(freqTuple):
		if t[1] <= matchTotal:
			x = x + t[1]
			if x >= matchTotal:
				index = i
				break
	
	if index is not "null":
		print 
		print "Top 20% (out of " + str(total) + " ) " + text + ": "
		for i in range(index):
			print freqTuple[i][0] + "       COUNT: " + str(freqTuple[i][1])
	
	else:
		print "Format frequency: "
		for t in test:
			print freqTuple[i][0] + "       COUNT: " + str(freqTuple[i][1])

def paretoListings(c):
	# duplication in this function can potentially be removed through
	# effective use of classes...
	
	puidTotal = countIdentifiedQuery(c)
	puidPareto = int(puidTotal * 0.80)
	
	extTotal = countExtensions(c)
	extPareto = int(extTotal * 0.80)

	listTopTwenty(identifiedPUIDFrequency(c), puidPareto, puidTotal, "identified PUIDS")
	listTopTwenty(allExtensionsFrequency(c), puidPareto, extTotal, "format extensions")
	

def queryDB(c):
	countFilesQuery(c)
	countContainerObjects(c)
	countFilesInContainerObjects(c)
	countFoldersQuery(c)
	countTotalUnidentifiedQuery(c)
	countZeroIDMethod(c)
	countExtensionIDOnly(c)
	countSignaturePUIDS(c)
	countExtensionPUIDS(c)
	countExtensions(c)
	paretoListings(c)

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def detect_invalid_characters(s):
	#http://msdn.microsoft.com/en-us/library/aa365247(VS.85).aspx
	
	#Strings for unit tests
	test_strings = ['COM4', 'COM4.txt', '.com4', 'abccom4text', 'abc.com4.txt.abc', 'con', 'CON', '�', '�', '�', '���', '-=_|\"', '(<|>|:|"|/|\\|\?|\*|\||\x00-\x1f)']
	
	# First test, all ASCII characters?
	for s in test_strings:
		if not is_ascii(s):
			print "We have some characters outside of ASCII range: " + s
	
	#regex strings...
	
	#CON|PRN|AUX|NUL
	msdn_three_files = "(^)(con|prn|aux|nul)($|.|.[0-9a-zA-Z]{1,5}$)"
		
	#COM1-COM9 | LPT1-LPT9
	msdn_no_files = "((^)(COM|LPT)(.*[1-9]))($|(.[0-9a-zA-Z]{0,5}))"
	
	#<, >, :, ", /, \, ?, *, |, \x00-\x1f
	non_recommended_chars = '(<|>|:|"|/|\\|\?|\*|\||\x00-\x1f)'
	
	characters_regex = re.compile(non_recommended_chars, re.IGNORECASE)
	non_num_filename_regex = re.compile(msdn_three_files, re.IGNORECASE)
	num_filename_regex = re.compile(msdn_no_files, re.IGNORECASE)
		
	for s in test_strings:	
		char_tuples = re.findall(characters_regex, s)
		nonnum_tuples = re.findall(non_num_filename_regex, s)
		num_tuples = re.findall(num_filename_regex, s)
	
		if char_tuples:
			print "got some bad characters: " + s
		if nonnum_tuples or num_tuples:
			print "Got some bad filenames: " + s

def droidDBSetup(droidcsv):

	DROID_COLUMNS = 18

	print sqlite3.version
	
	conn = sqlite3.connect(droidcsv.replace(".csv", "") + ".db")
	
	c = conn.cursor()

	c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='droid';")

	# Can't DROP something that doesn't exist...
	if c.fetchone() is not None:
		c.execute("DROP table droid")	# DROP just in case

	# DROID Table: Standard Columns
	# ID, PARENT_ID, URI, FILE_PATH, NAME, METHOD, STATUS, SIZE, TYPE, 
	# EXT, LAST_MODIFIED, EXTENSION_MISMATCH, MD5_HASH, FORMAT_COUNT, PUID, 
	# MIME_TYPE, FORMAT_NAME, FORMAT_VERSION

	# Create table
	c.execute('''CREATE TABLE droid
					 (ID, PARENT_ID, URI, URI_SCHEME, FILE_PATH, NAME, METHOD, STATUS, SIZE, TYPE, EXT, LAST_MODIFIED, EXTENSION_MISMATCH, MD5_HASH, FORMAT_COUNT, PUID, MIME_TYPE, FORMAT_NAME, FORMAT_VERSION)''')

	URI_COL = 2

	with open(droidcsv, 'rb') as csvfile:
		droidreader = csv.reader(csvfile)
		for row in droidreader:
			rowstr = ""
			if droidreader.line_num != 1:								# ignore column headers
			
				for i,item in enumerate(row[0:DROID_COLUMNS]):
									
					if item == "":
						rowstr = rowstr + "'no value'"
					else:
						rowstr = rowstr + "'" + item + "'"
				
					if i == URI_COL:
						url = item
						rowstr = rowstr + ",'" + urlparse(url).scheme + "'"
	
					if i < DROID_COLUMNS-1:
						rowstr = rowstr + ","
				
				#test = "INSERT INTO stocks VALUES (" + rowstr + ")"
				#print test
				
				c.execute("INSERT INTO droid VALUES (" + rowstr + ")")

	# Save (commit) the changes
	conn.commit()

	### TEMPORARY READ FUNCTIONS ###

	queryDB(c)

	detect_invalid_characters("test")


	### TEMPORARY READ FUNCTIONS ###


	# We can also close the connection if we are done with it.
	# Just be sure any changes have been committed or they will be lost.
	conn.close()

def handleDROIDCSV(droidcsv):
	droidDBSetup(droidcsv)

def main():

	#	Usage: 	--csv [jp2file]

	#	Handle command line arguments for the script
	parser = argparse.ArgumentParser(description='Place DROID profiles into a SQLite DB')
	parser.add_argument('--csv', help='Optional: Single DROID CSV to read.')
	
	#parser.add_argument('--pro', help='Optional: XML profile to validate against.', default=False)
	#parser.add_argument('--dif', help='Optional: Generate diff in errorlog if validation fails.', default=False)

	if len(sys.argv)==1:
		parser.print_help()
		sys.exit(1)

	#	Parse arguments into namespace object to reference later in the script
	global args
	args = parser.parse_args()
	
	if args.csv:
		handleDROIDCSV(args.csv)			
	else:
		sys.exit(1)

if __name__ == "__main__":
	main()

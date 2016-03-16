import os
import sys 
import sqlite3
import hashlib
import time
import datetime
import csv
from urlparse import urlparse
from GenerateBaselineDBClass import GenerateBaselineDB

class DROIDLoader:

   csvcolumncount = 0
   moduleversion = sqlite3.version
   sqliteversion = sqlite3.sqlite_version
   contenthash = 0
   timestamp = 0
   hashtype = 0

   #DROID SPECIFIC COLUMN INDEXES
   #zer0-based index
   URI_COL = 2
   PATH_COL = 3
   DATE_COL = 10
   
   #better way to handle this? 
   #avoid overflow for multiple-ids
   LAST_COL = 18

   #Database metadata table, data about the content of the table...
   def createDBMD(self, cursor):
      self.dropDBMDTable(cursor)
      cursor.execute("CREATE TABLE dbmd (CONTENT_MD5, TIMESTAMP, HASH_TYPE)")
      cursor.execute("INSERT INTO dbmd VALUES ('" + str(self.contenthash) + "', '" + str(self.timestamp) + "', + '" + str(self.hashtype) + "')")

   def createDROIDTable(self, cursor, csvcolumnheaders):
      # turn csv headers list into a csv string, write query, create table

      self.csvcolumncount = len(csvcolumnheaders)
      columns = ""
      for header in csvcolumnheaders:
         if header == "URI":
            columns = columns + header + ", " + "URI_SCHEME, "
            self.csvcolumncount+=1
         elif header == "FILE_PATH":
            columns = columns + header + ", " + "DIR_NAME, "
            self.csvcolumncount+=1
         elif "_HASH" in header:    #regex alternative: ^([[:alnum:]]*)(_HASH)$
            self.hashtype = header.split('_', 1)[0]
            columns = columns + "HASH" + ", "
         elif header == "LAST_MODIFIED":
            columns = columns + header + " TIMESTAMP" + ","
            columns = columns + "YEAR INTEGER" + ","
         else:
            #sys.stderr.write(header + "\n")
            columns = columns + header + ", "

      cursor.execute("CREATE TABLE droid (" + columns[:-2] + ")")
      return True

   def dropTable(self, cursor, tablename):
      # If we've a db already, can check it has a droid table
      cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='" + tablename + "';")
      # Can't DROP something that doesn't exist...
      if cursor.fetchone() is not None:
         cursor.execute("DROP table " + tablename + "")	# DROP just in case

   def dropDROIDTable(self, cursor):
      self.dropTable(cursor, 'droid')
      return

   def dropDBMDTable(self, cursor):
      self.dropTable(cursor, 'dbmd')

   def userOverwriteOption(self, conn, msg):
      user_input = raw_input("DROID DB file exists, " + msg + " Overwrite (y/n): ")
      if user_input[0:1].lower()	== 'y':
         conn.close()
         overwrite = True
         return overwrite
      else:
         sys.stderr.write("Program exiting..." + "\n\n")
         conn.close()
         sys.exit(0)

   def checkDBExists(self, dbfilename):
      # if .db file exists, read MD5 column
      # provide option to do something... 
      overwrite = False
      if os.path.isfile(dbfilename):
         # File exists			
         conn = sqlite3.connect(dbfilename)
         cursor = conn.cursor()
         cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='dbmd';")
         if cursor.fetchone() is not None:
            cursor.execute("SELECT CONTENT_MD5 FROM dbmd")
            if cursor.fetchone()[0] == self.contenthash:
               cursor.execute("SELECT TIMESTAMP FROM dbmd")
               sys.stderr.write("Identical content hashes, generated: " + cursor.fetchone()[0] + "\n\n")
               overwrite = self.userOverwriteOption(conn, "hashes identical.")
         else:
            sys.stderr.write("\n")
            overwrite = self.userOverwriteOption(conn, "hashes cannot be read.")

         return overwrite

   def droidDBSetup(self, droidcsv):

      basedb = GenerateBaselineDB()

      dbfilename = basedb.getDBFilename(droidcsv)













      
      #Overwrite Disabled
      #self.checkDBExists(dbfilename)

      conn = sqlite3.connect(dbfilename)
      cursor = conn.cursor()
      self.dropDROIDTable(cursor)	# may place elsewhere, e.g. when looking for dupes

      with open(droidcsv, 'rb') as csvfile:
         droidreader = csv.reader(csvfile)
         for row in droidreader:
            if droidreader.line_num == 1:		# not zero-based index
               tablequery = self.createDROIDTable(cursor, row)
            else:
               rowstr = ""	
               for i,item in enumerate(row[0:self.csvcolumncount-1]):

                  if i != self.LAST_COL:  #avoid overrun of columns when multi-id occurs
                     
                     if item == "":
                        rowstr = rowstr + ',"no value"'
                     else:
                        rowstr = rowstr + ',"' + item + '"'
                                    
                     if i == self.URI_COL:
                        url = item
                        rowstr = rowstr + ',"' + urlparse(url).scheme + '"'

                     if i == self.PATH_COL:
                        dir = item
                        rowstr = rowstr + ',"' + os.path.dirname(item) + '"'		

                     if i == self.DATE_COL:
                        if item is not '':
                           datestring = item
                           #split at '+' if timezone is there, we're only interested in year
                           dt = datetime.datetime.strptime(datestring.split('+', 1)[0], '%Y-%m-%dT%H:%M:%S')
                           rowstr = rowstr + ',"' + str(dt.year) + '"'
                        else:
                           rowstr = rowstr + ',"' + "no value" + '"'

               cursor.execute("INSERT INTO droid VALUES (" + rowstr.lstrip(',') + ")")

      self.createDBMD(cursor) 

      # Save (commit) the changes
      #conn.commit()

      conn.execute("CREATE INDEX HASH ON droid(HASH)");
      conn.execute("CREATE INDEX NAME ON droid(NAME)");
      conn.execute("CREATE INDEX PUID ON droid(PUID)");

      # Save (commit) the changes
      conn.commit()

      # We can also close the connection if we are done with it.
      # Just be sure any changes have been committed or they will be lost.
      conn.close()
      return dbfilename

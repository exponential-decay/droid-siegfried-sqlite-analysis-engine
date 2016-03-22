﻿class AnalysisQueries:
   
   SELECT_ALL_NAMES = "SELECT FILEDATA.NAME FROM FILEDATA"
   SELECT_FILENAMES_AND_DIRNAMES = "SELECT FILEDATA.DIR_NAME, FILEDATA.NAME FROM FILEDATA"
   
   SELECT_HASH = "SELECT DBMD.HASH_TYPE FROM DBMD"
   
   SELECT_COLLECTION_SIZE = "SELECT SUM(FILEDATA.SIZE) FROM FILEDATA"
   SELECT_COUNT_FILES = "SELECT COUNT(FILEDATA.NAME) FROM FILEDATA WHERE (FILEDATA.TYPE='File' OR FILEDATA.TYPE='Container')"
   SELECT_COUNT_CONTAINERS = "SELECT COUNT(FILEDATA.NAME) FROM FILEDATA WHERE FILEDATA.TYPE='Container'"
   
   SELECT_COUNT_FILES_IN_CONTAINERS = "SELECT COUNT(FILEDATA.NAME) FROM FILEDATA WHERE (FILEDATA.URI_SCHEME!='file') AND (FILEDATA.TYPE='File' OR FILEDATA.TYPE='Container')"
   
   SELECT_COUNT_FOLDERS = "SELECT COUNT(FILEDATA.NAME) FROM FILEDATA WHERE FILEDATA.TYPE='Folder'"
   
   SELECT_COUNT_UNIQUE_FILENAMES = "SELECT COUNT(DISTINCT FILEDATA.NAME) FROM FILEDATA WHERE (FILEDATA.TYPE='File' OR FILEDATA.TYPE='Container')"
   SELECT_COUNT_UNIQUE_DIRNAMES =  "SELECT COUNT(DISTINCT FILEDATA.DIR_NAME) FROM FILEDATA"
   
   SELECT_COUNT_IDENTIFIED_FILES = """SELECT COUNT(FILEDATA.NAME)
                                       FROM IDRESULTS
                                       JOIN FILEDATA on IDRESULTS.FILE_ID = FILEDATA.FILE_ID
                                       JOIN IDDATA on IDRESULTS.ID_ID = IDDATA.ID_ID
                                       WHERE (FILEDATA.TYPE='File' or FILEDATA.TYPE='Container')
                                       AND (IDDATA.METHOD='Signature' or IDDATA.METHOD='Container');"""
                                       
   SELECT_COUNT_MULTIPLE_ID = """SELECT COUNT(IDDATA.FORMAT_COUNT) 
                                    FROM IDRESULTS
                                    JOIN FILEDATA on IDRESULTS.FILE_ID = FILEDATA.FILE_ID
                                    JOIN IDDATA on IDRESULTS.ID_ID = IDDATA.ID_ID
                                    WHERE (FILEDATA.TYPE='File' OR FILEDATA.TYPE='Container') 
                                    AND (IDDATA.FORMAT_COUNT!='1' AND IDDATA.FORMAT_COUNT!='0') 
                                    AND (CAST(FILEDATA.SIZE AS INT) > 0)"""
   
   SELECT_COUNT_UNIDENTIFIED = """SELECT COUNT(FILEDATA.NAME) 
                                    FROM IDRESULTS 
                                    JOIN FILEDATA on IDRESULTS.FILE_ID = FILEDATA.FILE_ID
                                    JOIN IDDATA on IDRESULTS.ID_ID = IDDATA.ID_ID   
                                    WHERE (FILEDATA.TYPE='File' OR FILEDATA.TYPE='Container') 
                                    AND (IDDATA.METHOD='' OR IDDATA.METHOD='Extension')"""

   SELECT_COUNT_EXTENSION_ONLY = """SELECT COUNT(FILEDATA.NAME) 
                                       FROM IDRESULTS 
                                       JOIN FILEDATA on IDRESULTS.FILE_ID = FILEDATA.FILE_ID
                                       JOIN IDDATA on IDRESULTS.ID_ID = IDDATA.ID_ID
                                       WHERE IDDATA.METHOD='Extension' 
                                       AND(FILEDATA.TYPE='File' OR FILEDATA.TYPE='Container')"""


   SELECT_COUNT_FORMAT_RANGE = """SELECT COUNT(DISTINCT IDDATA.ID) 
                                       FROM IDRESULTS 
                                       JOIN FILEDATA on IDRESULTS.FILE_ID = FILEDATA.FILE_ID
                                       JOIN IDDATA on IDRESULTS.ID_ID = IDDATA.ID_ID                                       
                                       WHERE (FILEDATA.TYPE='File' OR FILEDATA.TYPE='Container') 
                                       AND (IDDATA.METHOD='Signature' OR IDDATA.METHOD='Container')"""

   SELECT_COUNT_EXTENSION_RANGE = """SELECT COUNT(DISTINCT FILEDATA.EXT) 
                                       FROM FILEDATA  
                                       WHERE FILEDATA.TYPE='File' OR FILEDATA.TYPE='Container'"""

   SELECT_COUNT_MISMATCHES = """SELECT COUNT(IDDATA.EXTENSION_MISMATCH) 
                                    FROM IDRESULTS 
                                    JOIN FILEDATA on IDRESULTS.FILE_ID = FILEDATA.FILE_ID
                                    JOIN IDDATA on IDRESULTS.ID_ID = IDDATA.ID_ID                                       
                                    WHERE (FILEDATA.TYPE='File' OR FILEDATA.TYPE='Container') 
                                    AND (IDDATA.EXTENSION_MISMATCH=1)"""

   SELECT_METHOD_FREQUENCY_COUNT = """SELECT IDDATA.METHOD, COUNT(*) AS total 
                                       FROM IDRESULTS  
                                       JOIN FILEDATA on IDRESULTS.FILE_ID = FILEDATA.FILE_ID
                                       JOIN IDDATA on IDRESULTS.ID_ID = IDDATA.ID_ID                                          
                                       WHERE (FILEDATA.TYPE='File' OR FILEDATA.TYPE='Container') 
                                       GROUP BY IDDATA.METHOD ORDER BY TOTAL DESC"""	

   SELECT_MIME_FREQUENCY_COUNT = """SELECT IDDATA.MIME_TYPE, COUNT(*) AS total 
                                       FROM IDRESULTS 
                                       JOIN FILEDATA on IDRESULTS.FILE_ID = FILEDATA.FILE_ID
                                       JOIN IDDATA on IDRESULTS.ID_ID = IDDATA.ID_ID                                          
                                       WHERE (FILEDATA.TYPE='File' OR FILEDATA.TYPE='Container') 
                                       GROUP BY IDDATA.MIME_TYPE ORDER BY TOTAL DESC"""

   SELECT_COUNT_ZEROID = """SELECT COUNT(FILEDATA.NAME) 
                              FROM IDRESULTS
                              JOIN FILEDATA on IDRESULTS.FILE_ID = FILEDATA.FILE_ID
                              JOIN IDDATA on IDRESULTS.ID_ID = IDDATA.ID_ID  
                              WHERE IDDATA.METHOD='' 
                              AND (FILEDATA.TYPE='File' OR FILEDATA.TYPE='Container')"""

   SELECT_DISTINCT_BINARY_MATCH_NAMES = """SELECT DISTINCT IDDATA.ID, IDDATA.FORMAT_NAME, IDDATA.FORMAT_VERSION 
                                          FROM IDDATA
                                          WHERE (IDDATA.METHOD='Signature' OR IDDATA.METHOD='Container')"""

   SELECT_BINARY_MATCH_COUNT = """SELECT IDDATA.ID, COUNT(*) AS total 
                                    FROM IDRESULTS 
                                    JOIN FILEDATA on IDRESULTS.FILE_ID = FILEDATA.FILE_ID
                                    JOIN IDDATA on IDRESULTS.ID_ID = IDDATA.ID_ID                                      
                                    WHERE (FILEDATA.TYPE='File' OR FILEDATA.TYPE='Container') 
                                    AND (IDDATA.METHOD='Signature' OR IDDATA.METHOD='Container') 
                                    GROUP BY IDDATA.ID ORDER BY TOTAL DESC"""

   SELECT_YEAR_FREQUENCY_COUNT = """SELECT FILEDATA.YEAR, COUNT(FILEDATA.YEAR) AS total 
                                       FROM FILEDATA 
                                       WHERE (FILEDATA.TYPE='File' OR FILEDATA.TYPE='Container') 
                                       GROUP BY FILEDATA.YEAR ORDER BY TOTAL DESC"""


   #TODO: THIS STAT NEEDS REVISITING IN LIGHT OF SIEGFRIED
   #MULTIPLE IDS WILL BE REFLECTED USING MULTIPLE NAMESPACE PLACES - HOW TO REPORT ON?
   SELECT_PUIDS_EXTENSION_ONLY = """SELECT DISTINCT IDDATA.ID, IDDATA.FORMAT_NAME 
                                       FROM IDDATA 
                                       WHERE IDDATA.METHOD='Extension'
                                       AND IDDATA.FORMAT_COUNT=1"""
   
   #TODO: THIS STAT IS DIFFERENT FROM THE ON ABOVE BECAUSE IT INCLUDES MULTIPLE FORMAT COUNT - UGH!
   SELECT_EXT_ONLY_FREQUENCY = """SELECT IDDATA.ID, COUNT(*) AS total 
                                    FROM IDDATA                                     
                                    WHERE IDDATA.METHOD='Extension'
                                    GROUP BY IDDATA.ID ORDER BY TOTAL DESC"""


   SELECT_ALL_UNIQUE_EXTENSIONS = """SELECT DISTINCT FILEDATA.EXT 
                                       FROM FILEDATA 
                                       WHERE (FILEDATA.TYPE='File' OR FILEDATA.TYPE='Container')"""

   SELECT_COUNT_EXTENSION_FREQUENCY = """SELECT FILEDATA.EXT, COUNT(*) AS total 
                                             FROM FILEDATA
                                             WHERE (FILEDATA.TYPE='File' OR FILEDATA.TYPE='Container') 
                                             GROUP BY FILEDATA.EXT ORDER BY TOTAL DESC"""

   SELECT_EXTENSION_MISMATCHES = """SELECT FILEDATA.FILE_PATH 
                                             FROM IDRESULTS 
                                             JOIN FILEDATA on IDRESULTS.FILE_ID = FILEDATA.FILE_ID
                                             JOIN IDDATA on IDRESULTS.ID_ID = IDDATA.ID_ID                                              
                                             WHERE (FILEDATA.TYPE='File' OR FILEDATA.TYPE='Container') 
                                             AND (IDDATA.EXTENSION_MISMATCH=1)"""

   #ERRORS, TODO: Place somewhere else?
   ERROR_NOHASH = "Unable to detect duplicates: No HASH algorithm used by identification tool."
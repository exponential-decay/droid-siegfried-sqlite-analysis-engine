 # -*- coding: utf-8 -*-
 
class AnalysisStringsEN:
 
   REPORT_TITLE = "DROID Analysis Results"
   REPORT_SUMMARY = "Summary Statistics" 
   REPORT_VERSION = "Analysis Version"
   REPORT_FILE = "Analysis File"
   
   REPORT_MORE_INFORMATION = "Summary of the Statistic"
   
   SUMMARY_TOTAL_FILES = "Total Files" 
   SUMMARY_ARCHIVE_FILES = "Total Archive Files" 
   SUMMARY_INSIDE_ARCHIVES = "Total Files Inside Archive Objects" 
   SUMMARY_DIRECTORIES = "Total Directories" 
   SUMMARY_UNIQUE_DIRNAMES = "Total Unique Directory Names" 
   SUMMARY_IDENTIFIED_FILES = "Total Identified Files (Based on Signature)"
   SUMMARY_MULTIPLE = "Total Multiple Identifications (Baed on Signature)"
   SUMMARY_UNIDENTIFIED = "Total Unidentified Files" 
   SUMMARY_EXTENSION_ID = "Total Extension ID Only Count"
   SUMMARY_EXTENSION_MISMATCH = "Total Extension Mismatches" 
   SUMMARY_ID_PUID_COUNT = "Total Discrete File Format Signature Identifiers (PUIDs) in the Accession/Extract"
   SUMMARY_UNIQUE_EXTENSIONS = "Total Unique Extensions Across Accession/Extract"
   SUMMARY_ZERO_BYTE = "Total Zero-byte Files in Accession/Extract" 
   SUMMARY_IDENTICAL_FILES = "Total Files with Identical Content (Checksum Value)"
   SUMMARY_MULTIPLE_SPACES = "Total Files with Multiple Contiguous Space Characters"
   SUMMARY_PERCENTAGE_IDENTIFIED = "Percentage of Accession/Extract Identified"
   SUMMARY_PERCENTAGE_UNIDENTIFIED = "Percentage of Accession/Extract Unidentified"
   
   HEADING_SIZE = "Size of the accession/extract"
   HEADING_IDENTIFIED = "Identified File Formats in Accession/Extract" 
   HEADING_FREQUENCY_PUIDS_IDENTIFIED = "Frequency of File Format Signature Identified PUIDs"
   HEADING_DATE_RANGE = "Date Range of Items in the Accession/Extract"
   HEADING_EXTENSION_ONLY = "Extension Only Identification in the Accession/Extract"
   HEADING_ID_METHOD = "Identification Method Frequency" 
   HEADING_FREQUENCY_EXTENSION_ONLY = "Frequency of Extension Only Identification In Accession/Extract" 
   HEADING_UNIQUE_EXTENSIONS = "Unique Extensions Identified Across All Objects (ID and non-ID)"
   HEADING_LIST_MULTIPLE = "List of Files With Multiple Identifications" 
   HEADING_FREQUENCY_EXTENSIONS_ALL = "Frequency of All Extensions"
   HEADING_FREQUENCY_MIME = "MIME Type (Internet Media Type) Frequency"
   HEADING_LIST_ZERO_BYTES = "Zero-byte files in Accession/Extract" 
   HEADING_NO_ID = "Files With No Identification"
   HEADING_ARCHIVE_FORMATS = "Archive Format Types in Accession/Extract"
   HEADING_IDENTICAL_CONTENT = "Files With Identical Content (Checksum Value)" 
   HEADING_TROUBLESOME_FILENAMES = "Identifying Non-ASCII and System File Names" 

   SUMMARY_DESC_TOTAL_FILES = "Number of digital files in the accession/extract." 
   SUMMARY_DESC_ARCHIVE_FILES = "The total number of archive files in the accession/extract overall. Archive files are objects that wrap together one or more files such as Zip files, GZIP files, and TAR files. Knowing an accession/extract contains these objects is important as a single archive file may contain many hundreds of other files that also need to be preserved and looked after." 
   SUMMARY_DESC_INSIDE_ARCHIVES = "An aggregate total number of all files inside archive files." 
   SUMMARY_DESC_DIRECTORIES = "A directory is a folder in the accession/extract delineating a file system hierarchy. Total directories is the total number of directories in the accession/extract overall." 
   SUMMARY_DESC_UNIQUE_DIRNAMES = "This is used to determine the number of duplicate directory (folder) names." 
   SUMMARY_DESC_IDENTIFIED_FILES = "The number of files that are identified based on a file format signature. The file format signature is a string in binary (or hexadecimal (HEX)) that uniquely identifies a file format. Note: A signature is a more mature form of a magic number that can be read across the file. A basic magic number is a unique section at the beginning of a file that can be seen when the file is looked at with an x-ray machine (the innards of a file is examined). This number could be in binary (that is numerical) or ASCII (readable text) form."
   SUMMARY_DESC_MULTIPLE = "This is the total number of files with uncertain file format identification. DROID will help to identify the number of potential formats."
   SUMMARY_DESC_UNIDENTIFIED = "This is the number of files identified only by the file extension alone (e.g. there are no verifiable file format signatures in the file, only the file extension is provided). This number may represent files not identified at all (i.e.. there is no identification information in the DROID database)." 
   SUMMARY_DESC_EXTENSION_ID = "Files that can only be identified by their extension (e.g. \".doc\" might be a Microsoft Word file, \".mp3\" might be an audio file) This is a sub-set of the \"Total unidentified files\"."
   SUMMARY_DESC_EXTENSION_MISMATCH = "This is the total number of cases where the extension used does not match with the file signature." 
   SUMMARY_DESC_ID_PUID_COUNT = "The total discrete file format signature identifiers in the accession/extract are used to help identify its diversity/complexity. PUID is an acronym for PRONOM Unique Identifier. PRONOM is a web-based technical registry to support digital preservation services, developed by The National Archives of the United Kingdom."
   SUMMARY_DESC_UNIQUE_EXTENSIONS = "The total number of unique file extensions identified in the accession/extract. The total unique extensions across the accession/extract are another statistic we can use to identify the diversity/complexity of the accession/extract."
   SUMMARY_DESC_ZERO_BYTE = "Zero byte files have no binary content. They may have been created with the intention of turning into a record, e.g. a document, but they may also be indicative of a process that has corrupted the file such as a faulty extract. Zero-byte files may have a filename and extension but will have zero size." 
   SUMMARY_DESC_IDENTICAL_FILES = "Total number of files across the accession/extract that are identical byte-for-byte."
   SUMMARY_DESC_MULTIPLE_SPACES = "Number of filenames that contain more than one space in a row, these filenames may cause some problems with some systems and may require pre-conditioning."
   SUMMARY_DESC_PERCENTAGE_IDENTIFIED = "Percentage of files with formats that are positively identified by DROID, pending other processes such as format validation, this percentage may be indicative of how much of the accession/extract will need little or no intervention to ingest cleanly."
   SUMMARY_DESC_PERCENTAGE_UNIDENTIFIED = "Percentage of files with formats that were not able to be identified by DROID, which could be due to a signature not being in the PRONOM database yet, the file being corrupt, a signature and extension mismatch or another reason. This percentage is indicative of how much work will be involved in processing the accession/extract."
   
   HEADING_DESC_SIZE = "The size of the accession/extract is represented using two values, bytes (a byte equals eight binary bits) from the DROID export and conversion from bytes into megabytes for understanding the size of larger accessions/extracts. We will use this statistic to understand how much storage is required for this accession/extract when ingested."
   HEADING_DESC_IDENTIFIED = "A list of PUID values and format names to provide a clear picture of diversity/complexity of the accession/extract. PUID is an acronym for PRONOM Unique Identifier. PRONOM is a web-based technical registry to support digital preservation services, developed by The National Archives of the United Kingdom." 
   HEADING_DESC_FREQUENCY_PUIDS_IDENTIFIED = "Visualization is used to provide a clear description of the distribution of file formats across the accession/extract. The file format signature is a string in binary (or hexadecimal (HEX)) that uniquely identifies a file format. PUID is an acronym for PRONOM Unique Identifier. PRONOM is a web-based technical registry to support digital preservation services, developed by The National Archives of the United Kingdom. Count and visualization of how many times each format is represented in the accession/extract, in a descending list from most frequent to least."
   HEADING_DESC_DATE_RANGE = "Count and visualization of how many times each format is represented in the accession/extract, in a descending list from most frequent to least. The visualization gives a clear description of the distribution of file modification dates across the accession/extract. Too small or too recent a date range may indicate file transfer errors depending on the source of files."
   HEADING_DESC_EXTENSION_ONLY = "A list of the PUID and format name of each format of one or more files where DROID has tried to offer suggestions as to potential file format by utilizing the file extension where a file has not been matched by file format signature."
   HEADING_DESC_ID_METHOD = "Lists in descending order the types of identification DROID used for each file, indicating the reliability of each identification, with Container/Signature being the more concrete forms of identification and extension being a less certain way to identify a format. The file format signature is a string in binary (or hexadecimal (HEX)) that uniquely identifies a file format. Container identification takes this concept further by being able to match specific elements of a file format's structure." 
   HEADING_DESC_FREQUENCY_EXTENSION_ONLY = "A count of the files associated with possible PUIDs where DROID has tried to offer suggestions as to potential file format by utilizing the file extension where a file format signature has not matched a file." 
   HEADING_DESC_UNIQUE_EXTENSIONS = "Lists all the file extensions found in all the files in the accession/extract. This information can be used to identify the diversity/complexity of the accession/extract, but also to identify the consistency with which extensions may have been used in the accession/extract and may indicate how much work may be needed to correct inconsistencies to create a clean ingest."
   HEADING_DESC_LIST_MULTIPLE = "List of files with an uncertain file format identification. These files will almost certainly need to be investigated independently to understand their preservation risks. Where possible file format signatures will be created to ensure that the same types of object are identified in future."
   HEADING_DESC_FREQUENCY_EXTENSIONS_ALL = "Lists the gamut of file extensions alongside how many times they appear in accession/extract in descending order. This information can be used to identify the diversity/complexity of the accession/extract, but also to identify the consistency with which extensions may have been used in the accession/extract and may indicate how much work may be needed to correct inconsistencies to create a clean ingest."
   HEADING_DESC_FREQUENCY_MIME = "Lists all the MIME Types alongside how many times they appear in the accession/extract in descending order. A MIME Type is an identification used by internet browsers to determine how a browser will represent a file on the internet by displaying, playing or prompting the user to download the object."
   HEADING_DESC_LIST_ZERO_BYTES = "This is a list of files with no payload. Zero byte files have no binary content. They may have been created with the intention of turning into a record, e.g. a document, but they may also be indicative of a process that has corrupted the file such as a faulty extract. Zero-byte files may have a filename and extension but will have zero size." 
   HEADING_DESC_NO_ID = "List of files identified only by the file extension alone (e.g. there are no verifiable file format signatures in the file, only the file extension is provided). This number may represent files not identified at all (i.e. there is no identification information in the DROID database)"
   HEADING_DESC_ARCHIVE_FORMATS = "Archive files are files that wrap together one or more files such as Zip files, GZIP files, and TAR files. Knowing an accession/extract contains these objects is important as a single archive file may contain many hundreds of other files that also need to be preserved and looked after."
   HEADING_DESC_IDENTICAL_CONTENT = "This is a list of files that are identical byte for byte. Count: is the number of instances of a particular checksum value that are found across the accession/extract. Filepath is listed to help with locating the object and to help appraisal decisions if the purpose of the duplicate can be ascertained. In the majority of cases if a duplicate is received it will be ingested as-is as that is what was received." 
   HEADING_DESC_TROUBLESOME_FILENAMES = "Lists filenames that may cause issues across different systems and applications. These could be filenames that include UTF-8 characters such as Macrons, or incidences of filenames with multiple space characters following one after the other. Filenames identified will also include those for which there is an explicit recommendation against from Microsoft: https://msdn.microsoft.com/en-nz/library/windows/desktop/aa365247%28v=vs.85%29.aspx?f=255&MSPPError=-2147217396"    

   TEXT_ONLY_FIVE_TOP_PUIDS = "Five Top PUIDs in Accession/Extract"
   TEXT_ONLY_FIVE_TOP_EXTENSIONS = "Five Top Extensions in Accession/Extract"
   
   COLUMN_HEADER_VALUES_FORMAT = "Format Name"
   COLUMN_HEADER_VALUES_COUNT = "Count"
   COLUMN_HEADER_VALUES_YEAR = "Year"
   
   FNAME_CHECK_ASCII = "contains, characters outside of ASCII range"
   FNAME_CHECK_PERIOD = "has a period ('.') as its last character"
   FNAME_CHECK_NOT_RECOMMENDED = "contains, non-recommended character"
   FNAME_CHECK_NON_PRINT = "contains, non-printable character"
   FNAME_CHECK_RESERVED = "contains, reserved name"
   FNAME_CHECK_SPACE = "has a SPACE as its last character"

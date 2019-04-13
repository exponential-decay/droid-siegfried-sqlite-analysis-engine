# -*- coding: utf-8 -*-


class AnalysisStringsEN:

    REPORT_TITLE_DR = "DROID Analysis Results"
    REPORT_TITLE_SF = "Siegfried Analysis Results"
    REPORT_SUMMARY = "Summary Statistics"
    REPORT_VERSION = "Analysis Version"
    REPORT_FILE = "Analysis File"
    REPORT_TOOL = "Analysis Tool"
    NAMESPACES = "Namespaces Used"

    REPORT_MORE_INFORMATION = "More Detail:"

    COUNT_TEXT = " Counts are shown for each entry in round () brackets."

    SUMMARY_TOTAL_FILES = "Total Files"
    SUMMARY_ARCHIVE_FILES = "Total Archive Files"
    SUMMARY_INSIDE_ARCHIVES = "Total Files Inside Archive Files"
    SUMMARY_DIRECTORIES = "Total Directories"
    SUMMARY_UNIQUE_DIRNAMES = "Total Unique Directory Names"
    SUMMARY_IDENTIFIED_FILES = "Total Identified Files (Based on Signature)"
    SUMMARY_MULTIPLE = "Total Multiple Identifications (Based on Signature)"
    SUMMARY_UNIDENTIFIED = "Total Unidentified Files"
    SUMMARY_EXTENSION_ID = "Total Extension ID Only Count"
    SUMMARY_EXTENSION_MISMATCH = "Total Extension Mismatches"

    SUMMARY_ID_PUID_COUNT = "Total Discrete File Format Signature Identifiers (PUIDs) in the Accession/Extract"
    SUMMARY_DESC_ID_PUID_COUNT = (
        "The total discrete file format signature identifiers in the accession/extract are "
        "used to help identify its diversity/complexity. PUID is an acronym for PRONOM Unique "
        "Identifier. PRONOM is a web-based technical registry to support digital preservation "
        "services, developed by The National Archives of the United Kingdom."
    )

    SUMMARY_UNIQUE_EXTENSIONS = "Total Unique Extensions Across Accession/Extract"
    SUMMARY_ZERO_BYTE = "Total Zero-byte Files in Accession/Extract"
    SUMMARY_IDENTICAL_FILES = "Total Files with Identical Content (Checksum Value)"
    SUMMARY_MULTIPLE_SPACES = "Total Files with Multiple Contiguous Space Characters"
    SUMMARY_PERCENTAGE_IDENTIFIED = "Percentage of Accession/Extract Identified"
    SUMMARY_PERCENTAGE_UNIDENTIFIED = "Percentage of Accession/Extract Unidentified"

    # NEW SIEGFRIED STRINGS
    XML_DETAILS = (
        "Freedesktop's XML matching mechanism will match features of an XML document once the "
        "identifying mechanism has established the file it is looking at is an XML file. Features may include "
        "XML namespace. This two pronged approach to identifying XML files may prove more rigorous than traditional "
        "file format signature matching techniques. More details on Freedesktop's "
        "mechanisms can be found <a href='https://docs.oracle.com/cd/E26502_01/html/E28056/gmcas.html'>here.</a>"
    )

    FILENAME_DETAILS = (
        "Freedesktop's filename matching mechanism will match a filename pattern ('GLOB' pattern). "
        "A pattern maybe a filename, or a filename extension, e.g. README*, or *.MP3. "
        "The mechanism works a lot like a filename extension match but can pick up more varied "
        "types that might not be encoded in the PRONOM database. More details on Freedesktop's "
        "mechanisms can be found <a href='https://docs.oracle.com/cd/E26502_01/html/E28056/gmcas.html'>here.</a>"
    )

    SUMMARY_XML_ID = "Total XML ID Only Count"
    SUMMARY_DESC_XML_ID = (
        "Total files identified using an XML matching mechanism. " + XML_DETAILS
    )

    SUMMARY_TEXT_ID = "Total Text ID Only Count"
    SUMMARY_DESC_TEXT_ID = "Total files identified using a Text matching/Text encoding matching methanism. "

    SUMMARY_FILENAME_ID = "Total Filename ID Only Count"
    SUMMARY_DESC_FILENAME_ID = (
        "Total files identified using a Filename matching mechanism. "
        + FILENAME_DETAILS
    )

    SUMMARY_OTHER_ID_COUNT = "Total Discrete Other (Non-PUID) File Format Signature Identifiers in the Accession/Extract"
    SUMMARY_DESC_OTHER_ID_COUNT = (
        "The total discrete file format signature identifiers in the accession/extract are "
        "used to help identify its diversity/complexity. Non-PUID identifiers are any that "
        "aren't specified within the PRONOM namespace, for example, Freedesktop.org. Using "
        "alternative namespaces can help us to identify ways of filling gaps within the PRONOM "
        "namespace."
    )

    SUMMARY_XML_ID_COUNT = (
        "Total XML Based Identification Identifiers in the Accession/Extract"
    )
    SUMMARY_DESC_XML_ID_COUNT = (
        "The total XML identifiers in the Accession/Exratact are used to help identify its "
        "diversity/complexity. XML identifiers are returned for files that have first been "
        "identified as XML, but have then had other features identified such as the XML's "
        "namespace which is often used to uniquely identify elements within the XML document."
    )

    SUMMARY_TEXT_ID_COUNT = (
        "Total Text Based Identification Identifiers in the Accession/Extract"
    )
    SUMMARY_DESC_TEXT_ID_COUNT = (
        "The total Text identifiers in the Accession/Exratact are used to help identify its "
        "diversity/complexity. Text identifiers are returned for files where their encoding "
        "can be regocognised not to be binary."
    )

    SUMMARY_FILENAME_ID_COUNT = (
        "Total Filename Based Identification Identifiers in the Accession/Extract"
    )
    SUMMARY_DESC_FILENAME_ID_COUNT = (
        "The total Filename identifiers in the Accession/Exratact are used to help identify its "
        "diversity/complexity. Filename identifiers may be returned where the filename extension "
        "is recognised, e.g. *.MP3, or the filename itself is recognised as being a common pattern, "
        "e.g. 'README*'."
    )

    SUMMARY_DISTANCE_BOF = "Max Distance Scanned from Beginning of File"
    SUMMARY_DISTANCE_EOF = "Max Distance Scanned from End of File"
    SUMMARY_GAPS_COVERED = (
        "Files Left Unidentified Across Multiple Identifiers (Gaps Based on Signature)"
    )
    SUMMARY_DESC_GAPS_COVERED = (
        "Count of all the files that have zero identification results across all "
        "namespaces utilizing binary and container file format signatures. As such "
        "this statisticate may indicate an immediate priority for digital preservation "
        "researchers, and therfore may be indicative of the amount of work needed to "
        "understand an accession/extract."
    )

    HEADING_BINARY_ID = (
        "Aggregated Frequency of File Format Signature Identifiers in Accession/Extract"
    )
    HEADING_DESC_BINARY_ID = (
        "Listing of format identification, namespace, count, and match basis for files "
        "identified using file format signatures. Some tools can report what the basis "
        "or rationale was for returning an identification - this is reported to demonstrate "
        "the diversity/complexity of an accession/extract and to provide clues for similar "
        "files in the accession/extract where there is zero identification."
        + COUNT_TEXT
    )

    HEADING_XML_ID = "Aggregated Frequency of XML Identifiers in Accession/Extract"
    HEADING_DESC_XML_ID = (
        "Listing of format identification, namespace, count, and match basis for files "
        "identified using XML based identification. Some tools can report what the basis "
        "or rationale was for returning an identification - this is reported to demonstrate "
        "the diversity/complexity of an accession/extract and to provide clues for similar "
        "files in the accession/extract where there is zero identification."
        + COUNT_TEXT
    )

    HEADING_TEXT_ID = "Aggregated Frequency of Text Identifiers in Accession/Extract"
    HEADING_DESC_TEXT_ID = (
        "Listing of format identification, namespace, count, and match basis for files "
        "identified using Text based identification. Some tools can report what the basis "
        "or rationale was for returning an identification - this is reported to demonstrate "
        "the diversity/complexity of an accession/extract and to provide clues for similar "
        "files in the accession/extract where there is zero identification."
        + COUNT_TEXT
    )

    HEADING_FILENAME_ID = (
        "Aggregated Frequency of Filename Identifiers in Accession/Extract"
    )
    HEADING_DESC_FILENAME_ID = (
        "Listing of format identification, namespace, count, and match basis for files "
        "identified using Filename based identification. Some tools can report what the basis "
        "or rationale was for returning an identification - this is reported to demonstrate "
        "the diversity/complexity of an accession/extract and to provide clues for similar "
        "files in the accession/extract where there is zero identification."
        + COUNT_TEXT
    )

    HEADING_NAMESPACE_SPECIFIC_STATISTICS = "Results Per Identifier Namespace"
    HEADING_DESC_NAMESPACE_SPECIFIC_STATISTICS = (
        "Namespace describes an identifier used by any specific tool. Format identification "
        "tools such as Siegfried can include multiple identifiers, e.g. PRONOM (and) Freedesktop.org's "
        "MIME identification. Tools may also include subsets of an identification mechanism that will "
        "also be indicated by use of a different namespace, for example, a set of PRONOM identifiers for "
        "recognising types of audio visual file, exclusively." + COUNT_TEXT
    )

    HEADING_NAMESPACE = "Namespace"
    HEADING_DESC_NAMESPACE = (
        "The namespace that we're reporting on and the specific details associated with it. "
        "e.g. a PRONOM namespace with details of the signature file version used."
    )

    HEADING_ERRORS = "File Processing Errors Encountered During Scan"
    HEADING_DESC_ERRORS = (
        "Tools like Siegfried may report on file processing errors during a scan. "
        "A processing error may indicate a file with no payload (zero-byte file) or another "
        "problem that might be important ot understand as it may affect its access and preservation."
        + COUNT_TEXT
    )

    ACROSS_NAMESPACE_BOILERPLACE = (
        "Some sources of file format identification offer alternatives to file format "
        "signatures. Tools like Siegfried can also provide alternative techniques too. "
        "These techniques output identifiers within the framework set out by DROID and "
        "Siegfried, as oppesed the Linux tool File. "
    )

    HEADING_XML_ID_COMPLETE = "XML Based Identifiers Across Namespaces"
    HEADING_DESC_XML_ID_COMPLETE = (
        ACROSS_NAMESPACE_BOILERPLACE
        + (
            "This listing presents a count of identification "
            "results from scanning files using Freedesktop's MIME XML matching mechanism. "
        )
        + XML_DETAILS
    )

    HEADING_TEXT_ID_COMPLETE = "Text Based Identifiers Across Namespaces"
    HEADING_DESC_TEXT_ID_COMPLETE = ACROSS_NAMESPACE_BOILERPLACE + (
        "This listing presents a count of identification "
        "results from scanning files using a Text matching/Text Encoding matching mechanism. "
    )

    HEADING_FILENAME_ID_COMPLETE = "Filename Based Identifiers Across Namespaces"
    HEADING_DESC_FILENAME_ID_COMPLETE = (
        ACROSS_NAMESPACE_BOILERPLACE
        + (
            "This listing presents a count of identification "
            "results from scanning files using Freedesktop's MIME Filename matching mechanism. "
        )
        + FILENAME_DETAILS
        + COUNT_TEXT
    )

    # BELOW ITEMS MAY BE OBSOLETE...
    HEADING_NO_ID = "Files With No Identification"
    HEADING_DESC_NO_ID = (
        "List of files identified only by the file extension alone (e.g. there are no "
        "verifiable file format signatures in the file, only the file extension is provided). "
        "This number may represent files not identified at all (i.e. there is no identification "
        "information in the DROID database)"
    )

    HEADING_AGGREGATE_BINARY_IDENTIFIED = (
        "Aggregated File Format Signature Identifiers in Accession/Extract"
    )
    HEADING_DESC_IDENTIFIED = (
        "A list of ID values and format names to provide a clear picture of diversity/complexity of the "
        "accession/extract. PUID is an acronym for PRONOM Unique Identifier. PRONOM is a web-based technical "
        "registry to support digital preservation services, developed by The National Archives of the United Kingdom. "
        "Other identifiers listed may come from Freedesktop.org's MIMEInfo Database or Apache's Tika equivalent."
    )
    # NEW SIEGFRIED STRINGS

    HEADING_SIZE = "Size of the accession/extract"
    HEADING_FREQUENCY_PUIDS_IDENTIFIED = (
        "Frequency of File Format Signature Identified IDs"
    )
    HEADING_DATE_RANGE = "Date Range of Items in the Accession/Extract"
    HEADING_EXTENSION_ONLY = "Extension Only Identification in the Accession/Extract"
    HEADING_ID_METHOD = "Identification Method Frequency"
    HEADING_FREQUENCY_EXTENSION_ONLY = (
        "Frequency of Extension Only Identification In Accession/Extract"
    )
    HEADING_UNIQUE_EXTENSIONS = (
        "Unique Extensions Identified Across All Objects (ID and non-ID)"
    )
    HEADING_LIST_MULTIPLE = "List of Files With Multiple Identifications"
    HEADING_FREQUENCY_EXTENSIONS_ALL = "Frequency of All Extensions"
    HEADING_FREQUENCY_MIME = "MIME Type (Internet Media Type) Frequency"
    HEADING_LIST_ZERO_BYTES = "Zero-byte files in Accession/Extract"
    HEADING_ARCHIVE_FORMATS = "Archive File Types in Accession/Extract"
    HEADING_IDENTICAL_CONTENT = "Files With Identical Content (Checksum Value)"
    HEADING_TROUBLESOME_FILENAMES = "Identifying Non-ASCII and System File Names"
    HEADING_TROUBLESOME_DIRNAMES = "Identifying Non-ASCII and System Directory Names"

    SUMMARY_DESC_TOTAL_FILES = "Number of digital files in the accession/extract."

    SUMMARY_DESC_ARCHIVE_FILES = (
        "The total number of archive files in the accession/extract overall. Archive "
        "files are objects that wrap together one or more files such as Zip files, GZIP files, "
        "and TAR files. Knowing an accession/extract contains these objects is important as a "
        "single archive file may contain many hundreds of other files that also need to be preserved "
        "and looked after."
    )

    SUMMARY_DESC_INSIDE_ARCHIVES = (
        "An aggregate total number of all files inside archive files."
    )

    SUMMARY_DESC_DIRECTORIES = (
        "A directory is a folder in the accession/extract delineating a file system hierarchy. "
        "Total directories is the total number of directories in the accession/extract overall."
    )

    SUMMARY_DESC_UNIQUE_DIRNAMES = (
        "This is used to determine the number of duplicate directory (folder) names."
    )

    SUMMARY_DESC_IDENTIFIED_FILES = (
        "The number of files that are identified based on a file format signature. "
        "A file format signature is a string in binary (or hexadecimal (hex)) that "
        "uniquely identifies a file format. Note: A signature is a more mature form of "
        "a magic number that can be read across the file. A basic magic number is a unique "
        "section at the beginning of a file that can be seen when the file is looked at "
        "with an x-ray machine (the innards of a file is examined). This number could be "
        "in binary (that is numerical) or ASCII (readable text) form."
    )

    SUMMARY_DESC_MULTIPLE = (
        "This is the total number of files with uncertain file format identification. "
        "DROID will help to identify the number of potential formats."
    )

    SUMMARY_DESC_UNIDENTIFIED = (
        "This is the number of files identified only by the file extension alone "
        "(e.g. there are no verifiable file format signatures in the file, only the file "
        "extension is provided). This number may represent files not identified at all "
        "(i.e.. there is no identification information in the DROID database)."
    )

    SUMMARY_DESC_EXTENSION_ID = (
        'Files that can only be identified by their extension (e.g. ".DOC" might be a Microsoft Word '
        'file, ".MP3" might be an audio file) This is a sub-set of the "Total unidentified files".'
    )

    SUMMARY_DESC_EXTENSION_MISMATCH = "This is the total number of cases where the extension used does not match with the file signature."

    SUMMARY_DESC_UNIQUE_EXTENSIONS = (
        "The total number of unique file extensions identified in the accession/extract. "
        "The total unique extensions across the accession/extract are another statistic we "
        "can use to identify the diversity/complexity of the accession/extract."
    )

    SUMMARY_DESC_ZERO_BYTE = (
        "Zero byte files have no binary content. They may have been created with the intention of turning "
        "into a record, e.g. a document, but they may also be indicative of a process that has corrupted "
        "the file such as a faulty extract. Zero-byte files may have a filename and extension but will have zero size."
    )

    SUMMARY_DESC_IDENTICAL_FILES = "Total number of files across the accession/extract that are identical byte-for-byte."

    SUMMARY_DESC_MULTIPLE_SPACES = (
        "Number of filenames that contain more than one space in a row, these filenames may cause "
        "some problems with some systems and may require pre-conditioning."
    )

    SUMMARY_DESC_PERCENTAGE_IDENTIFIED = (
        "Percentage of files with formats that are positively identified by DROID, pending other processes "
        "such as format validation, this percentage may be indicative of how much of the accession/extract will "
        "need little or no intervention to ingest cleanly."
    )

    SUMMARY_DESC_PERCENTAGE_UNIDENTIFIED = (
        "Percentage of files with formats that were not able to be identified by DROID, which could be due to a "
        "signature not being in the PRONOM database yet, the file being corrupt, a signature and extension mismatch "
        "or another reason. This percentage is indicative of how much work will be involved in processing the "
        "accession/extract."
    )

    HEADING_DESC_SIZE = (
        "The size of the accession/extract is represented using two values, bytes (a byte equals eight binary bits) "
        "from the DROID export and conversion from bytes into megabytes for understanding the size of larger "
        "accessions/extracts. We will use this statistic to understand how much storage is required for this "
        "accession/extract when ingested."
    )

    HEADING_DESC_FREQUENCY_PUIDS_IDENTIFIED = (
        "A chart used to provide a clear visualization of the distribution of file formats "
        "across the accession/extract. A file format signature is a string in binary (or hexadecimal "
        "(hex)) that uniquely identifies a file format. PUID is an acronym for PRONOM Unique Identifier. "
        "PRONOM is a web-based technical registry to support digital preservation services, developed by "
        "The National Archives of the United Kingdom."
        "Other identifiers listed may come from Freedesktop.org's MIMEInfo Database or Apache's Tika equivalent. "
        "Count and visualization of how many times each format "
        "is represented in the accession/extract, in a descending list from most frequent to least."
    )

    HEADING_DESC_DATE_RANGE = (
        "Count and visualization giving a clear illustration of the distribution of file modification dates across the "
        "accession/extract. The list is in descending order based on the number of files last modified on any given year. "
        "Too small or too recent a date range may indicate file transfer errors depending on the source of files."
    )

    HEADING_DESC_EXTENSION_ONLY = (
        "A list of the identifier and format name of each format of one or more files where the file format identification tool has "
        "tried to offer suggestions as to potential file format by utilizing the file extension where a file has not been matched "
        "by file format signature."
    )

    HEADING_DESC_ID_METHOD = (
        "Lists in descending order the types of identification DROID used for each file, indicating the reliability "
        "of each identification, with Container/Signature being the more concrete forms of identification and extension "
        "being a less certain way to identify a format. A file format signature is a string in binary (or hexadecimal "
        "(hex)) that uniquely identifies a file format. Container identification takes this concept further by being able "
        "to match specific elements of a file format's structure." + COUNT_TEXT
    )

    HEADING_DESC_FREQUENCY_EXTENSION_ONLY = (
        "A count of the files associated with possible identifiers where file format identification tool has tried to offer "
        "suggestions as to potential file format by utilizing the file extension where a file format signature has not "
        "matched a file." + COUNT_TEXT
    )

    HEADING_DESC_UNIQUE_EXTENSIONS = (
        "Lists all the file extensions found in all the files in the accession/extract. This information can be "
        "used to identify the diversity/complexity of the accession/extract, but also to identify the consistency "
        "with which extensions may have been used in the accession/extract and may indicate how much work may be "
        "needed to correct inconsistencies to create a clean ingest."
    )

    HEADING_DESC_LIST_MULTIPLE = (
        "List of files with an uncertain file format identification. These files will almost certainly need to be "
        "investigated independently to understand their preservation risks. Where possible file format signatures "
        "will be created to ensure that the same types of object are identified in future."
    )

    HEADING_DESC_FREQUENCY_EXTENSIONS_ALL = (
        "Lists the gamut of file extensions alongside how many times they appear in accession/extract "
        "in descending order. This information can be used to identify the diversity/complexity of the "
        "accession/extract, but also to identify the consistency with which extensions may have been "
        "used in the accession/extract and may indicate how much work may be needed to correct "
        "inconsistencies to create a clean ingest." + COUNT_TEXT
    )

    HEADING_DESC_FREQUENCY_MIME = (
        "Lists all the MIME Types alongside how many times they appear in the accession/extract in descending order. "
        "A MIME Type is an identification used by internet browsers to determine how a browser will represent a file "
        "on the internet by displaying, playing or prompting the user to download the object."
        + COUNT_TEXT
    )

    HEADING_DESC_LIST_ZERO_BYTES = (
        "This is a list of files with no payload. Zero byte files have no binary content. They may have been created "
        "with the intention of turning into a record, e.g. a document, but they may also be indicative of a process "
        "that has corrupted the file such as a faulty extract. Zero-byte files may have a filename and extension but "
        "will have zero size."
    )

    HEADING_DESC_ARCHIVE_FORMATS = (
        "Archive files are files that wrap together one or more files such as Zip files, GZIP files, and TAR files. "
        "Knowing an accession/extract contains these objects is important as a single archive file may contain many "
        "hundreds of other files that also need to be preserved and looked after."
    )

    HEADING_DESC_IDENTICAL_CONTENT = (
        "This is a list of files that are identical byte for byte. Count: is the number of instances of a "
        "particular checksum value that are found across the accession/extract. Filepath is listed to help "
        "with locating the object and to help appraisal decisions if the purpose of the duplicate can be "
        "ascertained. In the majority of cases if a duplicate is received it will be ingested as-is as that "
        "is what was received."
    )

    HEADING_DESC_TROUBLESOME_FILENAMES = (
        "Lists filenames that may cause issues across different systems and applications. These could "
        "be filenames that include UTF-8 characters such as macrons, or incidences of filenames with "
        "multiple space characters following one after the other. Filenames identified will also include "
        "those for which there is an explicit recommendation against from "
        "<a href='https://msdn.microsoft.com/en-nz/library/windows/desktop/aa365247%28v=vs.85%29.aspx?f=255&MSPPError=-2147217396'>Microsoft</a>"
    )

    HEADING_DESC_TROUBLESOME_DIRNAMES = (
        "Lists drectory names that may cause issues across different systems and applications. These "
        "could be directory names that include UTF-8 characters such as macrons, or incidences of "
        "filenames with multiple space characters following one after the other. Directory names identified "
        "will also include those for which there is an explicit recommendation against from "
        "<a href='https://msdn.microsoft.com/en-nz/library/windows/desktop/aa365247%28v=vs.85%29.aspx?f=255&MSPPError=-2147217396'>Microsoft</a>"
    )

    HEADING_BLACKLIST_IDS = "Blacklist Identifiers found in Accession/Extract"
    HEADING_BLACKLIST_EXTS = "Blacklist Filename Extensions found in Accession/Extract"
    HEADING_BLACKLIST_DIRS = "Blacklist Directory Names found in Accession/Extract"
    HEADING_BLACKLIST_FILENAMES = "Blacklist Filenames found in Accession/Extract"
    HEADING_DESC_BLACKLIST = """Lists objects which are considered undesirable inside an accession/extract.
                               The blacklist is entirely configurable by user and may contain files that can be
                               identified as undesirable, e.g. system files; or file names that may need pre-conditioning
                               e.g. with the title 'Untitled Document'. Filename and directory searches are greedy and will
                               look for instances of the strings specified in the blacklist within filename and directory
                               strings using a wildcard search. IDs e.g. PUID identifiers, and filename extension searches
                               are understandably more precise."""

    TEXT_ONLY_FIVE_TOP_PUIDS = "Five Top PUIDs in Accession/Extract"
    TEXT_ONLY_FIVE_TOP_EXTENSIONS = "Five Top Extensions in Accession/Extract"

    COLUMN_HEADER_VALUES_NAMESPACE = "Namespace"
    COLUMN_HEADER_VALUES_ID = "ID"
    COLUMN_HEADER_VALUES_FORMAT = "Format Name"
    COLUMN_HEADER_VALUES_COUNT = "Count"
    COLUMN_HEADER_VALUES_YEAR = "Year"
    COLUMN_HEADER_VALUES_YEAR = "Volume"

    FNAME_CHECK_ASCII = "contains, characters outside of ASCII range"
    FNAME_CHECK_PERIOD = "has a period '.' as its last character"
    FNAME_CHECK_NOT_RECOMMENDED = "contains, non-recommended character"
    FNAME_CHECK_NON_PRINT = "contains, non-printable character"
    FNAME_CHECK_RESERVED = "contains, reserved name"
    FNAME_CHECK_SPACE = "has a SPACE as its last character"

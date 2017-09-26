# Reading from and writing to a text file
''' The basic steps are
1. open the file using open("filename", "access method")
2. Read the file using read(), or readline() or readlines()
3. close the file using close(filename) or filename.close()
ACCESS METHODS
===============
'r', 'w', 'a' ==>
(read from an existing file, write to an existing file or create it,
or append to an existing file or create it )
'r+' read and write
'w+' write and read---- overwrites existing file
'a+' read and append --- adds to existing file '''

myfile = open('new file.doc','r+')
for i in range(len(myfile.readlines())):
               myfile.close()
               myfile = open('new file.doc','r+')
               print "Line", i + 1 , ". ", myfile.readline()


myfile.close()

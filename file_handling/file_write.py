#--------------------------------------------------------------------
#Description : Writing into the file 
#Used Function : write()
#Mode : 'w'
#--------------------------------------------------------------------

with open('file1.py','w') as f:
  print("write(This is write function using 'w')");
  f.write("Hey this the write function");

#--------------------------------------------------------------------
#Description : Adding data into the file
#Used Function : write()
#Mode : 'a'
#--------------------------------------------------------------------

with open('file1.py','a') as f:
  print("write(writing data using append it at the end)");
  f.write("--Adding this line --");



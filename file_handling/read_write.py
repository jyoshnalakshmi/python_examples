#--------------------------------------------------------------------
#Description : Appending into the file and reading from the file 
#Used Function : write(), read()
#Mode : 'a+'
#seek() -> Moves the cursor to the character you mention.
#--------------------------------------------------------------------

with open('file2.py','a+') as f:
  print("write(---using a+ mode---)");
  f.write("Hey this the write function");
  f.seek(0);
  print("Reading from file")
  print(f.read());


#--------------------------------------------------------------------
#Description : Writing into the file and reading from the file 
#Used Function : write(), read()
#Mode : 'w+'
#seek() -> Moves the cursor to the character you mention.
#--------------------------------------------------------------------

with open('file2.py','w+') as f:
  print("write(------using w+ mode------)");
  f.write("Hey this the write function");
  f.seek(1);
  print("Reading from file")
  print(f.read());

#--------------------------------------------------------------------
#Description : Replacing the lines with the string/lines given and reading from the file 
#Used Function : write(), read()
#Mode : 'r+'
#seek() -> Moves the cursor to the character you mention.
#--------------------------------------------------------------------

with open('file.py','r+') as f:
  print("write(----using r+ mode-----)");
  f.write("Writing into the file from r+ mode");
  f.seek(0);
  print("Reading from file")
  print(f.read());


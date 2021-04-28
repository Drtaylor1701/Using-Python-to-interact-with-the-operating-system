import os
#deletes files if they exist, otherwise gives a FileNotFound error
os.remove("novel.txt")

#renames a file if it exists, othewise give a FileNotFound error
os.rename("oldname.txt", "newname.txt")

#os.path submodule
#to see if a file exists - returns true or false
os.path.exists("finshed_masterpiece.txt")
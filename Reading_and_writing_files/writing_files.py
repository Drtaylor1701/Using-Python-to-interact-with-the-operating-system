with open("novel.txt", "w") as file:
    # the 'w' is the mode you open the file in
    # by default they are opened in "r"  - read only
    # "w" opens in write mode. If the file doesn't exist, Python will create it and if it exists the current contents will be overwritten as soon ad the file is opened.
    # in "w" mode, you can't read the file's contents - if you try, you get an error.
    # "a" mode appends text to the end of a file
    # "r+" allows you to read and overwrite content
    file.write("It was a dark and stormy night.")
    # write() will return the number of characters written

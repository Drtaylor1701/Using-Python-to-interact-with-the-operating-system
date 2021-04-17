import os

def new_directory(directory, filename):
    # Before creating a new directory, check to see if it already exists
    if os.path.isdir(directory) == False:
        os.mkdir(directory)
        print("Made the directory, boss")

    # Create the new file inside of the new directory
    os.chdir(directory)
    with open (filename) as file:
        pass

    # Return the list of files in the new directory
    #return ___

print(new_directory("PythonPrograms", "script.py"))
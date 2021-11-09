#make a line uppercasse before processing
with open("spider.txt") as file:
    for line in file:
        print(line.upper())

#do it without the newline character at the end of the line
with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())

#read the file lines into a list
file = open("spider.txt")
lines = file.readlines()
file.close()
#lines now has list of lines so we can operate on it
lines.sort()
print(lines)
#lines are now sorted alphabetically

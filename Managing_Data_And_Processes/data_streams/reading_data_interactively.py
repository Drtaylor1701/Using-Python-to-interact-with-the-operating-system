#input function allows us to prompt the user for a value

name = input("Please enter your name: ")
print("Hello, " + name)

#input always returns a string

def to_seconds(hours, minutes, seconds):
    return hours*3600+minutes*60+seconds

print("Welcome to this time converter.")

cont = "y"
while(cont.lower() == "y"):
    #convert the value to int
    hours = int(input("Enter the number of hours "))
    minutes = int(input("Enter the number of miutes "))
    seconds = int(input("Enter the number of seconds "))

    print("That's {} seconds".format(to_seconds(hours, minutes, seconds)))
    print()

    cont = input("Do you want to do another conversion? Press Y to continue.")

print("Good Bye")
# Problem Statement
# We've written a helper function for you called greet(name) which takes as input a string name and prints a greeting. Write some code in main() to get the user's name and then greet them, being sure to call the greet(name) helper function.

def main():
    print("Delete this line and write your code here! :)")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

def main():
    name : str = input("What's your name? ")
    print(greet(name))

# There is no need to edit code beyond this point

def greet(name):
    return "Greetings " + name + "!"
	
if __name__ == '__main__':
    main()

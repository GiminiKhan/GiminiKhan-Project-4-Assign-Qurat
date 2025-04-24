# Problem Statement
# Fill out print_multiple(message, repeats), which takes as parameters a string message to print, and an integer repeats number of times to print message. 

def print_multiple(message: str, repeats: int):
    for i in range(repeats):
        print(message)

def main():
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)

# Corrected line to properly check if the script is being run directly
if __name__ == '__main__':
    main()
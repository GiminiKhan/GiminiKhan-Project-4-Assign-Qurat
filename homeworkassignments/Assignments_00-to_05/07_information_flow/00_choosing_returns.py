# Problem Statement
# There are times where we want to return different things from a function based on some condition. To practice this idea, imagine that we want to check if someone is an adult. We might check their age and return different things depending on how old they are!

def main():
    print("Delete this line and write your code here! :)")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

    ADULT_AGE : int = 18 # U.S. age 

def is_adult(age: int):
    if age >= ADULT_AGE:
        return True
    
    return False
    
########## No need to edit code beyond this point :) ##########

def main():
    age : str = int(input("How old is this person?: "))
    print(is_adult(age))
    

if __name__ == "__main__":
    main()
    
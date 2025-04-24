# Problem Statement
# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

def get_last_element(lst):
    """
    Prints the last element of the provided list.
    """
    # Takes the length of the list and subtracts 1 because it's zero-indexed
    print(lst[len(lst) - 1])
    
    # The line below works too!
    # print(lst[-1])

# You can test it with a main function like this:
def main():
    sample_list = ["\napple", "\nbanana", "\ncherry"]
    get_last_element(sample_list)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
    

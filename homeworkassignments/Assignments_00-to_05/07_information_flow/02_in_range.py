# Problem Statement
# Implement the following function which takes in 3 integers as parameters:

def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    return low <= n <= high

def main():
    n = int(input("Enter a number: "))
    low = int(input("Enter the low end of the range: "))
    high = int(input("Enter the high end of the range: "))

    if in_range(n, low, high):
        print("Yes, the number is within the range.")
    else:
        print("No, the number is not within the range.")

# This line ensures main() runs only when this file is executed directly
if __name__ == '__main__':
    main()
    

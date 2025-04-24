# Problem Statement
# There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.

def main():
    # Dictionary of available fruits and their prices
    fruits = {
        "apple": 0.5,
        "banana": 0.3,
        "orange": 0.8,
        "mango": 1.5
    }
    
    total_cost = 0
    
    # Ask the user how many of each fruit they want to buy
    for fruit_name in fruits:
        price = fruits[fruit_name]
        try:
            amount_bought = int(input(f"How many {fruit_name}s do you want to buy? "))
            total_cost += (price * amount_bought)
        except ValueError:
            print("Please enter a valid number.")
    
    # Print the total cost
    print(f"Your total is: ${total_cost:.2f}")

# Python boilerplate to call the main() function
if __name__ == '__main__':
    main()
    
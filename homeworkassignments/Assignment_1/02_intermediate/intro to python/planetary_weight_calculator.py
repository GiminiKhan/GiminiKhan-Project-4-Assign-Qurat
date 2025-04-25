"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.

Note that the user should type in a planet with 
the first letter as uppercase, and you do not need
to handle the case where a user types in something 
other than one of the planets (that is not Earth). 
"""


# Mars Weight

"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

def main():
    # Fill this function out!
    pass

if __name__ == "__main__":
    main()

    MARS_MULTIPLE = 0.378

def main(): earth_weight_str = input('Enter a weight on Earth: ')

# Get the numeric value since input() returns a value in string form
earth_weight = float(earth_weight_str)

# Having a variable for each piece of information is a good habit
mars_weight = earth_weight * MARS_MULTIPLE
rounded_mars_weight = round(mars_weight, 2)


# Note the string concatenation!
print('The equivalent weight on Mars: ' + str(rounded_mars_weight))
if name == 'main': main()

def main(): # Prompt the user for their weight on Earth earth_weight = float(input("Enter a weight on Earth: "))

    # Prompt the user for the name of a planet
planet = input("Enter a planet: ")

# Determine the gravitational constant for the selected planet
if planet == "Mercury":
    gravity_constant = MERCURY_GRAVITY
elif planet == "Venus":
    gravity_constant = VENUS_GRAVITY
elif planet == "Mars":
    gravity_constant = MARS_GRAVITY
elif planet == "Jupiter":
    gravity_constant = JUPITER_GRAVITY
elif planet == "Saturn":
    gravity_constant = SATURN_GRAVITY
elif planet == "Uranus":
    gravity_constant = URANUS_GRAVITY
else:
    # can assume user types in one of these planets, so this can be an else instead of elif
    gravity_constant = NEPTUNE_GRAVITY

# Calculate the equivalent weight on the selected planet
planetary_weight = earth_weight * gravity_constant
rounded_planetary_weight = round(planetary_weight, 2)

# Print the result
print("The equivalent weight on " + planet + ":  " + str(rounded_planetary_weight))
if name == "main": main()

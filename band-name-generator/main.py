#1. Create a greeting for your program.
#2. Ask the user for the city that they grew up in.

#3. Ask the user for the name of a pet.

#4. Combine the name of their city and pet and show them their band name.

#5. Make sure the input cursor shows on a new line, see the example at:
# ------------------------------------------------------------------------------------


print("Hello, Welcome to the band name generator program")

city_name = input("What's the name of the city you grew up in ? \n")
pet_name = input("What's the name of a pet you like ? \n")


band_name = city_name + pet_name
print(f"Your band name could be: {band_name}")
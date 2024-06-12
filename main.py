# this is the main file that will run the program

# Import the functions from the utility file
from utility import find_plant, compute_average_height

# Define the initial string
data_string = "Rose,Flower,35; Oak,Tree,180; Tulip,Flower,40; Pine,Tree,200; Daisy,Flower,25;"

# Get user input for the plant search
search_term = input("Enter the name of the plant you want to find: ")

# Task 1: Find if the plant exists in the data string and display its info
find_plant(data_string, search_term)

# Task 2: Calculate the average height of all plants
average_height = compute_average_height(data_string)
print("Average Height:", average_height)
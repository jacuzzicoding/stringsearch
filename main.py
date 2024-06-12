# this is the main file that will run the program

# Import the functions from the utility file
from utility import find_object, compute_average

# Define the initial string
data_string = "Rose,Flower,35; Oak,Tree,180; Tulip,Flower,40; Pine,Tree,200; Daisy,Flower,25;"

# Task 1: Find if there is a plant named tulip in the data string and display its info
find_object(data_string, "Tulip")

# Task 2: Calculate the average height of all plants
average_height = compute_average_height(data_string)
print("Average Height:", average_height)
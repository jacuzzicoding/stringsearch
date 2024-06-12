#this will be the utility file for the project
#this file will contain the functions that will be used in the main file

# Function to find an object in the data string

def find_plant(string, search_term):
    # Split the string into individual plants based on the semicolon
    plants = string.split(';')
    # Loop through each plant
    for plant in plants:
        # Split each plant's attributes based on the comma
        attributes = plant.split(',')
        # Check if the search term matches any attribute
        if search_term in attributes:
            print(f"Found: {plant.strip()}")
            return
    print("Not found")

def compute_average_height(string):
    # Split the string into individual plants
    plants = string.split(';')
    total_height = 0
    count = 0
    # Loop through each plant
    for plant in plants:
        # Split each plant's attributes 
        attributes = plant.split(',')
        try:
            # Assuming the height is the last attribute
            height = int(attributes[-1])
            total_height += height
            count += 1
        except ValueError:
            continue
    # Calculate and return the average height
    if count > 0:
        return total_height / count
    else:
        return 0
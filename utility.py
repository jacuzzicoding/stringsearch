#this will be the utility file for the project
#this file will contain the functions that will be used in the main file

# Function to find an object (plant) in the data string
def find_plant(string, search_term):
    # Split the string into individual plants 
    plants = string.split(';')
    for plant in plants:
        # Split each plant's attributes
        attributes = plant.split(',')
        # Check if the search term matches any attribute
        if search_term in attributes:
            print(f"Found: {plant.strip()}")
            return
    print("Not found")

# Function to compute the average height of all plants
def compute_average_height(string):
    # Split the string into individual plants
    plants = string.split(';')
    total_height = 0
    count = 0
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
    
# Function to find the tallest plant in the data string
def find_tallest_plant(string):
    plants = string.split(';')
    tallest_plant = ""
    max_height = 0
    for plant in plants:
        attributes = plant.split(',')
        try:
            height = int(attributes[-1].strip())
            if height > max_height:
                max_height = height
                tallest_plant = plant
        except ValueError:
            continue
    if tallest_plant:
        print(f"Tallest Plant: {tallest_plant.strip()}")
    else:
        print("No valid plant data found")
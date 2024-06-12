# this is the main file that will run the program

# Function to find an object (plant) in the data string
def find_plant(string, search_term):
    # Split the string into individual plants 
    plants = string.split(';')
    for plant in plants:
        # Split each plant's attributes
        attributes = plant.split(',')
        # Check if the search term matches the first attribute (plant name)
        if search_term.strip().lower() == attributes[0].strip().lower():
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


# Define the initial string
data_string = "Rose,Flower,35; Oak,Tree,180; Tulip,Flower,40; Pine,Tree,200; Daisy,Flower,25;"

# Function to display the menu
def display_menu():
    print("Menu:")
    print("1. Search for a plant")
    print("2. Calculate average height of plants")
    print("3. Find the tallest plant")
    print("4. Exit")

# Function to handle user input and display the results
while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        search_term = input("Enter the name of the plant you want to find: ")
        find_plant(data_string, search_term)
    elif choice == "2":
        average_height = compute_average_height(data_string)
        print("Average Height:", average_height)
    elif choice == "3":
        find_tallest_plant(data_string)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")

# Get user input for the plant search
search_term = input("Enter the name of the plant you want to find: ")



# Task 2: Calculate the average height of all plants
average_height = compute_average_height(data_string)
print("Average Height:", average_height)
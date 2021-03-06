destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

### BOREDLESS TOURIST'S FUNCTIONALITY
def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index
    
### LOGIC of list of attractions
attractions = [[] for attraction in destinations]

def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destination)
        attractions_for_destination = attractions[destination_index]
        attractions_for_destination.append(attraction)
        return
    except ValueError: ## Gives error message if destination is not found
        print("Destination doesn't exist")
        return

add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

### LOGIC to find the most interesting places in a new city for a traveler
def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []

    for possible_attractions in attractions_in_city:
        attraction_tags = possible_attractions[1]
        
        for interest in interests:
            if interest == attraction_tags[1]:
                attractions_with_interest.append(possible_attractions[0])
    return attractions_with_interest

### LOGIC to connect people with attractions that they are interested in
def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)
    
    interests_string = "Hi " + str(traveler[0]) + ", we think you'll like these places around " + str(traveler[1]) + ": " + str(traveler_attractions[0])

    return interests_string

## Traveler Dereck
dereck = 'Dereck Smill', 'Paris, France', ['monument']
smills_france = get_attractions_for_traveler(dereck)
print(smills_france)

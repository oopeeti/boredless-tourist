destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

# Traveller Erin Wilkes
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

### BOREDLESS TOURIST'S FUNCTIONALITY
def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

# print("Destination index is: " + str(get_destination_index("Hyderabad, India"))) ## GIVES AN ValueError

def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index
    
# print("Travelers destination index: " + str(get_traveler_location(test_traveler))) ## Prints dindex

test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)

### List of attractions
attractions = [[] for attraction in destinations]
print(attractions)

def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destination)
        attractions_for_destination = attractions[destination_index]
        attractions_for_destination.append(attraction)
        return
    except ValueError:
        print("Destination doesn't exist")
        return

add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

print(attractions)






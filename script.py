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




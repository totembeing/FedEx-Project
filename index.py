from geopy.geocoders import Nominatim
import folium


def getCoordinates(address):
    geolocator = Nominatim(user_agent="geoapiEcercises") #Creates a geolocator object with a user-defined agent name
    location = geolocator.geocode(address) #Uses geolocator to get the coordinates of the given address 
    if location: #checks if the location was found
        return location.latitude, location.longitude
    else:
        None, None


def determineLocation(lat, dividingLat):
    if lat >= dividingLat:
        return "North Barrie"
    else:
        return "South Barrie"
    
def main(address):
    dividingLat = 44.3787 #Taken upto four decimal points, original value: 44.378714

    lat, lon = getCoordinates(address)

    if lat and lon:
        location = determineLocation(lat, dividingLat)
        print(location)
    else: 
        print("Address not found.")

address = "L4N 4V9"
main(address)
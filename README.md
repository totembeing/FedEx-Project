# FedEx-Project

Using "geopy" library to convert the address into latitude and longitude coordinates. 
Using "folium" to visualize the address and the dividing line on map. A library used to create interactive maps.

Geopy serves as an interface to several geocoding services like Nominatim, Google Maps, Bing Maps. In this project, I have used Nominatim.

Geopy uses the selected geocoding service's API to get the coordinates of the given address.

When I called geolocator.geocode(address), geopy sens an HTTP request to the chosen geocoding service's API endpoint with the address I provide.

The geocoding service process my request and returns and appropriate response, which includes the coordinates of the given address.
The response format depends on the service but generally is provided in JSON or XML format.

Geopy parses the response from the geocoding service and extracts relevant information(latitude and longitude).

The Address can be your street address as well postal codes.
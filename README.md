# FedEx-Project

The given project solves a problem that is faced by me and my colleague as a package handler at FedEx Barrie. 

The packages have a serial number on them in the format: xxx-xxxx. 
First three digits tells us what trailer the package should be loaded into.
Sometimes the serial number says that a specific package is meant to go to truck 631, whereas it should be loaded into either truck 624 or 625. 
To determine whether that package should be loaded into truck 624, or truck 625, we have to manually check the address on google maps to find out where the address lies.
If it lies in South-side of Barrie, package should be loaded into 625, otherwise truck 625 for the North-side.

This python programs aims to automate the whole process.

The program takes a string input for the address and uses geopy to find its latitude and longitude. 
Geopy serves as an interface to several geocoding services like Nominatim (used in the project), Google Maps, etc. and uses their API to get the coordinates of the given address.
The dynamically returned latitude of the address, is compared to a pre-defined latitude to determine whether the address lies in North Barrie or South Barrie and gives an output. 



Using "geopy" library to convert the address into latitude and longitude coordinates. 
Using "folium" to visualize the address and the dividing line on map. A library used to create interactive maps.

Geopy serves as an interface to several geocoding services like Nominatim, Google Maps, Bing Maps. In this project, I have used Nominatim.

Geopy uses the selected geocoding service's API to get the coordinates of the given address.

When I called geolocator.geocode(address), geopy sens an HTTP request to the chosen geocoding service's API endpoint with the address I provide.

The geocoding service process my request and returns and appropriate response, which includes the coordinates of the given address.
The response format depends on the service but generally is provided in JSON or XML format.

Geopy parses the response from the geocoding service and extracts relevant information(latitude and longitude).

The Address can be your street address as well postal codes.
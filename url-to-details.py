
# Importing necessary modules
import socket
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance

# A function to provide details about a url
def printDetails(ip):
    res = DbIpCity.get(ip, api_key="free")
    print(f"IP Address: {res.ip_address}")
    print(f"Location: {res.city}, {res.region}, {res.country}")
    print(f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})")
    return 0

url = input("Enter URL: ")
ip_add = socket.gethostbyname(url)
printDetails(ip_add)



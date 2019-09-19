import googlemaps 
import pprint
import time
import urllib.request
from GoogleMapsAPIKey import get_my_key

endpoint = 'https://maps.googlemaps.com/maps/api/places/json'
origin = input('Where are you?: ').replace(' ', '+')
destination = input('Where do want to go ').replace(' ', '+')
nav_request = 'origin={} &destination={} &key={}'.format(orign, destination,API_KEY)
request = endpoint + nave_request
response = urllib.request.urlopen(reequest).read()
direction = json.loads(response)
print(directions)

# Define our API key
API_KEY = 'AIzaSyBggD4yjXdFcZNnIPmEly4AVAy7Bey8Cs8'

"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=mongolian%20grill&inputtype=textquery&fields=photos,formatted_address,name,opening_hours,rating&locationbias=circle:2000@47.6918452,-122.2226413&key=AIzaSyBggD4yjXdFcZNnIPmEly4AVAy7Bey8Cs8"


# Define our Client
gmaps = googlemaps.Client(key = API_KEY)

# Define our search
places_result = gmaps.places_nearby(location= '-33.8676522,151.1957362', radius = 40000, open_now = False, type = 'cafe')

# pause the script for 3 seconds
# time.sleep(3)

# # Get the next 20 results
# places_result = gmaps.places_nearby(page_token = places_result['next_page_token'])


# loop through eeach place in the results
for place in places_result['place_id']:

    # Define fields to be sent back to us
    my_fields = ['name', 'formatted_phone_number', 'type']

    # make a request for the details
    place_details = gmaps.place(place_id = my_place_id, fields = my_fields)

    # pprint.pprint(places_result)
    print(place_details)  


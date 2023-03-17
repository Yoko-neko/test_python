import googlemaps
import webbrowser
import time
from Pillow import Image

location1 = input("まず最初に訪れたい所を入力してクダさい：")
location2 = input("{}から歩いて行きたい場所を入力してください：".format(location1))

api_key = "your_api_key"
gmaps = googlemaps.Client(api_key)
directions = gmaps.directions(location1,location2)

size = "640x640" # size of the image
heading = "0" # direction in which the camera is facing (0 is North, 90 is East, etc.)
pitch = "0" # angle of the camera (0 is horizontal, 90 is straight up, -90 is straight down)

# Call the Street View API and get the image
result = gmaps.streetview(location=location1, size=size, heading=heading, pitch=pitch)

# Save the image to a file
# img = Image.open(BytesIO(result))
# img.save("streetview.jpg")

# Get the distance and duration of the trip
distance = directions[0]['legs'][0]['distance']['value']
duration = directions[0]['legs'][0]['distance']['value']

# cCaluculate the delay between each frame in seconds
delay = distance / (3000 * 60)

# Iterate over the steps and show the Street View for each step
for step in directions[0]['legs'][0]['steps']:
    start_loc = step['start_location']
    end_loc = step['end_location']
    pano_loc = step['street_view_panorama_id']

    # Build the URL for the Street View image
    url = f"https://www.google.com/maps/@?api=1&map_action=pano&pano={pano_id}&heading=0&pitch=0&fov=80" \

    webbrowser.open(url)
    time.sleep(delay)

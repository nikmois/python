import urllib.request, urllib.parse, urllib.error
import json
import ssl

# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
para = {"sensor": "false", "address": address}
parameters = urllib.parse.urlencode(para)
url = serviceurl + parameters
print('Retrieving', url)

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

js = json.loads(data)
place_id = js["results"][0]["place_id"]

print(place_id)

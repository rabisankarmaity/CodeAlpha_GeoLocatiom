import requests
import time

# OpenCage Geocoding API function
def get_loc(adr, api_key):
    time.sleep(1)
    url = f"https://api.opencagedata.com/geocode/v1/json?q={adr}&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            return data['results'][0]
        else:
            return None
    else:
        return None

# AbstractAPI phone number tracker function
def track_phone_number(phone_number, api_key):
    url = f"https://phonevalidation.abstractapi.com/v1/?api_key={api_key}&phone={phone_number}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


print('-'*10)
adr = input('Enter the name of a country/state/city: ')
phone_number = input('Enter the phone number to track (with country code): ')

#API keys
geocoding_api_key = 'ae9e3a4783d74237ab96ccb999c26d53'
phone_validation_api_key = '36f6ce6de34f4eab92a4f40546b2444f'


location = get_loc(adr, geocoding_api_key)
if location:
    lat = location['geometry']['lat']
    lon = location['geometry']['lng']
    name = location['formatted']

 
    print(f'Location = {name}\nLatitude = {lat}\nLongitude = {lon}')
else:
    print('Failed to retrieve location details.')

# Get phone number details
phone_details = track_phone_number(phone_number, phone_validation_api_key)
if phone_details:
    print(f"Phone Number = {phone_number}")
    print(f"Country = {phone_details.get('country', 'N/A')}")
    print(f"Location = {phone_details.get('location', 'N/A')}")
    print(f"Carrier = {phone_details.get('carrier', 'N/A')}")
    print(f"Line Type = {phone_details.get('line_type', 'N/A')}")
else:
    print("Failed to retrieve phone number details.")

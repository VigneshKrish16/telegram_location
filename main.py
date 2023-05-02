from telethon import TelegramClient, sync
from telethon.tl.functions.account import GetAuthorizationsRequest

# Set up a new Telegram client instance
client = TelegramClient('sen_ne_123352133993226', '28840942', '038305e093c7efd9fed3e13b44194686')

# Connect to the Telegram client using the provided phone number and password
client.start('+919486659224', 'sharandon@23')

# Get the user ID of the person you want to obtain the IP address for
user_id = 'SPIDEY1606'

# Get a list of all active sessions for the user

sessions = client(GetAuthorizationsRequest())

# Get the IP address for each active session
for session in sessions.authorizations:
    if session.current:
        ip_address = session.ip
        print(f"IP address for user {user_id}: {ip_address}")

# Import the necessary libraries
import geocoder

# Obtain the user's consent
consent = input("Do you consent to share your location? (yes/no): ")
if consent.lower() == "yes":
    # Retrieve the user's location data
    g = geocoder.ip('162.216.141.2')#enter the ip address obtained
    latitude = g.latlng[0]
    longitude = g.latlng[1]
    print("Your current location is:", latitude, longitude)
    # Send the location data to the receiver
    # Use a messaging or video chat API to send the location data to the receiver
else:
    print("Location sharing denied.")
# Import the necessary libraries
from geopy.geocoders import Nominatim

# Enter the longitude and latitude coordinates
latitude = latitude
longitude = longitude

# Create a geolocator object and retrieve the user's location
geolocator = Nominatim(user_agent="my_location")
location = geolocator.reverse(f"{latitude}, {longitude}")

# Print the user's location
print(location.address)

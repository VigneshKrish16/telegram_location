from telethon import TelegramClient, sync
from telethon.tl.functions.account import GetAuthorizationsRequest

# Set up a new Telegram client instance
client = TelegramClient('sen_ne_123352133993226', '28840942', '038305e093c7efd9fed3e13b44194686')#create a section randomly

# Connect to the Telegram client using the provided phone number and password
client.start('+919486659224', 'sharandon@23')#enter callee phone number and password

# Get the user ID of the person you want to obtain the IP address for
user_id = 'SPIDEY1606' #here you have to enter the callee's telegram username

# Get a list of all active sessions for the user

sessions = client(GetAuthorizationsRequest())

# Get the IP address for each active session
for session in sessions.authorizations:
    if session.current:
        ip_address = session.ip
        print(f"IP address for user {user_id}: {ip_address}")


#the respected IP address of the callee will be genrated here.
#then copy the IP address of the callee and enter in Caller location via IP Address program .

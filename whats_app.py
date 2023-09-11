from twilio.rest import Client

# Replace these with your Twilio credentials
account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
sandbox_number = '+919540070017'
# number = +919540070017

# List of recipient numbers in international format (e.g., +1 for the US)
recipient_numbers = ['+919717580196', '+918766393870', '+918130524691']

# Message to be sent
message = "Hello from Twilio! This is a WhatsApp message."

try:
    # Create a Twilio client
    client = Client(account_sid, auth_token)

    # Send the message to each recipient number
    for number in recipient_numbers:
        message = client.messages.create(
            from_='whatsapp:' + sandbox_number,
            to='whatsapp:' + number,
            body=message
        )
        print(f"Message sent to {number}. SID: {message.sid}")

except Exception as e:
    print(f"Error occurred: {e}")

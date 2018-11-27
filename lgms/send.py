from twilio.rest import Client

account_sid = 'ACf21d2b233b596594c0f99ec98fc1f85b'

auth_token = '4de07dfd813efc5b4f4a804ad25ffe33';

client = (account_sid, auth_token)

message = client.message.create(
    to="+639175960403",
    from_="+19032707693",
    body="Hello from LGMS"
)

print(message.sid)

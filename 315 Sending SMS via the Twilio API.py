from twilio.rest import Client

account_sid = "AC45f747f1f5981d4fd69679b4a7841078"
auth_token = "449e91740fb3837375978694160f0f6a"
client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+8801685336744",
    from_="+18317447758",
    body="sdhrudgh"
)

print(message.sid)
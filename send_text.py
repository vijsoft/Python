from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC07fc6782241b45057d6bd42937c145f4"
# Your Auth Token from twilio.com/console
auth_token  = "8c8863c9fc7c9701409d3239c93a6a7e"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+919340900459", 
    from_="+13347212390",
    body="This is Preeti Hingorani from Python!")

##call = client.calls.create(
##                        url='http://demo.twilio.com/docs/voice.xml',
##                        to='+918982887773',
##                        from_='+13347212390'
##                    )
##
##print(call.sid)
print(type(client))
print(type(message))
print(message.sid)

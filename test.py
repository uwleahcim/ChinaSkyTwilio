from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC555f4c62c3e64e84713d48165c9b7ac2"
# Your Auth Token from twilio.com/console
auth_token  = "061282e7b36fec165f9117339055505c"

client = Client(account_sid, auth_token)

# message = client.messages.create(
#     to="+17816005224", 
#     from_="+17812306220",
#     body="Hello from Python!")
# print(message.sid)

to_phone = '7816005224'

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='sip:' + to_phone + '@wap.thinq.com?X-account-id=13302&X-account-token=3ebd540dababb4b0f67b092bb458875653772ddf',
                        from_='+17817296899'
                    )
print(call.sid)


# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC473ea59d5754b0141f8bc5e6f4159e4b"
auth_token = "604c6eb2b506ba23d19300a863109c46"
client = Client(account_sid, auth_token)

""" verification = client.verify.v2.services('VA33258626b1e5f2a3ff10f7fb7668a79c') \
            .verifications \
            .create(to="+21655554907", channel="sms")

print(verification.status) """

verification_check = client.verify.v2.services('VA33258626b1e5f2a3ff10f7fb7668a79c') \
            .verification_checks \
            .create(to="+21655554907", code='649338')
print(verification_check.status)



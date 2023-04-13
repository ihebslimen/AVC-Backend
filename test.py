import jwt

# Create a payload for the JWT token
payload = {
    'user_id': 123,
    'email': 'user@example.com'
}

# Encode the payload into a JWT token
secret_key = 'my_secret_key'
token = jwt.encode(payload, secret_key, algorithm='HS256')
print(token)

# Decode the JWT token and verify the signature
decoded_token = jwt.decode(token, secret_key, algorithms=['HS256'])
print(decoded_token)

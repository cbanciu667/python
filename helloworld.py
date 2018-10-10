import os
import hvac

# Using plaintext
# client = hvac.Client()
# client = hvac.Client(url='http://192.168.0.101:8200')
client = hvac.Client(url='http://192.168.0.101:8200')

client.token = 'd7eba146-0a1b-5bd0-c5ac-a25c6bb2e39b'
assert client.is_authenticated() # => True

print(client.read('secret/pass01'))

# Using TLS
# client = hvac.Client(url='https://localhost:8200')

# Using TLS with client-side certificate authentication
# client = hvac.Client(url='https://localhost:8200', cert=('path/to/cert.pem', 'path/to/key.pem'))

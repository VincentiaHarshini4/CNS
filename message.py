import hmac
import hashlib

def generate_mac(message, key):
    mac = hmac.new(key.encode(), message.encode(), hashlib.sha256)
    return mac.hexdigest()

message = "Hello, this is a secure message."
key = "secretkey123"

mac = generate_mac(message, key)
print("Message:", message)
print("MAC:", mac)
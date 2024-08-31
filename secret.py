from cryptography.fernet import Fernet

API_WEBSITE_KEY = 'P2CDBP4-Z4946D6-KTBTY14-Y28Z30E'

key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(API_WEBSITE_KEY.encode())

'''
Created on 08.06.2016

@author: cypher9
'''
from Crypto.Cipher import AES
import base64

BLOCK_SIZE = 32
PADDING = '{'
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

def encryption(key, privateInfo): 
    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s))) 
    cipher = AES.new(pad(key))
    encoded = EncodeAES(cipher, privateInfo)
    
    return encoded

def decryption(key, encryptedString):
    DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
    cipher = AES.new(pad(key))
    decoded = DecodeAES(cipher, encryptedString)
    
    return decoded
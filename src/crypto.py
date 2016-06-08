'''
Created on 08.06.2016

@author: cypher9
'''
from Crypto.Cipher import AES
import base64

def encryption(key, privateInfo):
    BLOCK_SIZE = 16
    PADDING = '{'
    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
    secret = pad(key)
    cipher = AES.new(secret)
    encoded = EncodeAES(cipher, privateInfo)
    
    return encoded

def decryption(key, encryptedString):
    PADDING = '{'
    DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
    encryption = encryptedString
    key = ''
    cipher = AES.new(key)
    decoded = DecodeAES(cipher, encryption)
    print decoded
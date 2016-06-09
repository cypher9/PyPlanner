'''
Created on 08.06.2016

@author: cypher9
'''
import random, base64, hashlib
from Crypto.Cipher import AES

BLOCK_SIZE = 32
PADDING = '{'
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
KEY = None

def generate_key(password):
    key = hashlib.sha256(password).digest()    
    return key

def set_password():
    global KEY
    not_matching = True
    while not_matching:
        key = generate_key(str(raw_input("Enter Password: ")))
        key_repeat = generate_key(str(raw_input("Repeat Password: ")))
        if key == key_repeat:
            KEY = key
            not_matching = False
        else:
            print("passwords not matching")
    

def encryption(privateInfo):
    global KEY
    iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16)) 
    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
    if KEY:
        key = KEY
    else:
        key = generate_key(str(raw_input("Enter Password: "))) 
        KEY = key
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    encoded = EncodeAES(encryptor, privateInfo)
    return iv+encoded  
                
def decryption(encrypted_xml):
    global KEY
    DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
    iv = encrypted_xml[:16]
    encrypted_xml = encrypted_xml[16:]
    if KEY:
        key = KEY
    else:
        key = generate_key(str(raw_input("Enter Password: ")))
        KEY = key 
    decryptor = AES.new(key, AES.MODE_CBC, iv)
    decoded = DecodeAES(decryptor, encrypted_xml)
    return decoded
        
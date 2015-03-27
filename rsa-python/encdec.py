#!/usr/bin/env python
# -*- coding: utf-8 -*-

generate = 1	# generate new keys?


def encrypt_RSA(key, message):
  '''
  param: public_key_loc Path to public key
  param: message String to be encrypted
  return base64 encoded encrypted string
  '''
  from Crypto.PublicKey import RSA
  from Crypto.Cipher import PKCS1_OAEP
  #key = open(public_key_loc, "r").read()
  rsakey = RSA.importKey(key)
  rsakey = PKCS1_OAEP.new(rsakey)
  encrypted = rsakey.encrypt(message)
  return encrypted.encode('base64') 


def decrypt_RSA(private_key, package):
  '''
  param: public_key_loc Path to your private key
  param: package String to be decrypted
  return decrypted string
  '''
  from Crypto.PublicKey import RSA
  from Crypto.Cipher import PKCS1_OAEP
  from base64 import b64decode
  #key = open(private_key_loc, "r").read()
  rsakey = RSA.importKey(private_key)
  rsakey = PKCS1_OAEP.new(rsakey)
  decrypted = rsakey.decrypt(b64decode(package))
  return decrypted 

def generate_RSA(bits=2048):
  '''
  Generate an RSA keypair with an exponent of 65537 in PEM format
  param: bits The key length in bits
  Return private key and public key
  '''
  from Crypto.PublicKey import RSA
  new_key = RSA.generate(bits)
  public_key = new_key.publickey().exportKey("PEM")
  private_key = new_key.exportKey("PEM")
  return private_key, public_key 
  


if generate == 1:
    prv, pub = generate_RSA()
    fileout = open('rsa_key.pub', 'w')
    fileout.write(pub)
    fileout.close()

    fileout = open('rsa_key.sec', 'w')
    fileout.write(prv)
    fileout.close()

else:
    filein = open('rsa_key.pub', 'r')
    pub = filein.read()
    filein.close()

    filein = open('rsa_key.sec', 'r')
    prv = filein.read()
    filein.close()


#print prv
#print pub

encMessage = encrypt_RSA(pub, "to jest test śćńół / this is a test")

try:
  decMessage = decrypt_RSA(prv, encMessage)

except ValueError:
  print "Błąd deszyfracji!"

else:
  print decMessage


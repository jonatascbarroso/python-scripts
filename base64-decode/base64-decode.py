'''
This script decode a base64 file
'''

import base64


inputFile = input('Base64 file to be decoded? ')
data = open(inputFile, "r").read()
decoded = base64.b64decode(data)

outputFile = input('Output file? ')
with open(outputFile, "wb") as f:
	f.write(decoded)

print('Done')
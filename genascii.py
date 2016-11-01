import os

os.mkdir('ascii')
print("Generating ascii files...")
for n in range(0, 256):
	with open('ascii/ascii' + str(n) + '.txt', 'wb') as f:
		f.write(n.to_bytes(1, byteorder='big'))
print("DONE!")

from sc_compression.decompressor import Decompressor
from reader import Reader
decompressor = Decompressor()
fileName = input('Enter file name (Without Format): ')
file = open(fileName + '.sc', 'rb')
text = open(fileName + '.txt', 'w')
file_data = decompressor.decompress(file.read())
file.close()
reader = Reader(file_data)
for x in range(6):
	reader.readUShort()
reader.readUByte()
reader.readUInt32()
exports_count = reader.readUShort()
for x in range(exports_count):
	reader.readUShort()
for x in range(exports_count):
	with open(fileName + '.txt', 'a') as f:
		f.write(reader.readString() +"\n")
print("All export names saves in ", fileName + '.txt')
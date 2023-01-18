import hashlib

# Open the image file
with open("riad-zyo.jpg ", "rb") as image_file:
    # Read the image data
    image_data = image_file.read()
    # Create a new SHA-256 hash object
    sha256 = hashlib.sha256()
    # Update the hash object with the image data
    sha256.update(image_data)
    # Get the hexadecimal representation of the hash
    hex_data = sha256.hexdigest()
    # Print the hexadecimal data
    print(hex_data)

'''


import struct
from PIL import Image


# Open the image file
image = Image.open("riad-zyo.jpg")

# Convert the image to binary
ba = bitarray()
ba.frombytes(image.tobytes())

# Truncate or pad the binary to 128 bits
if len(ba) < 128:
    ba.extend([0]*(128 - len(ba)))
else:
    ba = ba[:128]

# Convert the binary to a fixed-length 128-bit string
binary_data = struct.pack('>128b', *ba.tolist())

# Add the prefix "ff" to the beginning of the binary code
binary_data = b"ff" + binary_data

print(binary_data)

'''

'''
from PIL import Image

# Open the image file
image = Image.open("riad-zyo.jpg")

# Convert the image to binary
binary_data = image.tobytes()

# Truncate or pad the binary to 128 bits
if len(binary_data) < 16:
    binary_data += b'\ x00' * (16 - len(binary_data))
else:
    binary_data = binary_data[:16]

print(binary_data)

from PIL import Image
import binascii

# Open the image file
image = Image.open("riad-zyo.jpg")
# Convert the image to hexadecimal
hex_data = binascii.hexlify(image.tobytes()).decode("utf-8")

# Truncate or pad the hex code to 128 bits
if len(hex_data) < 32:
    hex_data += '0' * (32 - len(hex_data))
else:
    hex_data = hex_data[:32]

print(hex_data)




from PIL import Image
import binascii

# Open the image file
image = Image.open("riad-zyo.jpg")

# Convert the image to binary
binary_data = image.tobytes()

# Truncate or pad the binary to 128 bits
if len(binary_data) < 16:
    binary_data += b'\x00' * (16 - len(binary_data))
else:
    binary_data = binary_data[:16]

#Convert the binary data to hexadecimal
hex_data = binascii.hexlify(binary_data)

print(hex_data)'''
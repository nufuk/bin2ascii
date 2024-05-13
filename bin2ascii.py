import sys
import re
from bitarray import bitarray

if len(sys.argv) != 2:
   print("Please provide bitstream to decode")
   print("exiting")
   sys.exit(1)
full_string = sys.argv[1]
full_string = re.sub(r"\s+", "", full_string)

i = 0
message = ""
while i < len(full_string):
    try:
      bts = bitarray(full_string[i:i+8])
      message = message + bts.tobytes().decode("ascii")
    except UnicodeDecodeError:
       print("not 7 bit ascii value")
    i = i + 8

print(message)
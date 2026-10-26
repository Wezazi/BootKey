import codecs

output = codecs.decode("48656c6c6f", "hex") # The "hex" argument makes it interpret every pair of hexadecimal digits as one byte
print(output) #returns "bytes", not sure why the default byte representation isn't binary.
print(type(output))
print() #print() automatically returns a new line, so if you type print("\n") it returns two lines instead

output = codecs.decode("48656c6c6f", "hex").decode("ascii") 
print(output) #Returns ascii representation of the bytes
print(type(output))
print()

output = list(codecs.decode("48656c6c6f", "hex"))
print(output) #returns list where every list item is the hexadecimal representation of each byte

for item in output:
    print(type(item))









import binascii
gif = binascii.unhexlify('47494638396101000100800000000000ffffff21f9'
                         '0401000000002c000000000100010000020144003b')
valid_gif = b'GIF89a'
print(gif[0:6] == valid_gif)

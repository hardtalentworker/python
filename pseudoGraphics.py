from six import unichr

for y in range(0x2500, 0x2580, 0x10):
    print (u' '.join(unichr(x) for x in range(y, y+0x10)))

print (u'\u2550\u2551\u2552')

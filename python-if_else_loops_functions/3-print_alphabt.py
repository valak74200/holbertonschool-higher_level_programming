#!/usr/bin/python3


for i in range(ord('a'), ord('z') + 1):
    if i == ord('e') or i == ord('q'):
        continue
    else:
        print('{}'.format(chr(i)), end="")
        
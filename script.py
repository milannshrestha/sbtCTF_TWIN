#!/usr/bin/env python3

import base64
import os
import collections

empty = []

dir_list = os.listdir()
for i in dir_list:
        try:
                with open(i) as f:
                        for x in f:
                                decode = base64.b64decode(x)
                                ascii_decode = str(decode, 'utf-8')
                                empty.append(ascii_decode)
        except:
                pass

a = ([item for item, count in collections.Counter(empty).items() if count > 1])
print ("[+] Flag ", a)

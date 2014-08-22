#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  7.py
#  

from PIL import Image
import re

im = Image.open('oxygen.png')

pix = [im.getpixel((x,45)) for x in range(0, im.size[0], 7)]

ord = [r for r, g, b, k in pix if r ==g == b]

print(''.join(map(chr, map(int, re.findall('\d+', ''.join(map(chr, ord)))))))
	



#!/usr/bin/env python3
import os
#import PIL
from PIL import Image

image_dir = '/home/student-04-50053ed25bb7/supplier-data/images/'
for file in  os.listdir(image_dir):
  print(file)
  if file.endswith('.tiff'):
    im = Image.open(image_dir + file)
    im.convert('RGB')

    im.resize((600,400)).save(image_dir + file[0:len(file)-4]+'jpeg', 'JPEG')
    print(file[0:len(file)-4]+'JPEG')


#!/usr/bin/python3
import os
import requests
url = 'http://localhost/upload/'
image_dir = '/home/student-04-50053ed25bb7/supplier-data/images/'
for file in os.listdir(image_dir):
  if file.endswith('jpeg'):
    with open(image_dir + file,'rb') as f:
      print(f)
      r=requests.post(url,files={'file':f})
      print(r.status_code)
      print(r.text)

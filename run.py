
#!/usr/bin/env python3
import os
import requests

def format_weight(weight):
  return int(weight[0:len(weight)-5])

image_dir = '/home/student-04-50053ed25bb7/supplier-data/images/'
url ='http://localhost/fruits/'
desc_dir = '/home/student-04-50053ed25bb7/supplier-data/descriptions/'
upload_dict = {
        "name": "",
        "weight": 0,
        "description": "",
        "image_name": ""
}

for file in os.listdir(desc_dir):
 with open(desc_dir + file) as f:
  lines = f.readlines()
  #print(lines[2])
  #print(lines[1])
  upload_dict['name']=lines[0]
  upload_dict['weight']=format_weight(lines[1])
  upload_dict['description']=lines[2]
  upload_dict['image_name']=file.replace('.txt','.jpeg')
  r=requests.post(url,data=upload_dict)
  print(r.text)
  #print(f)
  #for line in f:
    #print(line)
   # for key, value in upload_dict.items():
    #  upload_dict[key]= f.readline()
print(upload_dict)

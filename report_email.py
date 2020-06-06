#!/usr/bin/env python3
import os
import datetime
#import pdf_sample
import reports

def get_title():
    return 'Processed Update on ' + datetime.datetime.today().strftime('%Y-%m-%d')


def get_body():
  body='<br/>'
  desc_dir = '/home/student-04-50053ed25bb7/supplier-data/descriptions/'
  for file in os.listdir(desc_dir):
    with open(desc_dir + file) as f:
      lines = f.readlines()
      print(lines[0])
      print(lines[1])
      body += lines[0]
      body += lines[1]
      body += '<br/>'
  return body
#print(get_body())
#print(get_title())
if __name__ == "__main__":

  reports.generate_report('/tmp/processed.pdf', get_title(),get_body())

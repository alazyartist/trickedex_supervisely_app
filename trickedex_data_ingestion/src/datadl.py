#%%writefile main.py

import requests
import json
import re
import locale
import os

def main():
  response = requests.get("https://trickedex.app/api/ml")
  data = response.json()

  cleandata = []

  for el in data:
    for sd in el['SessionData']:
      obj = {'name':el['name'],'Label':sd['ClipLabel']['name'],'vidsrc':sd['SessionSource']['vidsrc'],'clipStart':convertTime(sd['clipStart']),'clipEnd':convertTime(sd['clipEnd']),'comboArray':sd['ClipLabel']['comboArray']}
      cleandata.append(obj)
  os.system('mkdir vids')
  os.system('mkdir clips')
  processed = []
  count = 0
  for link in cleandata:
    if link['name'] not in processed:
      print('Downloading Video',count,link['name'])
      count +=1
      processed.append(link['name'])
  ##Download yt vid once
      command = f"yt-dlp {cleanLinks(link['vidsrc'])} -f 22 -o 'vids/{cleanFilename(link['name'])}.mp4'"
      os.system(command)
      print(command)
      # print(link['vidsrc'])
      # print(link['name'])

  for link in cleandata:
    print('Making Clip',cleanFilename(link['name']+'-'+link['Label']))
    # print(link['clipStart'],link['clipEnd'])
    command = f"ffmpeg -i 'vids/{cleanFilename(link['name'])}.mp4' -ss {link['clipStart']} -to {link['clipEnd']} -c:v copy 'clips/{cleanFilename(link['Label'])}/{cleanFilename(link['name']+'-'+link['Label'])}.mp4' -y"
    command = command.replace('"','')
    mkcommand = f"mkdir 'clips/{cleanFilename(link['Label'])}'"
    os.system(mkcommand)
    os.system(command)
    print(mkcommand)  
    print(command)  

def getpreferredencoding(do_setlocale = True):
    return "UTF-8"
locale.getpreferredencoding = getpreferredencoding
# Install dependencies, download the video, and crop 5 seconds for processing
# !pip install -U youtube-dl
# !youtube-dl https://www.youtube.com/watch?v=WsEjW8CCgtE -f 22 -o video.mp4
#!pip install -U yt-dlp

def convertTime(time_val):

  # Convert time value to hours, minutes, and seconds
  minutes, seconds = divmod(time_val, 60)
  hours, minutes = divmod(minutes, 60)

  # Format output string as HH:MM:SS
  time_str = "{:02d}:{:02d}:{:02d}".format(int(hours), int(minutes), int(seconds))
  return time_str

def cleanLinks (link):
  yt ='https://www.youtube.com/watch?v='
  repl =['https://youtu.be/',
  'https://www.youtube.com/shorts/','https://youtube.com/shorts/']
  for r in repl:
    link = link.replace(r,yt)
    link = link.replace('?feature=share','')
    pattern = r'&t=\d+s.*'
    link = re.sub(pattern,'',link)
  return link

def cleanFilename (name):
  name = name.replace(' ','')
  name = name.replace('>','-')
  name = name.replace('~','')
  name = name.replace('"','')
  return name

if __name__ == "__main__":
    main()
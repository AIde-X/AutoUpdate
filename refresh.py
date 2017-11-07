from selenium import webdriver

import urllib
import time
import os
import pygame
#driver = webdriver.Firefox()
#driver.get('http://reg.exam.dtu.ac.in/')
uri = "https://www.facebook.com/sagnik.bhowmick.90?ref=bookmarks"  #url where result will be declared
source = urllib.urlopen(uri).read()
nw_source=source 
cntr=0
flg=True
while nw_source==source:
    if flg:
      time.sleep(5)  #refresh every 5 seconds
    try:
      nw_source = urllib.urlopen(uri).read()
    except IOError:
      print "Error in reading url"
      flg=False
      continue 
    cntr+=1
    print cntr," times refreshed"
  
    flg=True
pygame.init()
pygame.mixer.music.load("NUCLEYA - Raja Baja - 05 Lights.mp3") #pass the path to the music file
pygame.mixer.music.play()
while True:
  pass

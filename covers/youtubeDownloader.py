from pytube import YouTube
from moviepy.editor import *
import os
import sys

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())

#Go to https://www.youtube.com/
driver.get("https://www.youtube.com/")

#Find and click Sign in button
driver.find_element_by_xpath("//paper-button[@aria-label='Sign in']").click()

#Type in Email
driver.find_element_by_xpath("//input[@type='email']").send_keys("tinglewisp")

#Click Next
driver.find_element_by_xpath("//div[@class='VfPpkd-RLmnJb']").click()

time.sleep(3)

#Type in Password
driver.find_element_by_xpath("//input[@type='password']").send_keys("clappersglee9610")
#driver.execute_script("arguments[0].value = '{}';".format("clappersglee9610"), passwordElement)

#Click Next
driver.find_element_by_xpath("//div[@class='VfPpkd-RLmnJb']").click()

time.sleep(3)

#Search for creative commons ASMR videos
driver.get("https://www.youtube.com/results?search_query=" + sys.argv[1] + "&sp=CAESBhABGAEwAQ%253D%253D")

time.sleep(2)
# &sp=EgIQAQ%253D%253D
# &sp=EgQQARgB
# &sp=EgYQARgBMAE%253D
# &sp=CAESBhABGAEwAQ%253D%253D

#Scroll down to get more videos
#driver.execute_script("scroll(0, 10000);")

linkFile = open("links.txt", "x")
linkFile = open("links.txt", "w")

#Find videos
videos = driver.find_elements_by_xpath("//a[@id='thumbnail']")
time.sleep(2)

for x in range(len(videos)):
	#Get link from video
	videoLink = videos[x].get_attribute("href")

	#Check for last video
	if (str(videoLink) == "None"):
		break
	else:
		linkFile.write(videoLink + "\n")

linkFile = open("links.txt", "r")

catFile = open("cat.txt", "x")
catFile = open("cat.txt", "w")

desFile = open("des.txt", "x")
desFile = open("des.txt", "w")

os.system("mkdir " + sys.argv[1])

desFile.write("Check out the originals!\n\n")

x = 0

for line in linkFile:

	desFile.write(line + "\n")

	yt = YouTube(line)

	title = yt.title
	duration = yt.length

	print(yt.streams.all())

	yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(filename="clip" + str(x))

	command = "ffmpeg -i 'clip" + str(x) + ".mp4' -vf scale=1080:720,setdar=1:1,fps=30 'clip" + str(x) + "-edit.mp4'"
	print(command)

	os.system(command)


	command = "ffmpeg -i 'clip" + str(x) + "-edit.mp4' -vf 'fade=t=in:st=0:d=3,fade=t=out:st=" + str(duration-3) +":d=3' 'clip" + str(x) + "-final.mp4'"
	print(command)

	os.system(command)


	catFile.write("file clip" + str(x) + "-final.mp4\n")

	x = x + 1

clipStr1 = ""

for y in range(x):
	clipStr1 = clipStr1 + " -i clip" + str(y) + "-final.mp4"

print(clipStr1)

clipStr2 = ""

for z in range(x):
	clipStr2 = clipStr2 + "[" + str(z) + ":v:0][" + str(z) + ":a:0]"

clipStr2 = clipStr2 + "concat=n=" + str(x) + ":v=1:a=1[outv][outa]"

print(clipStr2)

command = "ffmpeg" + clipStr1 + " -filter_complex '" + clipStr2 + "' -map '[outv]' -map '[outa]' " + sys.argv[1] + ".mp4"
print(command)
os.system(command)

#clean up

command = "mv " + sys.argv[1] + ".mp4 ./" + sys.argv[1] + "/" + sys.argv[1] + ".mp4"
print(command)
os.system(command)

command = "mv des.txt ./" + sys.argv[1] + "/des.txt"
print(command)
os.system(command)

os.system("rm *.mp4 *.txt")




	

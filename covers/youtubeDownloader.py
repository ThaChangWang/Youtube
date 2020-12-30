from pytube import YouTube
from moviepy.editor import *
import pandas as pd
import os
import sys

Data = pd.read_csv('links.csv', sep=r'\s*,\s*',
                           header=0, encoding='ascii', engine='python')
links = Data["link"]
names = Data["name"]

catFile = open("cat.txt", "x")
catFile = open("cat.txt", "w")

desFile = open("des.txt", "x")
desFile = open("des.txt", "w")

os.system("mkdir " + sys.argv[1])

desFile.write("Check out the originals!\n\n")


for x in range(len(links)):

	desFile.write(links[x] + " - " + names[x] + "\n")

	yt = YouTube(links[x])

	title = yt.title
	duration = yt.length

	print(yt.streams.all())

	yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(filename="clip" + str(x))

	command = "ffmpeg -i 'clip" + str(x) + ".mp4' -vf scale=640:640,setdar=1:1,fps=30 'clip" + str(x) + "-edit.mp4'"
	print(command)

	os.system(command)


	command = "ffmpeg -i 'clip" + str(x) + "-edit.mp4' -vf 'fade=t=in:st=0:d=3,fade=t=out:st=" + str(duration-3) +":d=3' 'clip" + str(x) + "-final.mp4'"
	print(command)

	os.system(command)


	catFile.write("file clip" + str(x) + "-final.mp4\n")

clipStr1 = ""

for x in range(len(links)):
	clipStr1 = clipStr1 + " -i clip" + str(x) + "-final.mp4"

print(clipStr1)

clipStr2 = ""

for y in range(len(links)):
	clipStr2 = clipStr2 + "[" + str(y) + ":v:0][" + str(y) + ":a:0]"

clipStr2 = clipStr2 + "concat=n=" + str(len(links)) + ":v=1:a=1[outv][outa]"

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




	

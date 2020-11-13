from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#Go to https://www.kapwing.com/studio/editor/scenes to combine videos

import time
import random

import pandas as pd

def convert(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds) 


if __name__ == "__main__":

	#Get links from populated csv file
	Data = pd.read_csv("links-ASMR.csv")

	links = Data["links"]
	print(links)

	for x in range(len(links)):

		#initialize driver
		driver = webdriver.Chrome(ChromeDriverManager().install())

		#Go to Youtube Cutter website
		driver.get("https://youtube-cutter.org/")

		#driver.execute_script("window.open('https://youtube-cutter.org/','_blank');")

		#Insert Youtube link
		driver.find_element_by_xpath("//input[@id='youtubeurl']").send_keys(links[x])
		print(links[x])

		time.sleep(1)

		#Click Next
		driver.find_element_by_xpath("//button[text()='Start Cutter']").click()

		time.sleep(2)

		#Get Start time element
		startElement = driver.find_element_by_xpath("//input[@id='startTimeRange']")

		#Get End time element
		endElement = driver.find_element_by_xpath("//input[@id='endTimeRange']")

		#Find length of video
		wholeVideoLength = int(endElement.get_attribute("max"))

		#Calculate Start time
		startTime = random.randint(wholeVideoLength // 4, (3 * wholeVideoLength) // 4)

		#Calc End time
		videoLength = 120
		endTime = startTime + videoLength

		#Format start input
		startInput = "0" + convert(startTime) + ":0"

		startInputElement = driver.find_element_by_xpath("//input[@id='startTime']")
		startInputElement.clear()
		startInputElement.send_keys(startInput)

		#format end input
		endInput = "0" + convert(endTime) + ":0"

		endInputElement = driver.find_element_by_xpath("//input[@id='endTime']")
		endInputElement.clear()
		endInputElement.send_keys(endInput)

		time.sleep(2)
		
		#Download
		driver.find_element_by_xpath("//button[text()='Cut Video']").click()

		while True:
			try:
				driver.find_element_by_xpath("//a[text()=' Download File']")
				break
			except:
				time.sleep(5)

		driver.find_element_by_xpath("//a[text()=' Download File']").click()

		time.sleep(120)

		driver.quit()








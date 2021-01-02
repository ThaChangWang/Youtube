from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import time
import sys

if __name__ == "__main__":

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
	driver.get("https://www.youtube.com/results?search_query=" + sys.argv[1])

	#Scroll down to get more videos
	#driver.execute_script("scroll(0, 10000);")

	linkFile = open("linkAds.txt", "x")
	linkFile = open("linkAds.txt", "w")

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

	linkFile = open("linkAds.txt", "r")

	for line in linkFile:
		#Go to video and comment
		print(line)
		driver.get(line)
		time.sleep(2)
		driver.execute_script("scroll(0, 500);")
		time.sleep(2)

		try:
			driver.find_element_by_xpath("//div[@id='placeholder-area']").click()
			time.sleep(2)
			driver.find_element_by_xpath("//div[@id='contenteditable-root']").send_keys("Here ye here ye! \n Check out these rare " + sys.argv[1] + " videos at " + sys.argv[2] + "\n You won't be disappointed!" )
			time.sleep(2)
			driver.find_element_by_xpath("//yt-formatted-string[text()='Comment']").click()
			time.sleep(5)

		except:
			print("video skipped")

	




	driver.quit()



		







	#driver.quit()
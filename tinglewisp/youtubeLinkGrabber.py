from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import time

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
	driver.get("https://www.youtube.com/results?search_query=ASMR&sp=CAISBhABGAIwAQ%253D%253D")

	#Scroll down to get more videos
	#driver.execute_script("scroll(0, 10000);")

	#time.sleep(2)

	#Find videos
	videos = driver.find_elements_by_xpath("//a[@id='thumbnail']")
	time.sleep(2)

	#Open link file for writing
	linkFile = open("links-ASMR.csv", "a")
	linkFile.write("links\n\n")

	for x in range(len(videos)):
		#Get link from video
		videoLink = videos[x].get_attribute("href")
		print(videoLink)

		#Check for last video
		if (str(videoLink) == "None"):
			break
		else:
			#Write links to file
			linkFile.write(videoLink + "\n")

	driver.quit()



		







	#driver.quit()
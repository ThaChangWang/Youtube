
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import 

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
	driver.find_element_by_xpath('//div[@class="VfPpkd-RLmnJb"]').click()


	#driver.quit()

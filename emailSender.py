from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import time

import pandas as pd

if __name__ == "__main__":

	Data = pd.read_csv("emailstest.csv")

	emails = Data["email"]

	name = Data["name"]

	urls = Data["url"]

	driver = webdriver.Chrome(ChromeDriverManager().install())

	#Go to email login
	driver.get("https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Dgoogle%2Bmail%26oq%3Dgoogle%2Bmail%26aqs%3Dchrome..69i57j69i64j69i60l2.8480j0j1%26sourceid%3Dchrome%26ie%3DUTF-8&ec=GAZAAQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

	#Type in Email
	driver.find_element_by_xpath("//input[@type='email']").send_keys("tinglewisp")

	#Click Next
	driver.find_element_by_xpath("//div[@class='VfPpkd-RLmnJb']").click()

	time.sleep(1)

	#Type in Password
	driver.find_element_by_xpath("//input[@type='password']").send_keys("clappersglee9610")
	#driver.execute_script("arguments[0].value = '{}';".format("clappersglee9610"), passwordElement)

	#Click Next
	driver.find_element_by_xpath('//div[@class="VfPpkd-RLmnJb"]').click()

	time.sleep(1)

	#Click Google - Mail
	driver.find_element_by_xpath('//span[text()="Gmail - Google"]').click()

	time.sleep(3)


	#Click Compose
	driver.find_element_by_xpath('//div[text()="Compose"]').click()

	time.sleep(3)

	#Type in recipient email
	driver.find_element_by_xpath('//textarea[@class="vO"]').send_keys("Bob@gmail.com")

	#Type in subject
	driver.find_element_by_xpath('//input[@class="aoT"]').send_keys("New ASMR video")

	#Type in message
	driver.find_element_by_xpath('//div[@aria-label="Message Body"]').send_keys(
		"""/t Hi Asmrtist, /n /n My name is Anders Bergquist and I'm coming to you because
		I love watching your videos and have an idea for a channel. I'm hoping to make an ASMR
		channel featuring a compilation of both popular artists as well as up and coming artists.
		My goal is to provide a space for listeners to get a wide range of ASMR styles and techniques
		in one video, and maybe even find new triggers that they haven't heard before. I am
		asking for your permission to use very small segments of your videos (<2min) to include in
		my compilation. Every """)

	#Click send







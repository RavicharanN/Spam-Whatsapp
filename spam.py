from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://web.whatsapp.com/")

# Note that the content in the whatsappSite is genertated dynamically by the JS engine
# So one has to was wait till the Js content is loaded in the source
# "WebDriverWait" is set to wait for .6s before any action begins.
# So the follwing is variable os set.
wait = WebDriverWait(driver, 600)

# Set the taget and the target message
target = '"Your friend name on the whatsapp contact list"'
string = "Your message goes here"

# Waits for the Desired contact to load and selects it
x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
group_title.click()

# Specifies the location of the input box in the page.
# 'Inspect element' on the message input field of the webpage for further clarification
inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))

# Enters the string in the input box and send it desired number of times.
for i in range(20):
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1)

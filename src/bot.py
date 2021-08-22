from edgedriver import Edge
from selenium.webdriver.common.keys import Keys

driver = Edge().start()
web_elements = {}

web_elements["cookies"] = driver.find_element_by_xpath("//button[text()='Allow all cookies']")
web_elements["cookies"].click()

web_elements["words"] = driver.find_element_by_id("row1")
words = web_elements["words"].get_attribute('innerText')

while words == '':
    words = web_elements["words"].get_attribute('innerText')

web_elements["input"] = driver.find_element_by_id('inputfield')

array_words = words.split(" ")

for word in array_words:
    web_elements["input"].send_keys(word)
    web_elements["input"].send_keys(Keys.SPACE)

web_elements["timer"] = driver.find_element_by_id('timer')
timer = web_elements["timer"].get_attribute('innerText')

while timer != "0:00":
    timer = web_elements["timer"].get_attribute('innerText')

closed_alert = False

while closed_alert == False:
    try:
        driver.switch_to.alert.accept()
        closed_alert = True
    except:
        pass

web_elements["screenshot"] = driver.find_element_by_xpath('//*[@id="auswertung-result"]/h3/a')
web_elements["screenshot"].click()

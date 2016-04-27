#Check for a page is redirected or not
from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException

def waitForload(driver):
    elem = driver.find_element_by_tag_name("html")
    count = 0
    while True:
        count += 1
        if count > 20:
            #Timeout: 10 seconds
            print "Timing out after 10 seconds and returning..."
            return
        time.sleep(.3)
        try:
            elem = driver.find_element_by_tag_name("html")
        except StaleElementReferenceException:
            return

driver = webdriver.PhantomJS(executable_path="/usr/local/Cellar/phantomjs/2.1.1/bin/phantomjs")
driver.get("http://pythonscraping.com/pages/javascript/redirectDemo1.html")
waitForload(driver)
print driver.page_source

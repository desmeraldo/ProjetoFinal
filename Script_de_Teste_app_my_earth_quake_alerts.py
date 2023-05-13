import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import os
import base64

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.jrustonapps.myearthquakealerts',
    appActivity='.controllers.MainActivity',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, capabilities)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_testeaplicativo(self) -> None:
        self.driver.start_recording_screen()
                       
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.jrustonapps.myearthquakealerts:id/action_search"]')))
        actions = ActionChains(self.driver)
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="Search"]')
        el.click()

        directory = '%s/' % os.getcwd()
        file_name = 'screenshot-appmyearthquakealerts-1.png'
        self.driver.save_screenshot(directory + file_name)

        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.jrustonapps.myearthquakealerts:id/dateFromText"]')))
        actions = ActionChains(self.driver)
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Tap here"]')
        el.click()

        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="android:id/button1"]')))
        actions = ActionChains(self.driver)
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="OK"]')
        el.click()

        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.jrustonapps.myearthquakealerts:id/dateToText"]')))
        actions = ActionChains(self.driver)
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Tap here"]')
        el.click()

        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="android:id/button1"]')))
        actions = ActionChains(self.driver)
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="OK"]')
        el.click()

        file_name = 'screenshot-appmyearthquakealerts-2.png'
        self.driver.save_screenshot(directory + file_name)
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="android:id/text1"]')))
        actions = ActionChains(self.driver)
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="All Regions"]')
        el.click()

        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@text="Albania"]')))
        actions = ActionChains(self.driver)
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Albania"]')
        el.click()

        file_name = 'screenshot-appmyearthquakealerts-3.png'
        self.driver.save_screenshot(directory + file_name)

        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.jrustonapps.myearthquakealerts:id/title"]')))
        actions = ActionChains(self.driver)
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@resource-id="com.jrustonapps.myearthquakealerts:id/title"]')
        el.click()
                            
        filepath = os.path.join(directory, "screen_recording_appmyearthquakealerts.mp4")
        payload = self.driver.stop_recording_screen()
        with open(filepath, "wb") as fd:
           fd.write(base64.b64decode(payload))
                
        file_name = 'screenshot-appmyearthquakealerts-4.png'
        self.driver.save_screenshot(directory + file_name)

if __name__ == '__main__':
    unittest.main()

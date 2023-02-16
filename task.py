from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

#password
password='autoTest@0110'

op = webdriver.ChromeOptions()
#grasping your own chrome user data so please use your own chrome user data 
op.add_argument('user-data-dir=C:\\Users\\sagar.parajuli\\AppData\\Local\\Google\\Chrome\\User Data')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install(),options=op)
driver.get("https://dev.zebec.io/")
driver.maximize_window()
time.sleep(2)
phantom= driver.find_element(by=By.XPATH, value='//*[@id="headlessui-dialog-panel-2"]/div[2]/button[1]/div').click()

parent= driver.window_handles[0]
time.sleep(3)

#get instance of first pop up  window
getPop = driver.window_handles[1]
#switch to pop up window
driver.switch_to.window(getPop)
time.sleep(2)
password= driver.find_element(by=By.NAME,value='password').send_keys(password)
unlock= driver.find_element(by=By.TAG_NAME,value='button').click()
driver.switch_to.window(parent)
time.sleep(1)
sign= driver.find_element(by=By.XPATH, value='//*[@id="headlessui-dialog-panel-2"]/div[2]/button[1]').click()
time.sleep(4)
#get instance of first pop up  window
getPop = driver.window_handles[1]
#switch to pop up window
driver.switch_to.window(getPop)
approve= driver.find_element(by=By.XPATH,value='//*[@id="root"]/div/div[1]/div/div[2]/div/button[2]').click()
driver.switch_to.window(parent)
time.sleep(2)

enterSol=driver.find_element(By.CSS_SELECTOR, "input[name='amount']")
time.sleep(8)
enterSol.send_keys('0.001')
Deposit= driver.find_element(by=By.XPATH, value='//*[@id="__next"]/main/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/form/button').click()
time.sleep(2)
#get instance of first pop up  window
getPop = driver.window_handles[1]
#switch to pop up window
driver.switch_to.window(getPop)
time.sleep(2)
approve= driver.find_element(by=By.XPATH,value='/html/body/div/div/div[1]/div/div[2]/div/button[2]').click()
time.sleep(2)
driver.quit()

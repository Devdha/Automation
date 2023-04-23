from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()

code = os.environ.get('CODE')
password = os.environ.get('PASSWORD')

driver = webdriver.Chrome("chromedriver")
driver.get('https://etk.srail.co.kr/cmc/01/selectLoginForm.do')
driver.implicitly_wait(15)

driver.find_element(By.ID, 'srchDvNm01').send_keys(code)
driver.find_element(By.ID, 'hmpgPwdCphd01').send_keys(password)

driver.find_element(By.XPATH, '//*[@id="login-form"]/fieldset/div[1]/div[1]/div[2]/div/div[2]/input').click()
driver.get('https://etk.srail.kr/hpg/hra/01/selectScheduleList.do')
driver.implicitly_wait(5)
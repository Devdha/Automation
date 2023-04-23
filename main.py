from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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

dep_stn = driver.find_element(By.ID, 'dptRsStnCdNm')
dep_stn.clear()
dep_stn.send_keys('수서')

arr_stn = driver.find_element(By.ID, 'arvRsStnCdNm')
arr_stn.clear()
arr_stn.send_keys('동대구')

elm_dptDt = driver.find_element(By.ID, 'dptDt')
driver.execute_script("arguments[0].setAttribute('style', 'display: True;')", elm_dptDt)
Select(driver.find_element(By.ID, 'dptDt')).select_by_value('20230428')

elm_dptTm = driver.find_element(By.ID, "dptTm")
driver.execute_script("arguments[0].setAttribute('style','display: True;')", elm_dptTm)
Select(driver.find_element(By.ID, "dptTm")).select_by_visible_text("18")

driver.find_element(By.XPATH,"//input[@value='조회하기']").click()


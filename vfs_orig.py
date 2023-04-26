import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

NAME_BOX_XPATH = "/html/body/form/div[3]/table/tbody/tr[2]/td/div/div[2]/table/tbody/tr[1]/td[2]/table/tbody/tr/td/table/tbody/tr[3]/td[2]/input"
AURN_BOX_XPATH = "/html/body/form/div[3]/table/tbody/tr[2]/td/div/div[2]/table/tbody/tr[1]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td[2]/input"
SUBMIT_BUTTON_XPATH = "/html/body/form/div[3]/table/tbody/tr[2]/td/div/div[2]/table/tbody/tr[1]/td[2]/table/tbody/tr/td/table/tbody/tr[4]/td[2]/input[1]"
TEXT_FIELD_RESULT_XPATH = "/html/body/form/div[3]/table/tbody/tr[2]/td/div/div[2]/table/tbody/tr[1]/td[2]/table/tbody/tr/td/table/tbody/tr[5]/td/span[2]"



driver = webdriver.Chrome(executable_path='./chromedriver.exe') #download chromedriver at https://chromedriver.chromium.org/downloads
driver.get("https://www.vfsvisaonline.com/DHAOnlineTracking/OnlineTracking.aspx")

result_text_fields = []
usual_result = [
    'Application for foo has been received at DHA on date1.',
    'Application for bar has been received at DHA on date2.',
    'Application for baz has been received at DHA on date3.',
]



driver.find_element(by=By.XPATH, value=NAME_BOX_XPATH).send_keys("foo")
driver.find_element(by=By.XPATH, value=AURN_BOX_XPATH).send_keys("TRRbazbar1")
driver.find_element(by=By.XPATH, value=SUBMIT_BUTTON_XPATH).click()
time.sleep(0.5)
result_text_fields.append(driver.find_element(by=By.XPATH, value=TEXT_FIELD_RESULT_XPATH).text)
test_result = 'Application for foo has been received at DHA on date1.'
time.sleep(0.25)


driver.find_element(by=By.XPATH, value=AURN_BOX_XPATH).clear()
driver.find_element(by=By.XPATH, value=AURN_BOX_XPATH).send_keys("TRRbazbar2")
driver.find_element(by=By.XPATH, value=SUBMIT_BUTTON_XPATH).click()
time.sleep(0.5)
result_text_fields.append(driver.find_element(by=By.XPATH, value=TEXT_FIELD_RESULT_XPATH).text)
test_result = 'Application for bar has been received at DHA on date2.'
time.sleep(0.5)


driver.find_element(by=By.XPATH, value=AURN_BOX_XPATH).clear()
driver.find_element(by=By.XPATH, value=AURN_BOX_XPATH).send_keys("TRRbazbar3")
driver.find_element(by=By.XPATH, value=SUBMIT_BUTTON_XPATH).click()
time.sleep(0.5)
result_text_fields.append(driver.find_element(by=By.XPATH, value=TEXT_FIELD_RESULT_XPATH).text)
test_result = 'Application for baz has been received at DHA on date3.'
time.sleep(0.5)

driver.quit()


#print(usual_result, result_text_fields)
if usual_result == result_text_fields:
    print('Nothing new... keep waiting... :|')
else:
    print('Unusual result. Check again to see if a Visa has arrived.')
    print('Expected result: ', usual_result)
    print('Actual result: ', result_text_fields)







    

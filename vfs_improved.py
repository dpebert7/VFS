import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

NAME_BOX_XPATH = "/html/body/form/div[3]/table/tbody/tr[2]/td/div/div[2]/table/tbody/tr[1]/td[2]/table/tbody/tr/td/table/tbody/tr[3]/td[2]/input"
AURN_BOX_XPATH = "/html/body/form/div[3]/table/tbody/tr[2]/td/div/div[2]/table/tbody/tr[1]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td[2]/input"
SUBMIT_BUTTON_XPATH = "/html/body/form/div[3]/table/tbody/tr[2]/td/div/div[2]/table/tbody/tr[1]/td[2]/table/tbody/tr/td/table/tbody/tr[4]/td[2]/input[1]"
TEXT_FIELD_RESULT_XPATH = "/html/body/form/div[3]/table/tbody/tr[2]/td/div/div[2]/table/tbody/tr[1]/td[2]/table/tbody/tr/td/table/tbody/tr[5]/td/span[2]"
#https://machinelearningmastery.com/a-gentle-introduction-to-unit-testing-in-python/


class VFS:
    def __init__(self, surname, aurn):
        self.surname = surname
        self.aurn = aurn

    def get_status(self):
        #driver = webdriver.Chrome(executable_path='./chromedriver.exe') # This gives deprecation warning
        s = Service('./chromedriver.exe') #download chromedriver at https://chromedriver.chromium.org/downloads
        driver = webdriver.Chrome(service=s)
        driver.get("https://www.vfsvisaonline.com/DHAOnlineTracking/OnlineTracking.aspx")
        time.sleep(2)
        driver.find_element(by=By.XPATH, value=NAME_BOX_XPATH).send_keys(self.surname)
        driver.find_element(by=By.XPATH, value=AURN_BOX_XPATH).send_keys(self.aurn)
        driver.find_element(by=By.XPATH, value=SUBMIT_BUTTON_XPATH).click()
        time.sleep(2)
        current_status = driver.find_element(by=By.XPATH, value=TEXT_FIELD_RESULT_XPATH).text
        driver.quit()
        return(current_status)


class TestVFS(unittest.TestCase):
    def test_trp_1(self):
        vfs_trp_1 = VFS('xxxxx', 'TRRzzzzzzzzz')
        self.assertEqual(vfs_trp_1.get_status(), 'Application for zzzzzzz has been received at DHA on zzzzzzzz.', 'Unexpected status for foo')

    def test_trp_2(self):
        vfs_trp_2 = VFS('xxxxx', 'TRRzzzzzzzzz')
        self.assertEqual(vfs_trp_2.get_status(), 'Application for zzzzzzz has been received at DHA on zzzzzzzz.', 'Unexpected status for bar')

    def test_trp_3(self):
        vfs_trp_3 = VFS('xxxxx', 'TRRzzzzzzzzz')
        self.assertEqual(vfs_trp_3.get_status(), 'Application for zzzzzzz has been received at DHA on zzzzzzzz.', 'Unexpected status for baz')


unittest.main()






    

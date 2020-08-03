from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class PageIndex:
    def __init__(self, my_driver):
        self.query_top = (By.ID, 'search_query_top')
        self.query_button = (By.NAME, 'submit_search')
        self.driver = my_driver

    def search(self, item):
        try:
            search_box = WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.query_top))
            search_box.send_keys(item)
            search_button = WebDriverWait(self.driver, 4).until(ec.visibility_of_element_located(self.query_button))
            search_button.click()
        except:
            print('no se encuentra el elemento')
        #self.driver.find_element(*self.query_top).send_keys(item)
        #self.driver.find_element(*self.query_button).click()


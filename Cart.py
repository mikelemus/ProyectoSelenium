import unittest
from selenium import webdriver
import time


class Cart(unittest.TestCase):
    def test_cart(self):
        driver = webdriver.Chrome()
        driver.get('http://automationpractice.com/index.php')
        driver.find_element_by_id('search_query_top').send_keys('T-shirts')
        driver.find_element_by_name('submit_search').click()
        time.sleep(2)
        self.assertTrue('T-SHIRTS' in driver.find_element_by_xpath('//*[@id="center_column"]/h1/span[1]').text)
        driver.close()
        driver.quit()


if __name__ == '__main__':
    unittest.main()

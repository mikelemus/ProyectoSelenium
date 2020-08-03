import unittest

from selenium import webdriver

import time
from pageIndex import PageIndex
from pageItems import PageItems
from pageItem import PageItem
from selenium.webdriver.chrome.options import Options


class SearchCases(unittest.TestCase):

    def setUp(self):
        option = Options()
        option.add_argument('start-maximized')
        option.add_argument('incognito')

        #option.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=option)
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.implicitly_wait(5)
        #self.driver.maximize_window()
        self.indexPage = PageIndex(self.driver)
        self.itemsPage = PageItems(self.driver)
        self.itemPage = PageItem(self.driver)


    def test_search_no_elements(self):
        self.indexPage.search('hola')
        self.assertEqual(self.itemsPage.return_no_element_text(), 'No results were found for your search "hola"')
        self.driver.save_screenshot('no_element.jpg')

    @unittest.skip('Not needed now')
    def test_search_find_dresses(self):
        self.indexPage.search('dress')

        self.assertTrue('DRESS' in self.itemsPage.return_section_title())

    @unittest.skip('Not needed now')
    def test_search_find_tshirts(self):
        self.indexPage.search('t-shirt')

        self.assertTrue('T-SHIRT' in self.itemsPage.return_section_title())

    @unittest.skip('Not needed now')
    def test_tarea(self):
        self.indexPage.search('t-shirt')
        self.itemsPage.click_orange_button()
        self.itemPage.enter_quantity('25')
        #self.itemPage.add_elements(3)

    @unittest.skip('Not needed now')
    def test_selections(self):
        self.indexPage.search('t-shirts')
        self.itemsPage.select_by_text('Product Name: A to Z')
        time.sleep(3)
        self.itemsPage.select_by_value('reference:asc')
        time.sleep(3)
        self.itemsPage.select_by_index(2)
        time.sleep(3)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

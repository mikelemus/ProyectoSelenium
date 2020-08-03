class PageItem:

    def __init__(self, my_driver):
        self.quantity = 'quantity_wanted'
        self.plus = 'icon-plus'
        self.driver = my_driver

    def enter_quantity(self, quantity):
        self.driver.find_element_by_id(self.quantity).clear()
        self.driver.find_element_by_id(self.quantity).send_keys(quantity)

    def add_elements(self, quantity):
        for i in range(quantity):
            self.find_element_by_class_name(self.plus).click()

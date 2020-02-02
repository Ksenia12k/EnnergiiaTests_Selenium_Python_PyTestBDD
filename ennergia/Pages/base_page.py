from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import random


class BasePage:
    def __init__(self, driver, timeout=4):
        self.driver = driver
        self.driver.implicitly_wait(timeout)
        self.wait = WebDriverWait(driver, timeout)

    def open(self, link):
        self.driver.get(link)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=2):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def get_random_item(self, item_name):
        items_list = self.driver.find_elements(*item_name)
        random_item = int(random.random() * len(items_list))
        return items_list[random_item]

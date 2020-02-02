from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePage(BasePage):
    cartProductsCounter = (By.XPATH, '//li[@data-test="navCartLink"]//span.notification')
    open_menu_btn = (By.CSS_SELECTOR, 'div[data-test="navSideBar"]')
    guest_profile_btn = (By.CSS_SELECTOR, 'li[data-test="navProfileLink"]')
    section_item = (By.XPATH, '//ul[@data-test="hierarchyRoots"]//li[@role="menuitem"]')
    category_item = (By.XPATH, '//ul[@data-test="hierarchyList"]//div[@role="button"]')
    subcategory_item = (By.XPATH, '//ul[@data-test="hierarchyList"]//li[@role="menuitem"]//button[@data-test="hierarchyItemTrigger"]')

    def check_the_cart_is_empty(self):
        assert self.is_not_element_present(*self.cartProductsCounter)

    def open_menu(self):
        self.driver.find_element(*self.open_menu_btn).click()

    def choose_section(self, section_name):
        section = self.driver.find_element_by_xpath("//h3[contains(text(), '" + section_name + "')]")
        self.driver.execute_script("arguments[0].click();", section)

    def choose_category(self, category_name):
        category = self.driver.find_element_by_css_selector("div[aria-label='" + category_name + "']")
        self.driver.execute_script("arguments[0].click();", category)

    def choose_subcategory(self, subcategory_name):
        subcategory = self.driver.find_element_by_css_selector("button[aria-label='" + subcategory_name + "']")
        self.driver.execute_script("arguments[0].click();", subcategory)

    def open_guest_profile(self):
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*self.guest_profile_btn))

    def choose_random_section(self):
        random_section = self.get_random_item(self.section_item)
        self.driver.execute_script("arguments[0].click();", random_section)

    def choose_random_category(self):
        random_category = self.get_random_item(self.category_item)
        self.driver.execute_script("arguments[0].click();", random_category)

    def choose_random_subcategory(self):
        random_subcategory = self.get_random_item(self.subcategory_item)
        self.driver.execute_script("arguments[0].click();", random_subcategory)


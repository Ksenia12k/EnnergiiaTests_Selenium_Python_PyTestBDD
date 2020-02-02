from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from .base_page import BasePage


class ProductCardPage(BasePage):
    cart_icon = (By.CSS_SELECTOR, 'li[data-test="navCartLink"]')
    add_to_cart_btn = (By.CSS_SELECTOR, "div[data-test='addToCart']")
    chose_size_btn = (By.CSS_SELECTOR, 'div[data-test="productSelectorTrigger"]')
    sizes_list = (By.XPATH, '//section[@role="dialog"]//ul[@data-test="productOptionsList"]')
    sizes_item = (By.XPATH, '//section[@role="dialog"]//ul[@data-test="productOptionsList"]//li[@data-test="productOptionsListItem"]')
    add_to_wishlist_btn = (By.CSS_SELECTOR, 'button[data-test="wishListAddButton"]')

    def add_product_to_cart(self):
        if self.driver.find_elements(*self.chose_size_btn):
            self.driver.execute_script("arguments[0].click();", self.driver.find_element(*self.chose_size_btn))
            self.wait.until(EC.visibility_of_element_located(self.sizes_list))
            sizes_items_list = self.driver.find_elements(*self.sizes_item)
            for item in sizes_items_list:
                print(item.get_attribute('class'))
                if item.get_attribute('class') != 'MegaUI__plank MegaUI_button_base MegaUI_button_default option optionDisabled':
                    self.driver.execute_script("arguments[0].click();", item)
                    #ActionChains(self.driver).move_to_element(item).click(item).perform()
                    break

        self.wait.until(EC.visibility_of_element_located(self.add_to_cart_btn))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*self.add_to_cart_btn))

    def add_product_to_wishlist(self):
        self.wait.until(EC.visibility_of_element_located(self.add_to_wishlist_btn)).click()
       # self.driver.find_element(*self.add_to_wishlist_btn).click()

    def go_to_cart(self):
        self.wait.until(EC.visibility_of_element_located(self.cart_icon))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*self.cart_icon))

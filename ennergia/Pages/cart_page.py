from selenium.webdriver.common.by import By
from .base_page import BasePage
import pickle


class CartPage(BasePage):
    cartItem = (By.XPATH, "//ul[@data-test='positionsList']//li")
    guest_profile_btn = (By.CSS_SELECTOR, 'li[data-test="navProfileLink"]')

    def check_product_was_added_to_cart(self):
        cartItems = self.driver.find_elements(*self.cartItem)
        assert len(cartItems) == 1

    def save_cookies(self):
        pickle.dump(self.driver.get_cookies(), open("cookies.pkl", "wb"))

    def open_guest_profile(self):
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*self.guest_profile_btn))
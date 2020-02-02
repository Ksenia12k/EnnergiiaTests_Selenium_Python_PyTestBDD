from selenium.webdriver.common.by import By
from .base_page import BasePage


class WishListPage(BasePage):
    emptyWrapper = (By.CLASS_NAME, "emptyWrapper")
    logo = (By.CSS_SELECTOR, 'a[data-test="navHomeLink"]')
    wishlist_item = (By.XPATH, '//div[@class="wrapper"]//ul[@class="list"]//li')

    def check_wishlist_is_empty(self):
        assert self.is_element_present(*self.emptyWrapper)

    def go_to_main_page(self):
        self.driver.find_element(*self.logo).click()

    def check_if_product_was_added_to_wish_list(self):
        wishlist_items = self.driver.find_elements(*self.wishlist_item)
        assert len(wishlist_items) == 1



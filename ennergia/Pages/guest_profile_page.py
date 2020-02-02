from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base_page import BasePage


class GuestProfilePage(BasePage):
    wishlist_btn = (By.CSS_SELECTOR, 'a[aria-label="Избранное"]')

    def open_wishlist(self):
        self.wait.until(EC.visibility_of_element_located(self.wishlist_btn)).click()



from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from .base_page import BasePage


class ProductsListPage(BasePage):
    popup = (By.XPATH, '//div[@class="vue-portal-target"]//div[@role="presentation"]')
    popup_close = (By.XPATH, "//button[contains(@class, 'closeModal')]")
    product_item = (By.CSS_SELECTOR, "a[data-test='productPreviewInfo']")

    def close_popup(self):
        self.wait.until(EC.visibility_of_element_located(self.popup_close)).click()
        self.wait.until(EC.invisibility_of_element_located(self.popup))
        assert self.is_not_element_present(*self.popup)

    def check_if_popup_is_present(self):
        self.wait.until(EC.visibility_of_element_located(self.popup))
        assert self.is_element_present(*self.popup)

    def open_product_card(self):
        self.wait.until(EC.visibility_of_element_located(self.product_item))
        random_section = self.get_random_item(self.product_item)
        random_section.click()

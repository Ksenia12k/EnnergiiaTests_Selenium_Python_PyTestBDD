from pytest_bdd import scenario, when, then
import unittest


@scenario('promo_popup_form.feature', "Closing a form with a proposal to receive a promotional code")
def test_close_popup_form():
    pass


@when("open the main page")
def open_main_page(driver, home_page):
    home_page.open("https://m.ennergiia.com/")


@when("cart counter doesn't exist")
def check_the_cart_is_empty(driver, home_page):
    home_page.check_the_cart_is_empty()


@when("choose section")
def choose_section(driver, home_page):
    home_page.open_menu()
    home_page.choose_section("Дети")


@when("choose category")
def choose_category(driver, home_page):
    home_page.choose_category("Школа")


@when("choose subcategory")
def choose_subcategory(driver, home_page):
    home_page.choose_subcategory("Рюкзаки")


@then("appearance of a form with a proposal to receive a promotional code")
def is_element_present(driver, products_list_page):
    products_list_page.check_if_popup_is_present()


@then("this form can be closed")
def close_popup(driver, products_list_page):
    products_list_page.close_popup()


if __name__ == '__main__':
    unittest.main()

from pytest_bdd import scenario, when, then
import unittest


@scenario('wishlist.feature', "Adding a product to the wishlist from its card")
def test_add_product_in_wishlist():
    pass


@when("open the main page")
def open_main_page(driver, home_page):
    home_page.open("https://m.ennergiia.com/")


@when("go to the guest page")
def go_to_guest_page(driver, home_page):
    home_page.open_guest_profile()


@when("go to the wishlist")
def go_to_wish_list(driver, guest_page):
    guest_page.open_wishlist()


@when("the product list in the wishlist is empty")
def go_to_wish_list(driver, wishlist_page):
    wishlist_page.check_wishlist_is_empty()


@when("go to the main page")
def go_to_wish_list(driver, wishlist_page):
    wishlist_page.go_to_main_page()


@when("choose random section")
def go_to_wish_list(driver, home_page):
    home_page.open_menu()
    home_page.choose_random_section()


@when("choose random category")
def go_to_wish_list(driver, home_page):
    home_page.choose_random_category()


@when("choose random subcategory")
def go_to_wish_list(driver, home_page):
    home_page.choose_random_subcategory()


@when("close promo popup form")
def go_to_wish_list(driver, products_list_page):
    products_list_page.close_popup()


@when("open random product card")
def go_to_wish_list(driver, products_list_page):
    products_list_page.open_product_card()


@when("add the product to the wishlist")
def go_to_wish_list(driver, product_card_page):
    product_card_page.add_product_to_wishlist()


@then("there's 1 product in the wishlist")
def go_to_wish_list(driver, wishlist_page):
    wishlist_page.check_if_product_was_added_to_wish_list()


if __name__ == '__main__':
    unittest.main()

from pytest_bdd import scenario, when, then


@scenario('../Features/cart.feature', "Adding a product to the cart from its card")
def test_add_product_in_cart():
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


@when("close promo popup form")
def close_popup(driver, products_list_page):
    products_list_page.close_popup()


@when("any random item is added to the cart")
def add_product_to_cart(driver, products_list_page, product_card_page):
    products_list_page.open_product_card()
    product_card_page.add_product_to_cart()


@when("going to the cart")
def add_product_to_cart(driver, product_card_page):
    product_card_page.go_to_cart()


@then("there's 1 product in the cart")
def choose_subcategory(driver, cart_page):
    cart_page.check_product_was_added_to_cart()
    cart_page.save_cookies()


@then("save cookies with 1 product in the cart")
def save_cookies(driver, cart_page):
    cart_page.save_cookies()



import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from .Pages.home_page import HomePage
from .Pages.products_list_page import ProductsListPage
from .Pages.product_card_page import ProductCardPage
from .Pages.cart_page import CartPage
from .Pages.guest_profile_page import GuestProfilePage
from .Pages.wishlist_page import WishListPage


@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)

    yield driver
    driver.quit()


@pytest.fixture()
def home_page(driver):
    home_page = HomePage(driver, 4)
    return home_page


@pytest.fixture()
def product_card_page(driver):
    product_card_page = ProductCardPage(driver, 10)
    return product_card_page


@pytest.fixture()
def products_list_page(driver):
    products_list_page = ProductsListPage(driver, 4)
    return products_list_page


@pytest.fixture()
def cart_page(driver):
    cart_page = CartPage(driver, 4)
    return cart_page


@pytest.fixture()
def wishlist_page(driver):
    wishlist_page = WishListPage(driver, 4)
    return wishlist_page


@pytest.fixture()
def guest_page(driver):
    guest_page = GuestProfilePage(driver, 4)
    return guest_page

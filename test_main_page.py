from pages.main_page import MainPage
# from pages.login_page import LoginPage
import time
from pages.base_page import BasePage
# from pages.basket_page import BasketPage
# import pytest

def test_guest_should_see_travel_benefits_container(browser):
    link = "https://www.ozon.ru/travel/"
    page = BasePage(browser, link)
    page.open()
    page.should_see_benefits_container()

def test_guest_should_see_switch_pannel(browser):
    link = "https://www.ozon.ru/travel/"
    page = BasePage(browser, link)
    page.open()
    page.should_see_switch_pannel()
    page.should_see_air()
    page.should_see_railway()

def test_guest_should_see_logo(browser):
    link = "https://www.ozon.ru/travel/"
    page = BasePage(browser, link)
    page.open()
    page.should_see_main_logo()

def test_guest_should_see_legal_person_button(browser):
    link = "https://www.ozon.ru/travel/"
    page = BasePage(browser, link)
    page.open()
    page.should_see_legal_person_button()
    page.should_see_legal_person_text()
    page.should_go_to_legal_person_book()

def test_guest_should_go_to_login_form(browser):
    link = "https://www.ozon.ru/travel/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_modal()
    time.sleep(10)

def test_guest_should_see_help_link(browser):
    link = "https://www.ozon.ru/travel/"
    page = BasePage(browser, link)
    page.open()
    page.should_see_help_link()
    page.should_go_to_help_page()

def test_guest_should_see_travel_title(browser):
    link = "https://www.ozon.ru/travel/"
    page = MainPage(browser, link)
    page.open()
    page.should_see_travel_title()
    page.should_see_travel_title_text()
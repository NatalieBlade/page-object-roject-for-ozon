from pages.main_page import MainPage
from pages.search_page import SearchPage
import time
from pages.base_page import BasePage
from selenium.webdriver.support.select import Select

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
    time.sleep(5)

def test_guest_should_go_to_login_form(browser):
    link = "https://www.ozon.ru/travel/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_modal()
    time.sleep(5)

def test_guest_should_see_help_link(browser):
    link = "https://www.ozon.ru/travel/"
    page = BasePage(browser, link)
    page.open()
    page.should_see_help_link()
    page.should_go_to_help_page()
    time.sleep(5)

def test_guest_should_see_travel_title(browser):
    link = "https://www.ozon.ru/travel/"
    page = MainPage(browser, link)
    page.open()
    page.should_see_travel_title()
    page.should_see_travel_title_text()

def test_guest_should_fill_search_departure_city(browser):
    link = "https://www.ozon.ru/travel/"
    page = SearchPage(browser, link)
    page.open()
    page.should_see_departure_city_drop_down()
    page.should_be_able_to_choose_departure_city_from_drop_down()
    # page.search_input_departure_city()
    time.sleep(5)

def test_guest_should_fill_search_arrival_city(browser):
    link = "https://www.ozon.ru/travel/"
    page = SearchPage(browser, link)
    page.open()
    page.search_input_arrival_city()
    time.sleep(5)

def test_guest_can_switch_cities(browser):
    link = "https://www.ozon.ru/travel/"
    page = SearchPage(browser, link)
    page.open()
    page.search_input_departure_city()
    page.search_input_arrival_city()
    page.switch_cities_button()
    page.switch_cities_button_click()
    time.sleep(10)

def test_user_can_select_departure_date(browser):
    link = "https://www.ozon.ru/travel/"
    page = SearchPage(browser, link)
    page.open()
    page.departure_date_click()

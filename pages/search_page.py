from pages.base_page import BasePage
from pages.locators import SearchPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from faker import Faker


class SearchPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login/" in self.browser.current_url, "'login' is absent in current url"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_form")
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#register_form"), "Register form is absent"
        assert True

    def should_see_departure_city_drop_down(self):
        departure_city = self.browser.find_element(*SearchPageLocators.DEPARTURE_CITY)
        departure_city.click()
        assert self.is_element_present(*SearchPageLocators.DEPARTURE_CITY_DROP_DOWN), "There is no departure city drop down"

    def should_be_able_to_choose_departure_city_from_drop_down(self):
        departure_city = self.browser.find_element(*SearchPageLocators.FIRST_CITY_DROP_DOWN_MOSCOW)
        departure_city.click()

    def search_input_departure_city(self):
        departure_city = self.browser.find_element(*SearchPageLocators.DEPARTURE_CITY)
        departure_city.send_keys("Москва")

    def search_input_arrival_city(self):
        arrival_city = self.browser.find_element(*SearchPageLocators.ARRIVAL_CITY)
        arrival_city.send_keys("Санкт-Петербург")

    def switch_cities_button(self):
        assert self.is_element_present(*SearchPageLocators.SWITCH_BUTTON), "There is no switch button"

    def switch_cities_button_click(self):
        button = self.browser.find_element(*SearchPageLocators.SWITCH_BUTTON)
        button.click()

    def should_be_departure_date_area(self):
        assert self.is_element_present(*SearchPageLocators.DEPARTURE_DATE), "There is no departure date area"

    def departure_date_click(self):
        area = self.browser.find_element(*SearchPageLocators.DEPARTURE_DATE)
        area.click()

    def should_see_calendar_drop_down(self):
        assert self.is_element_present(*SearchPageLocators.CALENDAR_DROPDOWN), "There is no calendar"

    def select_departure_date(self):
        date = self.browser.find_element(*SearchPageLocators.DEPARTURE_DATE_CHOICE)
        date.click()
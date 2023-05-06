from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoAlertPresentException
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators
from .locators import MainPageLocators

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def should_see_main_logo(self):
        assert self.is_element_present(*BasePageLocators.MAIN_LOGO), "Logo is presented"

    def should_see_legal_person_button(self):
        assert self.is_element_present(*BasePageLocators.LEGAL_PERSON_BUTTON)

    def should_see_legal_person_text(self):
        legal_text = self.browser.find_element(*BasePageLocators.LEGAL_PERSON_BUTTON)
        assert legal_text.text == "Бронируйте как юрлицо", "There is no legal text"

    def should_go_to_legal_person_book(self):
        legal_link = self.browser.find_element(*BasePageLocators.LEGAL_PERSON_BUTTON)
        legal_link.click()
        assert self.browser.url_contains('https://www.ozon.ru/business/')

    def should_see_help_link(self):
        assert self.is_element_present(*BasePageLocators.HELP_LINK), "There is no help link"

    def should_go_to_help_page(self):
        link = self.browser.find_element(*BasePageLocators.HELP_LINK)
        link.click()

    def go_to_login_modal(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_HEAD)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_HEAD), "Login link is not presented"

    def should_see_switch_pannel(self):
        assert self.is_element_present(*MainPageLocators.SWITCH_PANNEL), "There is no switch pannel"

    def should_see_air(self):
        air_link = self.browser.find_element(*BasePageLocators.AIR_LINK)
        assert air_link.text == 'АВИАБИЛЕТЫ', "There is no air link"

    def should_see_railway(self):
        railway_link = self.browser.find_element(*BasePageLocators.RAILWAY_LINK)
        assert railway_link.text == 'ЖД БИЛЕТЫ', "There is no railway link"

    def should_see_benefits_container(self):
        assert self.is_element_present(*MainPageLocators.BENEFITS_CONTAINER), "Tere is no benefits container"
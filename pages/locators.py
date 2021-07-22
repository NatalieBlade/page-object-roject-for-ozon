from selenium.webdriver.common.by import By

class MainPageLocators():
    BENEFITS_CONTAINER = (By.CSS_SELECTOR, "#layoutPage > div.a4e4 > div:nth-child(7) > div > div.b5y9.b5y > div.d7g8.b5y1")
    SWITCH_PANNEL = (By.CSS_SELECTOR, "#layoutPage > div.a4e4 > div:nth-child(4) > div > div.b5y8.b5y > div")
    TRAVEL_TITLE = (By.CSS_SELECTOR, "#layoutPage > div.a4e4 > div.c3s2.c3s3 > div > div:nth-child(1) > h1")

class BasePageLocators():
    # LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    # USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_HEAD = (By.CSS_SELECTOR, "#layoutPage > div.a4e4 > header > div.c5y1 > div.c5y6 > div.b2x4.c5y7 > div.a0k9.a9c2.b2x7 > svg")
    AIR_LINK = (By.CSS_SELECTOR, '#layoutPage > div.a4e4 > div:nth-child(4) > div > div.b5y8.b5y > div > div > div > div:nth-child(1) > div > button > div > div > span')
    RAILWAY_LINK = (By.CSS_SELECTOR, "#layoutPage > div.a4e4 > div:nth-child(4) > div > div.b5y8.b5y > div > div > div > div:nth-child(2) > div > button > div > div > span")
    MAIN_LOGO = (By.CSS_SELECTOR, "#layoutPage > div.a4e4 > div:nth-child(4) > div > div:nth-child(1) > img")
    LEGAL_PERSON_BUTTON = (By.CSS_SELECTOR, "#layoutPage > div.a4e4 > div:nth-child(4) > div > div:nth-child(3) > a")
    HELP_LINK = (By.CSS_SELECTOR, "#layoutPage > div.a4e4 > div:nth-child(4) > div > div.b5y2.b5y > a")
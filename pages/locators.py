from selenium.webdriver.common.by import By

class MainPageLocators():
    SWITCH_PANNEL = (By.NAME, "travelSwitchFunnels")
    TRAVEL_TITLE = (By.CSS_SELECTOR, "travelTitle")

class BasePageLocators():
    LOGIN_HEAD = (By.CSS_SELECTOR, "#layoutPage > div.a4e4 > header > div.c5y1 > div.c5y6 > div.b2x4.c5y7 > div.a0k9.a9c2.b2x7 > svg")
    AIR_LINK = (By.CSS_SELECTOR, '#layoutPage > div.a4e4 > div:nth-child(4) > div > div.b5y8.b5y > div > div > div > div:nth-child(1) > div > button > div > div > span')
    RAILWAY_LINK = (By.CSS_SELECTOR, "#layoutPage > div.a4e4 > div:nth-child(4) > div > div.b5y8.b5y > div > div > div > div:nth-child(2) > div > button > div > div > span")
    MAIN_LOGO = (By.CSS_SELECTOR, "#layoutPage > div.a4e4 > div:nth-child(4) > div > div:nth-child(1) > img")
    LEGAL_PERSON_BUTTON = (By.CSS_SELECTOR, "#layoutPage > div.a4e4 > div:nth-child(4) > div > div:nth-child(3) > a")
    HELP_LINK = (By.CSS_SELECTOR, "#layoutPage > div.a4e4 > div:nth-child(4) > div > div.b5y2.b5y > a")

class SearchPageLocators():
    SEARCH_FORM = (By.CSS_SELECTOR, "#layoutPage > div.a4e4 > div.c3s2.c3s3 > div > div:nth-child(3)")
    DEPARTURE_CITY = (By.CSS_SELECTOR, "#layoutPage > div.a4e4 > div.c3s2.c3s3 > div > div:nth-child(3) > form > div > div:nth-child(1) > label > div._3tp2._99Og > div > input")
    ARRIVAL_CITY = (By.CSS_SELECTOR, "#layoutPage > div.a4e4 > div.c3s2.c3s3 > div > div:nth-child(3) > form > div > div:nth-child(3) > label > div._3tp2._99Og > div > input")
    SWITCH_BUTTON = (By.CSS_SELECTOR, "#layoutPage > div.a4e4 > div.c3s2.c3s3 > div > div:nth-child(3) > form > div > div.d8i7._2avF._2w-L > button > div > svg")
    DEPARTURE_DATE = (By.CSS_SELECTOR, "#layoutPage > div.a4e4 > div.c3s2.c3s3 > div > div:nth-child(3) > form > div > div._3zcl.d8n0.d8j0 > div > label > div > div._3tp2._99Og.d8p7 > div")
    ARRIVAL_DATE = (By.CSS_SELECTOR, "#layoutPage > div.a4e4 > div.c3s2.c3s3 > div > div:nth-child(3) > form > div > div._3zcl.d8n0.d8j0 > div._176J.d8n1 > label > div > div.d8p9._2avF._2w-L > button > div > svg")
    PASSENGERS_CHOICE = (By.CSS_SELECTOR, "#layoutPage > div.a4e4 > div.c3s2.c3s3 > div > div:nth-child(3) > form > div > div._3zcl.d8j2 > div._176J.d8m4 > label > div > div > div._3wcl._99Og > div > button > div > svg > path")
    FIRST_CITY_DROP_DOWN_MOSCOW = (By.CSS_SELECTOR, "body > div:nth-child(35) > div > div._29Sp > div > div:nth-child(1) > div > span.d8m0")
    DEPARTURE_DATE_CHOICE = (By.CSS_SELECTOR, "body > div:nth-child(35) > div > div._29Sp > div > div.d6c0 > div:nth-child(2) > table > tbody > tr:nth-child(5) > td:nth-child(4) > div > div")
    CALENDAR_DROPDOWN = (By.CSS_SELECTOR, "body > div:nth-child(35) > div > div._29Sp > div > div.d6c0")
    DEPARTURE_CITY_DROP_DOWN = (By.CSS_SELECTOR, "body > div:nth-child(35) > div")
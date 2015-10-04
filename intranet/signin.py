import json

from selenium import webdriver


class GoogleRobot(object):
    login_url = "https://accounts.google.com/Login"
    account_url = "https://myaccount.google.com"

    def __init__(self, driver, user_details):
        self.driver = driver
        self.email = user_details["email"]
        self.password = user_details["password"]

    def navigate_to_login_page(self):
        self.driver.get(self.login_url)

    def sign_in_to_google_account(self):
        input_button = self.driver.find_element_by_id("Email")
        input_button.send_keys(self.email)

        next_button = self.driver.find_element_by_id("next")
        next_button.click()

        self.driver.implicitly_wait(1)

        input_button = self.driver.find_element_by_id("Passwd")
        input_button.send_keys(self.password)

        sign_in_button = self.driver.find_element_by_id("signIn")
        sign_in_button.click()


class IntranetRobot(object):
    homepage_url = "https://intranet.stxnext.pl/bugs/my"

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_homepage(self):
        self.driver.get(self.homepage_url)

    def sign_in_as_employee(self):
        button = self.driver.find_element_by_css_selector(
            "#one_column > div > div.box_btn_login > a:nth-child(1)"
        )
        assert button, "Can't find 'Employee' button"
        button.click()


if __name__ == "__main__":
    driver = webdriver.Firefox()

    with open('details.json') as data_file:
        user_details = json.load(data_file)

    google = GoogleRobot(driver, user_details)
    google.navigate_to_login_page()
    google.sign_in_to_google_account()

    intranet = IntranetRobot(driver)
    intranet.navigate_to_homepage()
    intranet.sign_in_as_employee()

    driver.close()

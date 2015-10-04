import sys
import json

from selenium import webdriver


class FacebookRobot(object):
    login_url = "https://www.facebook.com"

    def __init__(self, driver, user_details):
        self.driver = driver
        self.email = user_details["email"]
        self.password = user_details["password"]

    def navigate_to_login_page(self):
        self.driver.get(self.login_url)

    def sign_in(self):
        input_button = self.driver.find_element_by_id("email")
        input_button.send_keys(self.email)

        input_button = self.driver.find_element_by_id("pass")
        input_button.send_keys(self.password)

        sign_in_button = self.driver.find_element_by_css_selector(
            "#loginbutton input[type='submit']"
        )
        sign_in_button.click()

    def post_message(self, msg):
        post_input = self.driver.find_element_by_css_selector(
            "#mentionsInput textarea"
        )
        post_input.send_keys(msg)

        submit_button = self.driver.find_element_by_css_selector(
            "#pagelet_composer button[type='submit']"
        )
        submit_button.click()

        self.driver.implicitly_wait(2)


if __name__ == "__main__":
    try:
        message = sys.argv[1]
    except IndexError:
        sys.exit("Please write message as first argument")

    driver = webdriver.Firefox()

    with open('details.json') as data_file:
        user_details = json.load(data_file)

    facebook = FacebookRobot(driver, user_details)
    facebook.navigate_to_login_page()
    facebook.sign_in()
    facebook.post_message(message)

    driver.close()

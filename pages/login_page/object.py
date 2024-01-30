from core.data_classes import Config
from core.base_page import BaseScreen
from pages.login_page.elements import LoginPageEle
from assertpy import assert_that
from selenium.webdriver.common.action_chains import ActionChains


class LoginPageObj(BaseScreen):
    def __init__(self, config: Config):
        super().__init__(config)
        self.resource_url = "my-account"
        self.login_page_ele = LoginPageEle

    # Page actions

    def open(self):
        self.log.info(f"Open the {self.url} page")
        self.driver.get(self.url)

    def enter_username(self, username):
        self.log.info(f"input username in the {self.login_page_ele.input_username.name}")
        self.se_helper.get_element(self.login_page_ele.input_username).send_keys(username)

    def enter_password(self, password):
        self.log.info(f"input password in the {self.login_page_ele.input_password.name}")
        self.se_helper.get_element(self.login_page_ele.input_password).send_keys(password)

    def click_login(self):
        self.log.info(f"Click the {self.login_page_ele.login_button.name}")
        self.se_helper.get_element(self.login_page_ele.login_button).click()

    # Page assertions

    def verify_page_title(self):
        self.log.info("Verify the login page title")
        title = self.driver.title
        assert_that(title).contains("My Account")

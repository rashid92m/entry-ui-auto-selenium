from core.data_classes import Config
from core.base_page import BaseScreen
from pages.my_account_page.elements import MyAccountPageEle
from assertpy import assert_that
from selenium.webdriver.common.action_chains import ActionChains



class MyAccountPageObj(BaseScreen):
    def __init__(self, config: Config):
        super().__init__(config)
        self.resource_url = "my-account"
        self.myaccount_page_ele = MyAccountPageEle

    # Page actions

    def open(self):
        self.log.info(f"Open the {self.url} page")
        self.driver.get(self.url)


    def click_orders(self):
        self.log.info(f"Click the {self.myaccount_page_ele.lnk_orders.name}")
        self.se_helper.get_element(self.myaccount_page_ele.lnk_orders).click()

    # Page assertions

    def verify_page_title(self):
        self.log.info("Verify the page title")
        title = self.driver.title
        assert_that(title).contains("My Account")

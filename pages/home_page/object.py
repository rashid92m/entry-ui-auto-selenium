from core.data_classes import Config
from core.base_page import BaseScreen
from pages.home_page.elements import HomePageEle


class HomePageObj(BaseScreen):
    def __init__(self, config: Config):
        super().__init__(config)
        self.resource_url = ""
        self.home_page_ele = HomePageEle

    # Page actions

    def open(self):
        self.log.info(f"Open the {self.url} page")
        self.driver.maximize_window()
        self.driver.get(self.url)

    def click_my_account(self):
        self.log.info(f"Click the {self.home_page_ele.my_account_menu.name}")
        self.se_helper.get_element(self.home_page_ele.my_account_menu).click()

    def verify_page_title(self):
        self.log.info("Verify the page title")
        title = self.driver.title
        assert title == "Automation Practice Site"


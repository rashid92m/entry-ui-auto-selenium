from core.data_classes import Config
from core.base_page import BaseScreen
from pages.shop_page.elements import ShopPageEle
from assertpy import assert_that


class ShopPageObj(BaseScreen):
    def __init__(self, config: Config):
        super().__init__(config)
        self.resource_url = "shop"
        self.shop_page_ele = ShopPageEle

    # Page actions

    def open(self):
        self.log.info(f"Open the {self.url} page")
        self.driver.get(self.url)

    def select_android(self):
        self.log.info(f"Click the {self.shop_page_ele.lnk_android.name}")
        self.se_helper.get_element(self.shop_page_ele.lnk_android).click()

    # Page assertions

    def verify_page_title(self):
        self.log.info("Verify the page title")
        title = self.driver.title
        assert_that(title).contains("Products")
